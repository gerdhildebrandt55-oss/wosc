# Generiert kompendium/building/fire-crystal-furnace.html aus der Canva-Quelltabelle.
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = Path(r"c:\Users\Norman\Desktop\website wosc\fire-crystal-furnace-canva-table.html")
OUT = ROOT / "kompendium" / "building" / "fire-crystal-furnace.html"
ASSET = "/assets/kompendium/fc-furnace"

text = SRC.read_text(encoding="utf-8")
m = re.search(r"<tbody>([\s\S]*)</tbody>", text)
if not m:
    raise SystemExit("no tbody")
tbody = m.group(1)
urls = sorted(set(re.findall(r'https://[^"\s]+\.png', tbody)))
for u in urls:
    fn = u.split("/")[-1]
    tbody = tbody.replace(u, f"{ASSET}/{fn}")


def img_repl(match):
    inner = match.group(1)
    if 'class="fc-ico"' in inner:
        return match.group(0)
    return f'<img class="fc-ico" draggable="false" {inner}>'


tbody = re.sub(r"<img\s+([^>]*?)>", img_repl, tbody)
tbody = tbody.replace('alt="" alt=""', 'alt=""')

TEMPLATE = """<!doctype html>
<html lang="de">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>Fire Crystal Furnace – Upgrade-Tabelle | WOSC Database</title>
  <meta name="description" content="Fire Crystal Furnace: Stufen, Kosten, Bauzeit, Macht. Rechner für Summen von Stufe zu Stufe. Community-Ressource."/>
  <link rel="canonical" href="https://www.whiteoutsurvival-community.com/kompendium/building/fire-crystal-furnace.html"/>
  <meta name="robots" content="index,follow"/>
  <link rel="icon" href="/assets/logo.png"/>
  <link rel="preconnect" href="https://fonts.googleapis.com"/>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap" rel="stylesheet"/>
  <style>
    :root{{
      --bg:#030712; --bg2:#0c1220; --text:#f1f5f9; --muted:#94a3b8;
      --line:rgba(148,163,184,.18); --accent:#22d3ee; --accent2:#0ea5e9;
      --card:rgba(15,23,42,.75); --r:16px; --max:1200px;
    }}
    *{{ box-sizing:border-box; }}
    html{{ scroll-behavior: smooth; }}
    body{{
      margin:0; min-height:100vh; font-family:"Plus Jakarta Sans",ui-sans-serif,system-ui,sans-serif;
      color:var(--text); background: var(--bg);
      background-image:
        radial-gradient(ellipse 900px 500px at 10% -10%, rgba(14,165,233,.12), transparent),
        radial-gradient(ellipse 700px 400px at 100% 0%, rgba(34,211,238,.08), transparent);
    }}
    a{{ color: var(--accent2); text-decoration: none; }}
    a:hover{{ text-decoration: underline; text-underline-offset: 3px; }}
    .wrap{{ max-width: var(--max); margin: 0 auto; padding: 1.5rem 1.1rem 2.5rem; }}
    .mast{{
      display:flex; flex-wrap:wrap; align-items:flex-end; justify-content:space-between; gap:1rem;
      padding-bottom: 1.25rem; margin-bottom: 1.5rem; border-bottom: 1px solid var(--line);
    }}
    .brand-block{{ display:flex; flex-direction:column; gap:4px; }}
    .brand{{ display:flex; align-items:center; gap:12px; }}
    .brand img{{ width:40px; height:40px; border-radius:12px; border:1px solid var(--line); }}
    .brand-title{{ font-weight:800; font-size:1.05rem; letter-spacing:-.02em; }}
    .brand-sub{{ font-size:12.5px; color:var(--muted); font-weight:600; letter-spacing:.04em; text-transform:uppercase; }}
    .nav{{ display:flex; flex-wrap:wrap; gap:8px; }}
    .pill{{
      padding:10px 15px; border-radius:999px; border:1px solid var(--line);
      background: rgba(255,255,255,.04); font-weight:700; font-size:12.5px;
    }}
    .pill:hover{{ background: rgba(34,211,238,.08); border-color: rgba(34,211,238,.35); }}
    .pill.cta{{
      border-color: rgba(34,211,238,.55);
      background: linear-gradient(135deg, rgba(34,211,238,.2), rgba(14,165,233,.12));
    }}
    .layout{{ display:grid; grid-template-columns: 240px 1fr; gap: 1.5rem; align-items:start; }}
    @media (max-width: 860px){{ .layout{{ grid-template-columns: 1fr; }} }}
    aside.navcol{{
      position:sticky; top:14px; padding:1rem 1rem 1.1rem; border-radius: var(--r);
      border:1px solid var(--line); background: var(--card); backdrop-filter: blur(10px);
    }}
    aside.navcol h2{{ margin:0 0 .75rem; font-size:10px; letter-spacing:.14em; text-transform:uppercase; color:var(--muted); font-weight:800; }}
    aside.navcol ul{{ margin:0; padding:0; list-style:none; }}
    aside.navcol li{{ margin:8px 0; }}
    aside.navcol a{{ color:var(--text); font-weight:600; font-size:13.5px; }}
    aside.navcol a[aria-current="page"]{{ color: var(--accent); }}
    main{{ min-width:0; }}
    .panel{{
      border:1px solid var(--line); border-radius: var(--r); background: var(--card);
      backdrop-filter: blur(12px); padding: 1.35rem 1.2rem 1.5rem;
    }}
    main h1{{ margin:0 0 .4rem; font-size: clamp(1.35rem, 3vw, 1.75rem); font-weight:800; letter-spacing:-.03em; }}
    .lede{{ margin:0 0 1rem; color: var(--muted); font-size: 14px; max-width: 65ch; line-height:1.65; }}
    .disclaimer{{ font-size:11.5px; color:var(--muted); font-style:italic; margin:0 0 1.25rem; max-width:70ch; }}
    .calc{{
      margin-bottom: 1.35rem; padding: 1.1rem 1.15rem 1.2rem;
      border-radius: var(--r); border:1px solid rgba(34,211,238,.22);
      background: linear-gradient(165deg, rgba(14,165,233,.12), rgba(15,23,42,.4));
    }}
    .calc h2{{ margin:0 0 .6rem; font-size:13px; font-weight:800; letter-spacing:.06em; text-transform:uppercase; color: var(--accent); }}
    .calc p.hint{{ margin:0 0 1rem; font-size:13px; color:var(--muted); }}
    .calc-row{{ display:flex; flex-wrap:wrap; gap:12px; align-items:flex-end; margin-bottom:12px; }}
    .calc-row label{{ display:flex; flex-direction:column; gap:6px; font-size:12px; font-weight:700; color:var(--muted); }}
    .calc-row select{{
      min-width:140px; padding:10px 12px; border-radius:10px; border:1px solid var(--line);
      background:#0f172a; color:var(--text); font-family:inherit; font-size:13px;
    }}
    .calc-row button{{
      padding:10px 18px; border-radius:10px; border:1px solid rgba(34,211,238,.45);
      background: linear-gradient(180deg, rgba(34,211,238,.25), rgba(14,165,233,.12));
      color:var(--text); font-weight:800; font-size:13px; cursor:pointer; font-family:inherit;
    }}
    .calc-row button:hover{{ filter:brightness(1.08); }}
    #fc-calc-out{{ font-size:13px; }}
    #fc-calc-out[hidden]{{ display:none !important; }}
    .sum-line{{ display:flex; align-items:center; gap:10px; flex-wrap:wrap; margin:6px 0; color:var(--muted); }}
    .sum-line img{{ width:20px; height:20px; border-radius:4px; pointer-events:none; user-select:none; }}
    .sum-line strong{{ color:var(--text); font-weight:800; }}
    .sum-days{{ margin-top:10px; padding-top:10px; border-top:1px solid var(--line); color:var(--muted); }}
    .sum-days strong{{ color:var(--accent2); }}
    .table-wrap{{ overflow-x: auto; margin-top: 4px; border-radius: 14px;
      border: 1px solid var(--line); background: rgba(3,7,18,.5); }}
    table{{ width: 100%; border-collapse: collapse; min-width: 1080px; }}
    thead th{{
      text-align: left; font-size: 12px; font-weight: 800; letter-spacing: .06em;
      text-transform: uppercase; color: var(--muted);
      padding: 12px 14px; background: rgba(15,23,42,.9); border-bottom: 1px solid var(--line);
    }}
    tbody td{{
      padding: 10px 14px; border-bottom: 1px solid rgba(148,163,184,.1);
      vertical-align: top; font-size: 13.5px; color: var(--muted);
    }}
    tbody tr:nth-child(even){{ background: rgba(255,255,255,.02); }}
    .level{{ font-weight: 800; white-space: nowrap; color: #fde68a; }}
    .cost-list{{ display: flex; flex-direction: column; gap: 6px; min-width: 180px; }}
    .cost-item{{ display: inline-flex; align-items: center; gap: 8px; white-space: nowrap; }}
    .fc-ico{{
      width: 20px; height: 20px; border-radius: 4px; flex: 0 0 20px; object-fit: cover;
      pointer-events: none; user-select: none; -webkit-user-drag: none;
    }}
    footer.foot{{ margin-top: 1.35rem; padding-top: 1rem; border-top: 1px solid var(--line);
      font-size: 12.5px; color: var(--muted); text-align:center; }}
  </style>
</head>
<body>
  <div class="wrap">
    <header class="mast">
      <div class="brand-block">
        <a href="../index.html" class="brand" style="color:inherit;text-decoration:none">
          <img src="/assets/logo.png" alt=""/>
          <div>
            <div class="brand-title">WOSC Database</div>
            <div class="brand-sub">Tabellen · Rechner · Planung</div>
          </div>
        </a>
      </div>
      <nav class="nav" aria-label="Hauptnavigation">
        <a class="pill" href="../index.html">Übersicht</a>
        <a class="pill" href="../../guides/heroes/">Helden</a>
        <a class="pill" href="../../guides/experts/">Experts</a>
        <a class="pill" href="../../guides/alliance-mobilization.html">AM</a>
        <a class="pill cta" href="https://discord.gg/wos-community" target="_blank" rel="noopener">Discord</a>
      </nav>
    </header>
    <div class="layout">
      <aside class="navcol" aria-label="Navigation">
        <h2>Menü</h2>
        <ul>
          <li><a href="../index.html">WOSC Database</a></li>
          <li><a href="fire-crystal-furnace.html" aria-current="page">Fire Crystal Furnace</a></li>
        </ul>
      </aside>
      <main>
        <div class="panel">
        <h1>Fire Crystal Furnace</h1>
        <p class="lede">Upgrade-Tabelle mit Stufe, Voraussetzungen, Ressourcen-Kosten, Bauzeit und Macht. Der Rechner addiert die Werte aus dieser Tabelle für einen gewählten Stufenbereich.</p>
        <p class="disclaimer">Eigenständige Community-Inhalte für Planung und Übersicht. Keine Verbindung zu Anbietern oder externen Datenportalen; keine Garantie auf Vollständigkeit.</p>

        <section class="calc" aria-labelledby="fc-calc-h">
          <h2 id="fc-calc-h">Upgrade-Rechner</h2>
          <p class="hint">Wähle <strong>Von</strong>- und <strong>Bis</strong>-Stufe (inklusive). Es werden alle dazwischenliegenden Aufwertungen summiert.</p>
          <div class="calc-row">
            <label>Von-Stufe <select id="fc-from"></select></label>
            <label>Bis-Stufe <select id="fc-to"></select></label>
            <button type="button" id="fc-calc-btn">Summe berechnen</button>
          </div>
          <div id="fc-calc-out" hidden></div>
        </section>

        <div class="table-wrap">
      <table id="fc-table">
        <thead>
          <tr>
            <th>Stufe</th>
            <th>Voraussetzungen</th>
            <th>Kosten</th>
            <th>Zeit</th>
            <th>Macht</th>
          </tr>
        </thead>
        <tbody>
{tbody}
        </tbody>
      </table>
        </div>
        <footer class="foot">
          <a href="../index.html">WOSC Database</a> ·
          <a href="/">Community</a> · <span data-y></span>
        </footer>
        </div>
      </main>
    </div>
  </div>
  <script>
  (function(){{
    document.querySelector("[data-y]").textContent = new Date().getFullYear();
    var ASSET = "{ASSET}";
    var ICONS = [
      ASSET + "/item_icon_100011.png",
      ASSET + "/item_icon_103.png",
      ASSET + "/item_icon_104.png",
      ASSET + "/item_icon_105.png",
      ASSET + "/item_icon_100081.png",
      ASSET + "/item_icon_100082.png"
    ];
    function parseAmount(t) {{
      t = String(t).trim();
      if (/M$/i.test(t)) {{
        return parseFloat(t.slice(0, -1).replace(/\\s/g, "").replace(",", ".")) * 1e6;
      }}
      return parseInt(t.replace(/\\./g, "").replace(/,/g, ""), 10) || 0;
    }}
    function parseDays(s) {{
      var m = String(s).match(/(\\d+)\\s*d/i);
      return m ? parseInt(m[1], 10) : 0;
    }}
    function fmt(n) {{
      if (Math.abs(n) >= 1e6) {{
        var v = n / 1e6;
        var r = Math.round(v * 100) / 100;
        return (r % 1 === 0 ? String(r) : r.toFixed(2).replace(/\\.?0+$/, "")) + "M";
      }}
      return String(Math.round(n));
    }}
    var rows = Array.prototype.slice.call(document.querySelectorAll("#fc-table tbody tr"));
    var data = rows.map(function(tr) {{
      var tds = tr.querySelectorAll("td");
      var spans = tds[2].querySelectorAll(".cost-item span");
      var costs = Array.prototype.map.call(spans, function(s) {{ return parseAmount(s.textContent); }});
      while (costs.length < 6) costs.push(0);
      return {{
        label: tds[0].textContent.trim(),
        costs: costs,
        days: parseDays(tds[3].textContent)
      }};
    }});
    var fromSel = document.getElementById("fc-from");
    var toSel = document.getElementById("fc-to");
    data.forEach(function(d, i) {{
      var o = document.createElement("option");
      o.value = String(i);
      o.textContent = d.label;
      fromSel.appendChild(o.cloneNode(true));
      toSel.appendChild(o.cloneNode(true));
    }});
    if (toSel.options.length) toSel.selectedIndex = toSel.options.length - 1;
    function calc() {{
      var a = parseInt(fromSel.value, 10);
      var b = parseInt(toSel.value, 10);
      var lo = Math.min(a, b), hi = Math.max(a, b);
      var sum = [0, 0, 0, 0, 0, 0];
      var totalDays = 0;
      for (var i = lo; i <= hi; i++) {{
        for (var j = 0; j < 6; j++) sum[j] += data[i].costs[j];
        totalDays += data[i].days;
      }}
      var out = document.getElementById("fc-calc-out");
      var html = "";
      for (var k = 0; k < 6; k++) {{
        if (sum[k] <= 0) continue;
        html += '<div class="sum-line"><img src="' + ICONS[k] + '" alt="" draggable="false"/><strong>' + fmt(sum[k]) + "</strong></div>";
      }}
      html += '<div class="sum-days">Gesamt-Bauzeit (Summe der Tage laut Tabelle): <strong>' + totalDays + " Tage</strong></div>";
      out.innerHTML = html;
      out.hidden = false;
    }}
    document.getElementById("fc-calc-btn").addEventListener("click", calc);
  }})();
  </script>
</body>
</html>
"""

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(TEMPLATE.format(tbody=tbody, ASSET=ASSET), encoding="utf-8")
print("written", OUT, "icons:", len(urls))
