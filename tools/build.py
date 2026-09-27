#!/usr/bin/env python3
"""build.py — docs/index.html (English) and docs/th/index.html (Thai) from content.py + data/.

    python3 tools/build.py                                   # GitHub Pages copy, relative refs
    SITE_URL=https://motdang.net/sites/ship-to-thailand \
      OUT=../mot-dang/assets/sites/ship-to-thailand python3 tools/build.py   # Mot Dang copy

On motdang.net a folder answers without its trailing slash, so under SITE_URL every file
reference is root-relative (the URL's path); the Pages build stays relative.
"""
from __future__ import annotations

import json
import os
import shutil
import sys
from html import escape
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from content import RATES, READ, T  # noqa: E402

CANON = "https://motdang.net/sites/ship-to-thailand/"
PAGES = "https://nanobotco.github.io/ship-to-thailand/"
URL = os.environ.get("SITE_URL", "").rstrip("/") + "/" if os.environ.get("SITE_URL") else PAGES
MOUNT = urlparse(URL).path if os.environ.get("SITE_URL") else ""
OUT = Path(os.environ["OUT"]).resolve() if os.environ.get("OUT") else ROOT / "docs"
MOTDANG = "https://motdang.net/"
EXPLAINER = "https://nanobotco.github.io/indras-net/"

NET = json.loads((ROOT / "data" / "net.json").read_text(encoding="utf-8"))
HREF = json.loads((ROOT / "data" / "hrefs.json").read_text(encoding="utf-8"))

# jewels drawn in the hero: US points on the right, Thailand on the left, x/y in 0..1
PORTS = {
    "en": {"cm": "Chiang Mai", "lcb": "Laem Chabang", "sea": "Seattle", "or": "Oregon", "sf": "San Francisco",
           "la": "Los Angeles", "sd": "San Diego", "lv": "Las Vegas", "hi": "Hawaii"},
    "th": {"cm": "เชียงใหม่", "lcb": "แหลมฉบัง", "sea": "ซีแอตเทิล", "or": "ออริกอน", "sf": "ซานฟรานซิสโก",
           "la": "ลอสแอนเจลิส", "sd": "ซานดิเอโก", "lv": "ลาสเวกัส", "hi": "ฮาวาย"},
}

FONTS = [("Prompt", 600, "prompt-600"), ("Sarabun", 400, "sarabun-400"), ("Sarabun", 600, "sarabun-600")]
THAI_RANGE = "U+02D7,U+0303,U+0331,U+0E01-0E5B,U+200C-200D,U+25CC"
LATIN_RANGE = ("U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,"
               "U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD,U+0E3F")

