#!/usr/bin/env python3
"""Check that every quoted string in an answer is verbatim in the corpus.

The whole premise of this skill is "quote, don't paraphrase from memory."
Reading a stress-test answer by eye can't tell the two apart -- a rewritten
quote in Apple's voice reads exactly like a real one, and it's the single
worst failure this thing can have. So every "..." span an answer attributes
to Apple gets looked up.

Matching is normalized, not literal: Apple's pages use curly quotes and
en/em dashes, answers straighten them, and a quote spanning a link picks up
markdown brackets. Whitespace, quote characters, dashes, and markdown are
flattened on both sides, so only a real wording difference fails.

Misses are graded, because they are not equally bad:

  ELIDED     quote uses "..." and every segment is present, in order.
             Honest shortening. Not a defect.
  TRUNCATED  the quote is a true prefix of a real sentence but closes with
             a period Apple didn't put there, asserting the rule stops
             where it doesn't -- "essential commands." where the source
             reads "essential commands that people use frequently." A
             quote ending mid-clause on a comma is not flagged; that's
             ordinary inline quotation and claims nothing.
  SOURCE     not in the corpus but present in the code under review. A
             code review quotes the code too -- a UI string, a label it's
             criticizing -- and those aren't claims about Apple.
  ALTERED    not found in either. Either a paraphrase presented inside
             quotation marks, or two separate rules merged into one
             sentence Apple never wrote. This is the one that matters.

Point it at any text that quotes the HIG -- a draft answer, a design review,
a PR description:

    python3 verify_quotes.py review.md
    python3 verify_quotes.py review.md --project ~/src/MyApp
    cat draft.md | python3 verify_quotes.py -

`--project` defaults to the current directory, so running it from the repo
being reviewed already does the right thing.

Exits non-zero if anything is ALTERED, so it can gate a document the same
way a linter gates code.
"""

import argparse
import os
import re
import sys
import unicodedata

REFS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "references")

# Quoted spans, straight or curly. Short quotes are skipped -- "Done" or
# "sidebar" match everywhere and prove nothing.
QUOTE_RE = re.compile(r'["“]([^"“”]{25,400})["”]')

# Every transcript opens with the skill's own SKILL.md echoed back; those
# aren't Apple quotes. The answer proper starts after this marker.
SKILL_MD_MARKER = "ARGUMENTS:"

MIN_LEN = 25


