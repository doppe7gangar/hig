#!/usr/bin/env python3
"""Index the UIKit, AppKit and SwiftUI component surface.

api-map.md answers "this HIG concept -> that symbol", but only for the
147 pages where Apple happened to link one. It has 339 symbols. The
reverse question has no answer at all: *is* there a system component for
this, and what is it called? That gap is why a review can spot a
hand-rolled modal only if the HIG page for modality happened to name
UISheetPresentationController.

Depth is the whole design decision here. The framework landing pages are
shallow -- twelve entries that are themselves category pages. One level
down gives symbol lists with a one-line abstract each, which is exactly
the altitude that answers "what is this called". Two levels down is
method signatures and initialiser overloads: thousands of pages, and
nothing a design review would ever cite. So this walks to the category
pages and keeps the abstracts -- descending one further level only where
a category page turns out to hold more collections rather than symbols,
which is how Apple files whole families like Table views and Collection
views. Stopping cleanly at category depth cost UITableView, which is a
conspicuous thing for a component index to lack.

    python3 scripts/scrape_frameworks.py            # all three
    python3 scripts/scrape_frameworks.py --only swiftui
"""

import argparse
import collections
import json
import os
import sys
import time
import urllib.error
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
REFS = os.path.join(REPO, ".claude", "skills", "apple-hig", "references")
CACHE = os.path.join(REPO, ".cache", "frameworks")

BASE = "https://developer.apple.com/tutorials/data/documentation"
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

FRAMEWORKS = {
    "swiftui": "SwiftUI",
    "uikit": "UIKit",
    "appkit": "AppKit",
}

# Sections that are housekeeping rather than component surface. Keeping
# them would bury the useful entries under enumerations and macros.
SKIP_SECTIONS = {
    "deprecated", "reference", "protocols", "structures", "macros",
    "enumerations", "classes", "variables", "functions", "type aliases",
    "tool support",
}


def fetch(path, pause=0.15):
    """Fetch one DocC page, caching so a re-run costs nothing."""
    safe = path.replace("/", "_")
    cached = os.path.join(CACHE, safe + ".json")
    if os.path.exists(cached):
        try:
            return json.load(open(cached, encoding="utf-8"))
        except Exception:
            pass
    url = f"{BASE}/{path}.json"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            data = json.loads(r.read().decode("utf-8"))
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError):
        return None
    os.makedirs(CACHE, exist_ok=True)
    json.dump(data, open(cached, "w", encoding="utf-8"))
    time.sleep(pause)
    return data


def abstract_of(ref):
    parts = ref.get("abstract") or []
    return " ".join(p.get("text", "") for p in parts if isinstance(p, dict)).strip()


def path_of(identifier):
    return identifier.split("documentation/")[-1] if identifier else ""


def entry(framework, section, category, group, ref):
    return {
        "framework": framework,
        "section": section,
        "category": category,
        "group": group,
        "symbol": ref.get("title", ""),
        "abstract": abstract_of(ref),
        "url": "https://developer.apple.com" + (ref.get("url") or ""),
    }


def walk_framework(slug, name):
    """Landing -> sections -> category pages -> symbols."""
    root = fetch(slug)
    if not root:
        print(f"  {name}: could not fetch", file=sys.stderr)
        return []

    out = []
    for section in root.get("topicSections", []):
        stitle = section.get("title", "")
        if stitle.strip().lower() in SKIP_SECTIONS:
            continue
        for ident in section.get("identifiers", []):
            ref = root.get("references", {}).get(ident, {})
            cat = ref.get("title", "")
            child = fetch(path_of(ident))
            if not child:
                continue
            crefs = child.get("references", {})
            for csec in child.get("topicSections", []):
                gtitle = csec.get("title", "")
                for cid in csec.get("identifiers", []):
                    r = crefs.get(cid, {})
                    title = r.get("title", "")
                    if not title:
                        continue

                    if r.get("kind") == "symbol":
                        out.append(entry(name, stitle, cat, gtitle, r))
                        continue

                    # Not a symbol: Apple nests whole component families
                    # behind another collection page. "Table views" and
                    # "Collection views" both sit inside UIKit's
                    # "Container views" that way, which is how a stop at
                    # this depth loses UITableView entirely -- a fairly
                    # load-bearing omission for a component index.
                    # Recurse one more level, but only into collections.
                    if r.get("kind") != "article" and "documentation/" not in cid:
                        continue
                    grand = fetch(path_of(cid))
                    if not grand:
                        continue
                    grefs = grand.get("references", {})
                    for gsec in grand.get("topicSections", []):
                        for gid in gsec.get("identifiers", []):
                            gr = grefs.get(gid, {})
                            if gr.get("title") and gr.get("kind") == "symbol":
                                out.append(entry(name, stitle, cat,
                                                 f"{gtitle} / {title}", gr))
    return out


def write_index(rows):
    by_fw = collections.defaultdict(lambda: collections.defaultdict(list))
    for r in rows:
        by_fw[r["framework"]][r["category"]].append(r)

    out = [
        "# Framework index: what the system already provides",
        "",
        f"{len(rows)} component symbols across "
        f"{len(by_fw)} frameworks, grouped the way Apple groups them, each "
        "with its one-line description.",
        "",
        "`api-map.md` goes HIG concept → symbol, but only where an Apple page "
        "linked one. This goes the other way, and covers the whole surface: "
        "**does a system component for this already exist, and what is it "
        "called?**",
        "",
        "That question is the one worth asking before writing a custom "
        "control. A hand-rolled modal is worth flagging in review only if you "
        "can name what it should have been — `UISheetPresentationController`, "
        "`.sheet(item:onDismiss:content:)`, `NSPanel` — and this is where "
        "those names are.",
        "",
        "Scraped at category depth: symbol names and abstracts, not method "
        "signatures. Grep it.",
        "",
        "---",
        "",
    ]
    for fw in sorted(by_fw):
        cats = by_fw[fw]
        n = sum(len(v) for v in cats.values())
        out += [f"## {fw}", f"<sub>{n} symbols</sub>", ""]
        for cat in sorted(cats):
            out.append(f"### {cat}")
            out.append("")
            for r in sorted(cats[cat], key=lambda x: x["symbol"]):
                desc = f" — {r['abstract']}" if r["abstract"] else ""
                out.append(f"- [`{r['symbol']}`]({r['url']}){desc}")
            out.append("")
    return "\n".join(out).rstrip() + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", nargs="*", help="swiftui uikit appkit")
    args = ap.parse_args()

    want = {k: v for k, v in FRAMEWORKS.items()
            if not args.only or k in args.only}

    rows = []
    for slug, name in want.items():
        got = walk_framework(slug, name)
        print(f"  {name:8} {len(got):5} symbols")
        rows.extend(got)

    if not rows:
        sys.exit("nothing scraped")

    os.makedirs(REFS, exist_ok=True)
    md = os.path.join(REFS, "framework-index.md")
    open(md, "w", encoding="utf-8").write(write_index(rows))
    js = os.path.join(REFS, "framework-index.json")
    json.dump(rows, open(js, "w", encoding="utf-8"), indent=1)

    print(f"\nframework-index.md  {len(rows)} symbols, "
          f"{os.path.getsize(md)//1024} KB")
    return 0


if __name__ == "__main__":
    sys.exit(main())