CSS = """
:root{--sea:#0b1d30;--sea2:#123452;--gold:#e8b04a;--gold2:#ffd98a;--paper:#f8f3e8;--card:#fffdf8;
--ink:#1c2632;--muted:#5b6673;--line:#e3d9c4;--red:#c0392b;--best:#1f7a4d}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--paper);color:var(--ink);font:400 1.06rem/1.65 Sarabun,system-ui,sans-serif}
a{color:#1d5f8a;text-underline-offset:.15em}
b{font-weight:600}
h1,h2,h3{font-family:Prompt,Sarabun,system-ui,sans-serif;font-weight:600;line-height:1.25}
.wrap{max-width:46rem;margin:0 auto;padding:0 16px}
.hero{position:relative;background:radial-gradient(120% 90% at 30% 20%,var(--sea2),var(--sea) 70%);color:#f6ecd6;overflow:hidden}
#net{display:block;width:100%;height:min(70vh,560px);min-height:420px;cursor:pointer;touch-action:manipulation}
.hero-in{position:absolute;left:0;right:0;bottom:0;padding:0 16px 1.4rem;pointer-events:none;
 background:linear-gradient(transparent,rgba(8,20,34,.85) 55%)}
.hero-in .wrap{padding:0}
.kicker{margin:0;color:var(--gold2);font-size:.9rem;letter-spacing:.02em}
.hero h1{margin:.1rem 0 .4rem;font-size:clamp(2rem,6.5vw,3.3rem);color:#fff6e0}
.lede{margin:0;font-size:1.12rem;max-width:36rem}
.lede b{color:var(--gold2)}
.hint{margin:.5rem 0 0;font-size:.85rem;color:#c9d6e3}
.lang{position:absolute;top:12px;right:16px;z-index:2;color:#fff;background:rgba(255,255,255,.12);
 border:1px solid rgba(255,255,255,.35);border-radius:99px;padding:.2rem .8rem;font-size:.9rem;text-decoration:none}
nav.jump{display:flex;flex-wrap:wrap;gap:.4rem;padding:.9rem 0 0;margin:0}
nav.jump a{background:var(--card);border:1px solid var(--line);border-radius:99px;padding:.15rem .75rem;
 text-decoration:none;color:var(--ink);font-size:.95rem}
section{padding:1.2rem 0 .4rem}
h2{font-size:1.5rem;margin:.6rem 0 .6rem;display:flex;align-items:center;gap:.55rem}
h2::before{content:"";width:.8rem;height:.8rem;border-radius:50%;flex:none;
 background:radial-gradient(circle at 35% 35%,#fff7dd,var(--gold) 45%,#9c6a12);box-shadow:0 0 0 3px rgba(232,176,74,.25)}
h3{font-size:1.1rem;margin:1.1rem 0 .4rem}
.tbl{width:100%;border-collapse:collapse;background:var(--card);border:1px solid var(--line);border-radius:.6rem;overflow:hidden}
.tbl th,.tbl td{text-align:left;vertical-align:top;padding:.55rem .6rem;border-bottom:1px solid var(--line)}
.tbl th{font-family:Prompt,Sarabun,sans-serif;font-weight:600;font-size:.85rem;color:var(--muted);background:#f3ecdc}
.tbl td.code{font-family:ui-monospace,Menlo,monospace;font-size:.9rem;color:var(--muted);white-space:nowrap}
.tbl td.price{white-space:nowrap;font-weight:600}
.tbl .what{display:block;font-weight:600}
.tbl .why{display:block;color:var(--muted);font-size:.95rem}
.note{color:var(--muted);font-size:.92rem}
.two{list-style:none;padding:0;margin:0;display:grid;gap:.6rem}
.two li{background:var(--card);border:1px solid var(--line);border-left:4px solid var(--gold);border-radius:.5rem;padding:.6rem .8rem}
.calc{background:var(--card);border:1px solid var(--line);border-radius:.8rem;padding:1rem}
.calc label{display:block;font-weight:600;margin:.3rem 0 .2rem}
.calc input[type=number]{width:100%;max-width:12rem;font:inherit;padding:.45rem .6rem;border:1px solid #cbbd9f;border-radius:.4rem;background:#fff}
.calc .help{display:block;color:var(--muted);font-size:.9rem;font-weight:400}
.calc .chk{display:flex;gap:.5rem;align-items:flex-start;font-weight:400;margin-top:.8rem}
.calc .chk input{margin-top:.35rem}
.boxrow{display:flex;flex-wrap:wrap;gap:3px;margin:.6rem 0;min-height:14px}
.boxrow i{width:12px;height:12px;background:#c89b5a;border:1px solid #8a6331;border-radius:2px}
.boxrow i.f{background:#8fa7b8;border-color:#4d6577}
.total{font-size:1.05rem;margin:.3rem 0 .6rem}
.routes{list-style:none;padding:0;margin:0;display:grid;gap:.45rem}
.routes li{display:flex;justify-content:space-between;gap:.8rem;align-items:baseline;padding:.5rem .7rem;border:1px solid var(--line);border-radius:.5rem;background:#fff}
.routes li .sub{display:block;color:var(--muted);font-size:.88rem}
.routes li .amt{font-weight:600;white-space:nowrap;font-size:1.1rem}
.routes li.best{border:2px solid var(--best);background:#eef8f1}
.routes li.best .tag{color:var(--best);font-weight:600;font-size:.85rem;display:block;text-align:right}
.routes li.off{opacity:.55}
ol.steps{list-style:none;padding:0;margin:0;counter-reset:s;display:grid;gap:.55rem}
ol.steps li{counter-increment:s;position:relative;padding:.1rem 0 .1rem 2.6rem}
ol.steps li::before{content:counter(s);position:absolute;left:0;top:.05rem;width:1.9rem;height:1.9rem;border-radius:50%;
 display:grid;place-items:center;font:600 .95rem Prompt,sans-serif;color:var(--sea);
 background:radial-gradient(circle at 35% 35%,#fff7dd,var(--gold) 55%,#b47f22)}
ol.steps b{display:block}
ul.plain{padding-left:1.1rem;margin:.3rem 0}
.net{background:var(--card);border:2px solid var(--red);border-radius:.8rem;box-shadow:3px 3px 0 #f1c40f;padding:.8rem .9rem}
.net details{border-top:1px dashed var(--line);padding:.35rem 0}
.net details:first-of-type{border-top:0}
.net summary{cursor:pointer;font-weight:600;padding:.2rem 0}
.net summary .roman{font-style:italic;font-weight:400;color:var(--muted);font-size:.85rem}
.net summary .n{color:var(--muted);font-weight:400;font-size:.9rem}
.net ul{list-style:none;padding:0;margin:.2rem 0 .4rem}
.net li{padding:.3rem 0;line-height:1.45}
.net li .why{display:block;font-size:.92rem;color:var(--muted)}
dl.contact{display:grid;grid-template-columns:max-content 1fr;gap:.25rem 1rem;margin:.4rem 0}
dl.contact dt{font-weight:600}
dl.contact dd{margin:0}
.src{font-size:.92rem}
footer{margin:2rem 0 0;padding:1.2rem 0 2rem;border-top:1px solid var(--line);color:var(--muted);font-size:.92rem}
.nw{white-space:nowrap}
@media (max-width:599px){#net{height:300px;min-height:0}.hero-in{position:relative;background:none;padding-top:.4rem}
.tbl td.code{display:none}.tbl th.code{display:none}}
@media (prefers-reduced-motion:reduce){*{scroll-behavior:auto}}
"""


