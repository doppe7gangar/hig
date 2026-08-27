#!/usr/bin/env python3
"""Detect unfilled template text without banning ordinary vocabulary.

Three gates grew the same defect independently: a list of banned strings
matched as a substring against the whole of DESIGN.md. Twice that made a
gate unpassable, because the banned words were the ones its own template
mandates -- check_interaction banned "user action" and "system response"
while requiring a table headed with them, check_divergence banned
"direction a" while accepting "### Direction A" as a heading. The third
is a landmine rather than a wall: "todo" and "item 1" are perfectly
ordinary in a notes or commerce product, and check_content *requires*
realistic content, so the two rules pull against each other.

The distinction that actually matters is not which words, but where.

  LOOSE  - phrases with no legitimate use anywhere: lorem ipsum, and the
           aesthetic labels the divergence protocol rejects as reasons.
           A substring match is right, and false positives are not a
           real risk.

  STRICT - words that are placeholders only when they stand alone: as a
           whole table cell, a whole bullet, a whole line, or wrapped in
           a marker such as [todo]. "Each ticket can carry an inline
           todo list" is a filled-in design, not an unfilled template.

Both are exported so a caller states which kind it means.
"""

import re

# Markdown scaffolding to strip before asking "is this slot empty?".
# A list marker is punctuation followed by whitespace, which is what
# separates "* " from the "**" of a bold label -- stripping emphasis
# here ate the label and let "**When it becomes real:** TBD" through.
_MARKER = re.compile(r"^\s*(?:[-+*]\s+|>\s*|#{1,6}\s+)+")
_WRAP = re.compile(r"^(\*\*|__|\*|_|`)(.+?)\1$")
_BOLD_LABEL = re.compile(r"^\*\*[^*]+\*\*\s*:?\s*")


def _clean(s):
    s = _MARKER.sub("", s.strip()).strip()
    m = _WRAP.match(s)
    return (m.group(2) if m else s).strip()


def _units(text):
    """Every span a human would call 'one filled-in slot'."""
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("|"):
            for cell in stripped.strip("|").split("|"):
                yield _clean(cell)
            continue
        body = _MARKER.sub("", stripped).strip()
        yield _clean(body)
        # "**When the change becomes real:** TBD" -- label filled in,
        # value not. Run on the bullet-stripped text, which still has
        # its emphasis markers.
        without = _BOLD_LABEL.sub("", body).strip()
        if without and without != body:
            yield _clean(without)


def find(text, loose=(), strict=()):
    """Placeholders present in `text`, in the order given.

    `loose` matches anywhere. `strict` matches only a standalone slot or
    an explicitly marked one.
    """
    low = text.lower()
    hits = []

    for p in loose:
        if p.lower() in low and p not in hits:
            hits.append(p)

    if strict:
        marked = {p.lower(): re.compile(
            r"[\[\{<]\s*" + re.escape(p.lower()) + r"\s*[\]\}>]"
            r"|^\s*" + re.escape(p.lower()) + r"\b\s*[:.]?\s*$",
            re.M) for p in strict}
        units = {u.lower() for u in _units(text) if u}
        for p in strict:
            key = p.lower()
            if p in hits:
                continue
            if key in units or marked[key].search(low):
                hits.append(p)
    return hits
