#!/usr/bin/env python3
# Build guide HTML from bros24-bot jsons. Run: python3 build_guides_from_bot.py
from __future__ import annotations
import json
import re
import os
from pathlib import Path
from datetime import datetime

WOSC_ROOT = Path(__file__).resolve().parent
BOT_JSONS = (WOSC_ROOT / ".." / "bros24-bot" / "jsons").resolve()
if os.environ.get("BOT_JSONS"):
    BOT_JSONS = Path(os.environ["BOT_JSONS"])
OUT_GUIDES = WOSC_ROOT / "guides"
BASE_URL = "https://www.whiteoutsurvival-community.com"
DISCORD_INVITE = "https://discord.gg/wos-community"
LANG = "en"

GEN_HEROES = {
    2: ["alonso", "flint", "philly"],
    3: ["greg", "logan", "mia"],
    4: ["ahmose", "reina", "lynn"],
    5: ["hector", "norah", "gwen"],
    6: ["wu_ming", "renee", "wayne"],
    7: ["bradley", "edith", "gordon"],
    8: ["gatot", "sonya", "hendrik"],
    9: ["xura", "fred", "magnus"],
    10: ["blanchette", "freya", "gregory"],
    11: ["rufus", "lloyd", "eleonora"],
    12: ["ligeia", "karol", "hervor"],
    13: ["gisela", "flora", "vulcanus"],
    14: ["elif", "dominic", "cara"],
}

def _load_json(path):
    if not path.exists():
        return None
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None

def _md_html(text):
    if not text or not isinstance(text, str):
        return ""
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    s = re.sub(r"_(.+?)_", r"<em>\1</em>", s)
    lines = s.split("\n")
    out = []
    for line in lines:
        line = line.strip()
        if not line:
            if out and not out[-1].endswith("</p>"):
                out.append("</p>")
            continue
        if out and not out[-1].endswith("</p>"):
            out.append("<br/>\n")
        out.append("<p>" + line)
    if out and not out[-1].endswith("</p>"):
        out.append("</p>")
    return "\n".join(out) if out else ""

def _slug_title(slug):
    return slug.replace("_", " ").title()

def _esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

def _head(title, desc, path):
    url = BASE_URL.rstrip("/") + "/" + path.lstrip("/")
    return (
        '  <meta charset="utf-8"/><meta name="viewport" content="width=device-width, initial-scale=1"/>'
        f'<title>{_esc(title)}</title><meta name="description" content="{_esc(desc)}"/>'
        f'<link rel="canonical" href="{_esc(url)}"/><meta name="robots" content="index,follow"/>'
        '<link rel="icon" href="/assets/logo.png"/>'
    )

def _wrap(title, desc, path, body, extra=""):
    nav = f'<nav class="nav"><a class="pill" href="/">Home</a><a class="pill" href="/guides/heroes/">Heroes</a><a class="pill cta" href="{DISCORD_INVITE}" target="_blank" rel="noopener">Join Discord</a>{extra}</nav>'
    css = "body{background:#050810;color:#eaf2ff;font-family:system-ui,sans-serif;line-height:1.6;margin:0;padding:1.5rem;}.wrap{max-width:1180px;margin:0 auto;}.nav{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:1.5rem;}.pill{padding:10px 14px;border-radius:999px;border:1px solid rgba(255,255,255,.08);background:rgba(255,255,255,.06);font-weight:700;font-size:13px;color:inherit;text-decoration:none;}.pill.cta{border-color:rgba(125,211,252,.95);background:linear-gradient(135deg,rgba(125,211,252,.45),rgba(96,165,250,.25));}article{background:rgba(12,18,32,.72);border:1px solid rgba(255,255,255,.08);border-radius:18px;padding:1.5rem;}article h1{color:#7dd3fc;}article strong{color:#60a5fa;}.hero-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:12px;margin:1rem 0;}.hero-grid a{color:#7dd3fc;text-decoration:none;padding:8px 12px;border-radius:8px;background:rgba(255,255,255,.05);}"
    return f'<!doctype html><html lang="en"><head>{_head(title, desc, path)}<style>{css}</style></head><body><div class="wrap"><header style="display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:1rem;"><a href="/" style="color:#7dd3fc;font-weight:800;text-decoration:none;">WOSC</a>{nav}</header>{body}</div></body></html>'

def _cta():
    return f'<section style="margin-top:2rem;padding:1.5rem;border-radius:18px;background:rgba(12,18,32,.72);text-align:center;"><p style="margin:0 0 .75rem;">More guides on Discord.</p><a class="pill cta" href="{DISCORD_INVITE}" target="_blank" rel="noopener">Join WOSC Discord</a></section>'