def font_css(pre: str) -> str:
    out = []
    for fam, w, stem in FONTS:
        for script, rng in (("thai", THAI_RANGE), ("latin", LATIN_RANGE)):
            out.append(f"@font-face{{font-family:'{fam}';font-style:normal;font-weight:{w};font-display:swap;"
                       f"src:url({pre}assets/fonts/{stem}-{script}.woff2) format('woff2');unicode-range:{rng}}}")
    return "".join(out)


def th_hold(s: str, lang: str) -> str:
    """Thai phrases held together so a line breaks between phrases, never inside a word."""
    if lang != "th" or "<" in s:
        return s
    return " ".join(f'<span class="nw">{w}</span>' if len(w) <= 29 else w for w in s.split(" "))


def net_html(lang: str) -> str:
    parts = []
    for i, st in enumerate(NET["strands"]):
        lis = []
        for j in st["jewels"]:
            href = MOTDANG + HREF[j["id"]]
            lis.append(f'<li><a href="{href}">{escape(j["name"])}</a><span class="why">{escape(j[lang])}</span></li>')
        roman = f' <span class="roman">{escape(st["roman"])}</span>' if lang == "th" else ""
        label = st[lang] if lang == "en" else st["th"]
        parts.append(f'<details{" open" if i == 0 else ""}><summary>{escape(label)}{roman} '
                     f'<span class="n">· {len(st["jewels"])}</span></summary><ul>{"".join(lis)}</ul></details>')
    return "".join(parts)


