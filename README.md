# WOSC – Whiteout Survival Community Website

Website für den WOSC Discord (Whiteout Survival): 23 Sprachen, SEO, SVS/Bear Trap/Frostfire/Transfers.

## GitHub Pages

Die Seite läuft unter **GitHub Pages** (Projekt- oder User-Site):

1. Repo auf GitHub pushen.
2. **Settings → Pages**: Source = *Deploy from a branch*; Branch = `main` (oder `master`), Folder = `/ (root)`.
3. Nach dem Deploy:
   - **Projekt-Site:** `https://<user>.github.io/<repo-name>/`
   - **User-Site:** `https://<user>.github.io/`

Pfade für Übersetzungen (`index.json`) und Assets werden automatisch an den Repo-Pfad angepasst. Sprach-Redirects (z. B. `/de/`) nutzen relative Pfade (`../?lang=de`), damit sie mit Projekt-Sites funktionieren.

## Struktur

- `index.html` – Hauptseite (alle Sprachen über `?lang=xx`)
- `index.json` – Übersetzungen (23 Sprachen)
- `en/`, `de/`, … – Redirects zu `/?lang=xx`
- `assets/` – Bilder, Logo, Favicon
- `guides/` – Helden-, Experts-, AM-Guides
- `sitemap.xml` – für Suchmaschinen (bei Custom Domain anpassen)

## Custom Domain

Wenn du eine eigene Domain (z. B. `www.whiteoutsurvival-community.com`) nutzt: In Pages-Einstellungen die Domain eintragen und im Repo eine leere Datei `CNAME` mit dem Domain-Namen anlegen.
