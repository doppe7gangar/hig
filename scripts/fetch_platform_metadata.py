#!/usr/bin/env python3
"""Fetch each HIG page's `supported-platforms` metadata from Apple's DocC API.

The page Markdown doesn't carry this, but the JSON does — it's Apple's own
authoritative statement of which platforms a page applies to, which beats
inferring it from prose. Used by build_platform_skills.py to decide which
pages belong in a per-platform skill.

Writes scripts/platform_metadata.json.
"""

import json
import os
import sys
import time
import urllib.error
import urllib.request

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(REPO, "content")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "platform_metadata.json")
DATA_BASE = "https://developer.apple.com/tutorials/data/design/human-interface-guidelines"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

# Pages that aren't part of the DocC HIG tree (scraped from plain HTML instead).
NON_DOCC = {"design", "resources", "icon-composer", "sf-symbols-app",
            "pass-designer", "reality-composer-pro"}


def fetch(slug):
    url = f"{DATA_BASE}/{slug}.json" if slug != "human-interface-guidelines" else \
          "https://developer.apple.com/tutorials/data/design/human-interface-guidelines.json"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code in (404, 410):
                return None
            time.sleep(2 * (attempt + 1))
        except Exception:
            time.sleep(2 * (attempt + 1))
    return None


if __name__ == "__main__":
    slugs = sorted(f[:-3] for f in os.listdir(CONTENT) if f.endswith(".md"))
    out, missing = {}, []
    for i, slug in enumerate(slugs, 1):
        if slug in NON_DOCC:
            continue
        data = fetch(slug)
        if not data:
            missing.append(slug)
            continue
        cm = data.get("metadata", {}).get("customMetadata", {}) or {}
        sp = cm.get("supported-platforms")
        if sp:
            out[slug] = [p.strip() for p in sp.split(",") if p.strip()]
        else:
            missing.append(slug)
        if i % 40 == 0:
            print(f"  {i}/{len(slugs)}", file=sys.stderr)

    json.dump(out, open(OUT, "w"), indent=1, sort_keys=True)
    print(f"wrote {len(out)} pages with supported-platforms -> {os.path.relpath(OUT, REPO)}",
          file=sys.stderr)
    if missing:
        print(f"{len(missing)} without the field (treated as all-platforms): "
              f"{', '.join(missing[:12])}{' ...' if len(missing) > 12 else ''}", file=sys.stderr)