def page(lang: str) -> str:
    t = T[lang]
    other = "th" if lang == "en" else "en"
    depth = "" if lang == "en" else "../"
    pre = MOUNT if MOUNT else depth                       # asset prefix
    home = {"en": (MOUNT or depth) + ("" if MOUNT else "index.html"),
            "th": (MOUNT + "th/") if MOUNT else (depth + "th/index.html" if lang == "en" else "index.html")}
    if not MOUNT:
        home = {"en": "index.html" if lang == "en" else "../index.html",
                "th": "th/index.html" if lang == "en" else "index.html"}
    canon = CANON + ("" if lang == "en" else "th/")
    card = CANON + "card.jpg"
    title = f'{t["title"]} · Send2Thai · Mot Dang'

    rows = "".join(
        f'<tr><td class="code">{c}</td><td><span class="what">{escape(t["rate_rows"][c][0])}</span>'
        f'<span class="why">{th_hold(t["rate_rows"][c][1], lang)}</span></td><td class="price">{p[lang]}</td></tr>'
        for c, p in RATES)
    two = "".join(f"<li>{x[0]}</li>" for x in t["two"])
    steps = "".join(f"<li><b>{escape(a)}</b>{th_hold(escape(b), lang)}</li>" for a, b in t["steps"])
    pickup = "".join(f"<li>{th_hold(escape(x), lang)}</li>" for x in t["pickup"])
    cover = "".join(f"<li>{th_hold(escape(x), lang)}</li>" for x in t["cover"])
    ltc = "".join(f"<p>{x}</p>" for x in t["ltc"])
    customs = "".join(f"<p>{x}</p>" for x in t["customs"])
    contact = "".join(f"<dt>{escape(a)}</dt><dd>{b}</dd>" for a, b in t["contact_rows"])
    branches = "".join(
        f"<tr><td><b>{escape(a)}</b></td><td>{escape(b)}</td><td class=\"price\">"
        + (f'<a href="tel:{c.replace(" ", "").replace("-", "")}">{c}</a>' if c else "") + "</td></tr>"
        for a, b, c in t["branches"])
    src = "".join(f'<li><a href="{u}">{escape(l)}</a></li>' for u, l in t["src"])
    jump = "".join(f'<a href="{h}">{escape(l)}</a>' for h, l in t["jump"])

    ld = {
        "@context": "https://schema.org", "@type": "Article", "headline": t["title"], "inLanguage": lang,
        "description": t["desc"], "url": canon, "image": card, "dateModified": "2026-09-27",
        "author": {"@type": "Person", "name": "NaN", "url": "https://hongdam.net/"},
        "publisher": {"@type": "Organization", "name": "Mot Dang", "url": MOTDANG},
        "isPartOf": {"@type": "WebSite", "name": "Mot Dang", "url": MOTDANG},
        "about": {"@type": "Organization", "name": "Send2Thai", "url": "https://send2thai.com/",
                  "telephone": "+1-323-336-9595", "email": "info@send2thai.com"},
    }
    cfg = {"lang": lang, "ports": PORTS[lang], "t": {k: t[k] for k in (
        "c_total", "c_cuft", "c_routes", "c_pallets", "c_min", "c_over", "c_noallow", "c_best", "hours_now")}}

    ld_json = json.dumps(ld, ensure_ascii=False).replace("</", "<\\/")
    cfg_json = json.dumps(cfg, ensure_ascii=False).replace("</", "<\\/")
    return f"""<!doctype html>
<html lang="{lang}" translate="no" class="notranslate">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="google" content="notranslate">
<meta name="robots" content="notranslate">
<title>{escape(title)}</title>
<meta name="description" content="{escape(t['desc'])}">
<link rel="canonical" href="{canon}">
<link rel="alternate" hreflang="en" href="{CANON}">
<link rel="alternate" hreflang="th" href="{CANON}th/">
<meta property="og:type" content="article">
<meta property="og:title" content="{escape(t['title'])}">
<meta property="og:description" content="{escape(t['desc'])}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{card}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="{'en_US' if lang == 'en' else 'th_TH'}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{card}">
<meta name="theme-color" content="#0b1d30">
<link rel="icon" href="{pre}assets/icon.svg" type="image/svg+xml">
<style>{font_css(pre)}{CSS}</style>
<script type="application/ld+json">{ld_json}</script>
</head>
<body>
<header class="hero">
<a class="lang" href="{home[other]}" hreflang="{other}" lang="{other}">{t['other']}</a>
<canvas id="net" role="img" aria-label="{escape(t['hint'])}"></canvas>
<div class="hero-in"><div class="wrap">
<p class="kicker">{escape(t['kicker'])}</p>
<h1>{escape(t['h1'])}</h1>
<p class="lede">{t['lede']}</p>
<p class="hint">{escape(t['hint'])}</p>
</div></div>
</header>
<main class="wrap">
<nav class="jump" aria-label="sections">{jump}</nav>

<section id="ltc"><h2>{escape(t['ltc_h'])}</h2>{ltc}</section>

<section id="prices"><h2>{escape(t['prices_h'])}</h2>
<table class="tbl"><thead><tr><th class="code">{t['th_code']}</th><th>{t['th_what']}</th><th>{t['th_price']}</th></tr></thead>
<tbody>{rows}</tbody></table>
<p class="note">{escape(t['prices_note'].format(read=READ[lang]))}</p>
<h3>{escape(t['two_h'])}</h3><ul class="two">{two}</ul>
</section>

<section id="cost"><h2>{escape(t['cost_h'])}</h2>
<p>{escape(t['cost_intro'])}</p>
<form class="calc" onsubmit="return false">
<label for="boxes">{escape(t['f_boxes'])}</label>
<input id="boxes" type="number" min="0" max="2000" step="1" value="40" inputmode="numeric">
<label for="cuft">{escape(t['f_cuft'])}<span class="help">{escape(t['f_cuft_help'])}</span></label>
<input id="cuft" type="number" min="0" max="5000" step="5" value="0" inputmode="numeric">
<label class="chk"><input id="allow" type="checkbox"> <span>{escape(t['f_allow'])}</span></label>
<div class="boxrow" id="boxrow" aria-hidden="true"></div>
<p class="total" id="total" aria-live="polite"></p>
<ul class="routes" id="routes" aria-live="polite"></ul>
<p class="note">{t['c_note']}</p>
</form>
</section>

<section id="steps"><h2>{escape(t['steps_h'])}</h2>
<ol class="steps">{steps}</ol>
<h3>{escape(t['pickup_h'])}</h3><ul class="plain">{pickup}</ul>
</section>

<section id="cover"><h2>{escape(t['cover_h'])}</h2><ul class="plain">{cover}</ul></section>

<section id="customs"><h2>{escape(t['customs_h'])}</h2>{customs}</section>

<section id="chiang-mai"><h2>{escape(t['cm_h'])}</h2>
<p>{escape(t['cm_lede'])} <a href="{EXPLAINER}">{escape(t['cm_more'])}</a></p>
<div class="net">{net_html(lang)}</div>
<p class="note">{escape(t['cm_disclose'])}</p>
</section>

<section id="contact"><h2>{escape(t['contact_h'])} · Send2Thai</h2>
<dl class="contact">{contact}</dl>
<p class="note">{escape(t['hours'])} <span id="hours"></span></p>
<h3>{escape(t['branches_h'])}</h3>
<table class="tbl"><tbody>{branches}</tbody></table>
</section>

<section id="sources"><h2>{escape(t['src_h'])}</h2>
<ul class="plain src">{src}</ul>
<p class="note">{escape(t['src_read'].format(read=READ[lang]))}</p>
</section>
</main>
<footer><div class="wrap">{t['foot']} · <a href="{home[other]}" lang="{other}">{t['other']}</a> ·
<a href="https://github.com/NaNoBotCo/ship-to-thailand">GitHub</a> · CC BY 4.0</div></footer>
<script id="cfg" type="application/json">{cfg_json}</script>
<script src="{pre}assets/site.js" defer></script>
</body>
</html>
"""


