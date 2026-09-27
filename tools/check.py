#!/usr/bin/env python3
"""check.py — gates on docs/ before anything ships. Exit 1 on any failure.

    python3 tools/check.py
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
STYLECHECK = Path.home() / ".claude" / "bin" / "stylecheck.py"


def main() -> int:
    errs: list[str] = []
    net = json.loads((ROOT / "data" / "net.json").read_text(encoding="utf-8"))
    hrefs = json.loads((ROOT / "data" / "hrefs.json").read_text(encoding="utf-8"))
    ids = [j["id"] for s in net["strands"] for j in s["jewels"]]
    errs += [f"net: no motdang path for {i}" for i in ids if i not in hrefs]
    if len(ids) != len(set(ids)):
        errs.append("net: a jewel appears twice")

    for rel in ("index.html", "th/index.html"):
        html = (DOCS / rel).read_text(encoding="utf-8")
        for m in re.finditer(r'<(script|img|link)\b[^>]*\b(src|href)="([^"]+)"', html):
            tag, _, url = m.groups()
            if tag == "link" and re.search(r'rel="(canonical|alternate)"', m.group(0)):
                continue
            if re.match(r"https?://", url):
                errs.append(f"{rel}: outside request <{tag}> {url}")
        for needle in ('translate="no"', 'class="notranslate"', 'name="google" content="notranslate"'):
            if needle not in html:
                errs.append(f"{rel}: notranslate missing {needle}")
        for k in ("og:image", "og:image:width", "twitter:card", "twitter:image"):
            if f'"{k}"' not in html:
                errs.append(f"{rel}: share meta missing {k}")
        ld = re.search(r'<script type="application/ld\+json">(.*?)</script>', html, re.S)
        try:
            json.loads(ld.group(1).replace("<\\/", "</"))
        except Exception as e:  # noqa: BLE001
            errs.append(f"{rel}: JSON-LD {e}")
        shown = html.count('<li><a href="https://motdang.net/')
        if shown != len(ids):
            errs.append(f"{rel}: net shows {shown} of {len(ids)} jewels")
        for src in re.findall(r'(?:src|href)="((?:\.\./)?assets/[^"]+)"', html) + re.findall(r"url\(((?:\.\./)?assets/[^)]+)\)", html):
            if not (DOCS / Path(rel).parent / src).resolve().exists():
                errs.append(f"{rel}: missing file {src}")

    from PIL import Image
    if Image.open(DOCS / "card.jpg").size != (1200, 630):
        errs.append("share card is not 1200×630")

    r = subprocess.run([sys.executable, str(STYLECHECK), str(DOCS / "index.html"), str(DOCS / "th" / "index.html"),
                        str(ROOT / "tools" / "content.py"), str(ROOT / "README.txt")], capture_output=True, text=True)
    if r.returncode != 0:
        errs.append("stylecheck:\n" + r.stdout + r.stderr)

    for e in errs:
        print("FAIL", e)
    print("check:", "red" if errs else "green", f"({len(ids)} jewels)")
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())