def norm(s):
    """Flatten everything that legitimately varies between the two."""
    s = unicodedata.normalize("NFKD", s)
    s = s.replace("’", "'").replace("‘", "'")
    s = s.replace("“", '"').replace("”", '"')
    s = re.sub(r"[–—−]", "-", s)
    # Elision marks, normalized to one spelling. SKILL.md asks for "[…]"
    # when cutting from the middle of a quote, so a checker that only
    # understood "..." flagged writers for following its own instruction.
    s = re.sub(r"\[\s*(?:\.\.\.|…)\s*\]|…", "...", s)
    s = re.sub(r"[*_`]", "", s)                      # markdown emphasis
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)   # links -> label
    # A quote often keeps the link text and drops the URL, leaving a
    # bare "[Color]" where the source has "[Color](https://...)".
    # Without this the brackets alone read as a reworded quote.
    s = re.sub(r"\[([^\]\n]*)\]", r"\1", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()


def load_corpus():
    blob = []
    for root, _, files in os.walk(REFS):
        for f in files:
            if f.endswith(".md"):
                p = os.path.join(root, f)
                blob.append(norm(open(p, encoding="utf-8", errors="replace").read()))
    return "\n".join(blob)


SOURCE_EXT = (".swift", ".m", ".mm", ".h", ".js", ".jsx", ".ts", ".tsx",
              ".kt", ".java", ".py", ".strings", ".json", ".yaml", ".yml")
SKIP_DIRS = {".git", ".claude", "node_modules", "build", ".build",
             "DerivedData", "Pods", "__pycache__"}


def load_project(root):
    """Text of the code under review, for telling code quotes apart."""
    if not root or not os.path.isdir(root):
        return ""
    blob = []
    for dirpath, dirnames, files in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for f in files:
            if not f.endswith(SOURCE_EXT):
                continue
            p = os.path.join(dirpath, f)
            try:
                if os.path.getsize(p) > 2_000_000:
                    continue
                blob.append(norm(open(p, encoding="utf-8",
                                      errors="replace").read()))
            except OSError:
                continue
    return "\n".join(blob)


def classify(q, corpus, project=""):
    if q in corpus:
        return "VERBATIM"

    # A code review quotes the code as well as the HIG -- UI strings, a
    # label it's criticizing, its own scare-quoted phrase. Those aren't
    # claims about what Apple wrote, and reporting them as altered Apple
    # quotes makes the tool useless exactly where it's most wanted: on a
    # real review of a real project. If the text is in the reviewed
    # source, that's what it is.
    if project and q.rstrip(" .,;:-") in project:
        return "SOURCE"

    # Explicit elision: "a... b" is fine if a and b both appear, in order,
    # close enough together to plausibly be the same passage.
    if "..." in q:
        parts = [p.strip() for p in q.split("...") if len(p.strip()) >= 12]
        if parts:
            # The last segment usually stops mid-sentence and closes with a
            # period the source doesn't have, so allow it to be a prefix.
            parts[-1] = parts[-1].rstrip(" .,;:-")
            pos = 0
            for p in parts:
                i = corpus.find(p, pos)
                if i == -1:
                    break
                pos = i + len(p)
            else:
                return "ELIDED"

    # A quote that is a true prefix of a real sentence is accurate as far
    # as it goes. Whether that's a defect depends entirely on how it ends.
    stripped = q.rstrip(" .,;:-")
    if len(stripped) >= MIN_LEN and stripped in corpus:
        # Ending on a comma or mid-clause is ordinary inline quotation --
        # "the system automatically generates variants you don't provide,"
        # dropped into a sentence of your own claims nothing about where
        # Apple's sentence ended.
        if not q.rstrip().endswith((".", "!", "?")):
            return "VERBATIM"
        # A terminal period the source doesn't have is different: it
        # asserts the rule stops there, and Apple's qualifier is usually
        # what got cut.
        return "TRUNCATED"

    return "ALTERED"


FENCE_RE = re.compile(r"^```.*?^```", re.M | re.S)
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")


def segments(text):
    """Split into stretches within which quote pairing is meaningful.

    A `"` only marks a quotation if it pairs with another one, and the
    regex pairs whatever two quote characters it meets. That makes
    pairing fragile in both directions:

    Source code is full of string literals, so the regex spans from one
    literal's closing quote to the next one's opening quote --
    `Toggle("Allow Notifications", isOn: $on)` followed by
    `Text("Notifications")` yields `, isOn: $on) Text(` as a
    "quotation." Seven false alarms out of ten on a SwiftUI answer.

    And deleting the code to avoid that is worse: a fenced block holding
    an odd number of quotes flips the parity of everything after it, so
    the *gaps between* real quotations start getting captured instead of
    the quotations themselves.

    Both go away if pairing simply never crosses a boundary it has no
    business crossing. Code blocks are dropped, and each blank-line
    paragraph is scanned on its own -- a real quotation never spans a
    paragraph break -- so an unbalanced quote can only corrupt the
    paragraph it appears in.
    """
    text = FENCE_RE.sub("\n\n", text)
    # Inline code keeps its text -- Apple's own rules contain symbol names
    # ("Use the `.prominent` style for key actions"), so blanking it out
    # would break the very quotes being checked. Only the quote characters
    # inside it are dropped, since those are what corrupt pairing.
    text = INLINE_CODE_RE.sub(
        lambda m: re.sub(r'["“”]', "", m.group(0).strip("`")), text)
    return [s for s in re.split(r"\n\s*\n", text) if s.strip()]


QUOTE_CHAR_RE = re.compile(r'["“”]')


def resolve(seg, corpus, project):
    """Pick the quote pairing the evidence supports.

    Which quote character opens and which closes is genuinely ambiguous
    for straight quotes, and one stray or unbalanced quote flips the
    parity of the whole paragraph -- after which the checker reads the
    *gaps between* real quotations as if they were the quotations, and
    calls every one of them altered.

    There's no way to settle that lexically, but there is an empirical
    way: try both pairings and keep whichever produces more spans that
    actually exist in the corpus or the code. A pairing that lines up
    with reality is the right one; the off-by-one alternative yields
    fragments starting mid-clause that match nothing.
    """
    marks = [m.start() for m in QUOTE_CHAR_RE.finditer(seg)]
    best = []
    best_score = -1
    for offset in (0, 1):
        spans = []
        for a, b in zip(marks[offset::2], marks[offset + 1::2]):
            text = seg[a + 1:b]
            q = norm(text)
            if MIN_LEN <= len(q) <= 400:
                spans.append((text, classify(q, corpus, project)))
        score = sum(1 for _, v in spans if v in SOUND)
        # Prefer the pairing with more grounded spans; on a tie keep the
        # natural one, so a clean document isn't reinterpreted.
        if score > best_score:
            best, best_score = spans, score
    return best


def answer_body(text):
    i = text.find(SKILL_MD_MARKER)
    return text[i:] if i != -1 else text


SOUND = ("VERBATIM", "ELIDED", "SOURCE")


def main(paths, project_dir=""):
    corpus = load_corpus()
    project = load_project(project_dir)
    tally = {"VERBATIM": 0, "ELIDED": 0, "SOURCE": 0,
             "TRUNCATED": 0, "ALTERED": 0}
    for path in paths:
        if path == "-":
            label, raw = "(stdin)", sys.stdin.read()
        else:
            label = os.path.basename(path)
            raw = open(path, encoding="utf-8", errors="replace").read()
        seen, graded = set(), []
        for seg in segments(answer_body(raw)):
            for text, verdict in resolve(seg, corpus, project):
                q = norm(text)
                if q in seen:
                    continue
                seen.add(q)
                tally[verdict] += 1
                graded.append((verdict, text.strip()))
        clean = sum(1 for v, _ in graded if v in SOUND)
        print(f"{label:32} {clean:3}/{len(graded):3} sound")
        for verdict, q in graded:
            if verdict in SOUND:
                continue
            snip = q if len(q) < 140 else q[:137] + "..."
            print(f"    {verdict}: {snip}")

    n = sum(tally.values())
    if n:
        sound = sum(tally[k] for k in SOUND)
        print(f"\n{sound}/{n} sound ({100*sound//n}%)  |  "
              f"verbatim {tally['VERBATIM']}, elided {tally['ELIDED']}, "
              f"source {tally['SOURCE']}, truncated {tally['TRUNCATED']}, "
              f"altered {tally['ALTERED']}")
    return 1 if tally["ALTERED"] else 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser(
        description="Grade quoted spans in a draft against the HIG corpus.")
    ap.add_argument("paths", nargs="+",
                    help="files to check, or - for stdin")
    ap.add_argument("--project", default=".", metavar="DIR",
                    help="source tree under review; quotes of its own text "
                         "are reported as SOURCE rather than altered "
                         "(default: current directory)")
    a = ap.parse_args()
    sys.exit(main(a.paths, a.project))