ICON = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#0b1d30"/>'
        '<g stroke="#e8b04a" stroke-width="2" opacity=".8"><path d="M12 20h40M12 44h40M20 12v40M44 12v40"/></g>'
        '<g fill="#ffd98a"><circle cx="20" cy="20" r="5"/><circle cx="44" cy="20" r="5"/><circle cx="20" cy="44" r="5"/>'
        '<circle cx="44" cy="44" r="5"/></g><circle cx="32" cy="32" r="8" fill="#c0392b"/></svg>')


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "th").mkdir(exist_ok=True)
    (OUT / "index.html").write_text(page("en"), encoding="utf-8")
    (OUT / "th" / "index.html").write_text(page("th"), encoding="utf-8")
    assets = OUT / "assets"
    assets.mkdir(exist_ok=True)
    shutil.copy(ROOT / "tools" / "site.js", assets / "site.js")
    (assets / "icon.svg").write_text(ICON, encoding="utf-8")
    if OUT != ROOT / "docs":
        shutil.copytree(ROOT / "docs" / "assets" / "fonts", assets / "fonts", dirs_exist_ok=True)
        if (ROOT / "docs" / "card.jpg").exists():
            shutil.copy(ROOT / "docs" / "card.jpg", OUT / "card.jpg")
    else:
        (OUT / "_headers").write_text("/*\n  X-Robots-Tag: notranslate\n", encoding="utf-8")
        (OUT / ".nojekyll").write_text("", encoding="utf-8")
    print("built", OUT, "mount", MOUNT or "(relative)")


if __name__ == "__main__":
    main()