def main():
    if not BOT_JSONS.exists():
        print("BOT_JSONS not found:", BOT_JSONS)
        return
    urls = []
    (OUT_GUIDES / "heroes").mkdir(parents=True, exist_ok=True)
    (OUT_GUIDES / "experts").mkdir(parents=True, exist_ok=True)

    # Heroes index
    out = []
    for gen in sorted(GEN_HEROES.keys()):
        out.append(f"<h2>Generation {gen}</h2><div class=\"hero-grid\">")
        for slug in GEN_HEROES[gen]:
            if (BOT_JSONS / f"{slug}.json").exists():
                out.append(f'<a href="/guides/heroes/{slug}.html">{_slug_title(slug)}</a>')
                urls.append(f"/guides/heroes/{slug}.html")
            else:
                out.append(f'<span style="color:#aab8d6">{_slug_title(slug)}</span>')
        out.append("</div>")
        if (BOT_JSONS / f"gen{gen}_summary.json").exists():
            out.append(f'<p><a href="/guides/heroes/gen-{gen}.html">Gen {gen} summary</a></p>')
            urls.append(f"/guides/heroes/gen-{gen}.html")
    body = "<article><h1>Whiteout Survival Heroes Gen 2–14</h1><p>Guides and meta. Join Discord for more.</p>" + "".join(out) + _cta() + "</article>"
    (OUT_GUIDES / "heroes" / "index.html").write_text(_wrap("Heroes Guide Gen 2–14 | WOSC", "Whiteout Survival hero guides Gen 2 to 14. Join WOSC Discord.", "guides/heroes/", body, '<a class="pill" href="/guides/experts/">Experts</a><a class="pill" href="/guides/alliance-mobilization.html">AM</a>'), encoding="utf-8")
    print("Wrote guides/heroes/index.html")

    # Gen summary + hero pages
    for gen in sorted(GEN_HEROES.keys()):
        p = BOT_JSONS / f"gen{gen}_summary.json"
        if p.exists():
            d = _load_json(p)
            if d and LANG in d:
                body = f"<article><h1>Gen {gen} Meta</h1><div class=\"content\">{_md_html(d[LANG])}</div><p><a href=\"/guides/heroes/\">All heroes</a></p>{_cta()}</article>"
                (OUT_GUIDES / "heroes" / f"gen-{gen}.html").write_text(_wrap(f"Gen {gen} Meta | WOSC", f"Gen {gen} hero meta. Join WOSC Discord.", f"guides/heroes/gen-{gen}.html", body), encoding="utf-8")
    for gen, slugs in GEN_HEROES.items():
        for slug in slugs:
            p = BOT_JSONS / f"{slug}.json"
            if p.exists():
                d = _load_json(p)
                if d and LANG in d:
                    name = _slug_title(slug)
                    body = f"<article><h1>{name} (Gen {gen})</h1><p><a href=\"/guides/heroes/gen-{gen}.html\">Gen {gen}</a> · <a href=\"/guides/heroes/\">All</a></p><div class=\"content\">{_md_html(d[LANG])}</div>{_cta()}</article>"
                    desc = re.sub(r"\*\*", "", d[LANG][:150]) + "…"
                    (OUT_GUIDES / "heroes" / f"{slug}.html").write_text(_wrap(f"{name} Gen {gen} | WOSC", desc, f"guides/heroes/{slug}.html", body), encoding="utf-8")
                    if f"/guides/heroes/{slug}.html" not in urls:
                        urls.append(f"/guides/heroes/{slug}.html")

    # Experts
    experts = [(p.stem.replace("expert_", ""), _slug_title(p.stem.replace("expert_", ""))) for p in sorted(BOT_JSONS.glob("expert_*.json")) if p.name not in ("expert_intro.json", "expert_summary.json")]
    out = ["<div class=\"hero-grid\">"] + [f'<a href="/guides/experts/{s}.html">{t}</a>' for s, t in experts] + ["</div>"]
    body = "<article><h1>Experts Guide</h1><p>F2P vs P4W, affinity. Join Discord.</p>" + "".join(out) + _cta() + "</article>"
    (OUT_GUIDES / "experts" / "index.html").write_text(_wrap("Experts Guide | WOSC", "Whiteout Survival Experts. Join WOSC Discord.", "guides/experts/", body, '<a class="pill" href="/guides/heroes/">Heroes</a><a class="pill" href="/guides/alliance-mobilization.html">AM</a>'), encoding="utf-8")
    for slug, title in experts:
        urls.append(f"/guides/experts/{slug}.html")
        p = BOT_JSONS / f"expert_{slug}.json"
        d = _load_json(p)
        if d and LANG in d:
            body = f"<article><h1>{title}</h1><p><a href=\"/guides/experts/\">All experts</a></p><div class=\"content\">{_md_html(d[LANG])}</div>{_cta()}</article>"
            (OUT_GUIDES / "experts" / f"{slug}.html").write_text(_wrap(f"{title} Expert | WOSC", d[LANG][:150].replace("\n", " ") + "…", f"guides/experts/{slug}.html", body), encoding="utf-8")

    # AM guide
    p = BOT_JSONS / "am_guide.json"
    if p.exists():
        d = _load_json(p)
        if d and LANG in d:
            body = f"<article><h1>Alliance Mobilization (AM)</h1><div class=\"content\">{_md_html(d[LANG])}</div>{_cta()}</article>"
            (OUT_GUIDES / "alliance-mobilization.html").write_text(_wrap("Alliance Mobilization Guide | WOSC", "AM guide: SvS-safe priorities. Join WOSC Discord.", "guides/alliance-mobilization.html", body, '<a class="pill" href="/guides/heroes/">Heroes</a><a class="pill" href="/guides/experts/">Experts</a>'), encoding="utf-8")
            urls.append("/guides/alliance-mobilization.html")

    # Sitemap
    today = datetime.utcnow().strftime("%Y-%m-%d")
    new = "".join(f"<url><loc>{BASE_URL}{u}</loc><lastmod>{today}</lastmod></url>\n" for u in sorted(set(urls)))
    sp = WOSC_ROOT / "sitemap.xml"
    if sp.exists() and "guides/heroes" not in sp.read_text(encoding="utf-8"):
        c = sp.read_text(encoding="utf-8").replace("</urlset>", new + "</urlset>")
        sp.write_text(c, encoding="utf-8")
        print("Updated sitemap.xml")
    print("Done.", len(urls), "URLs")

if __name__ == "__main__":
    main()
