# CLAUDE.md — YouTube-Shorts aus dem Sonntagsgespräch

**Einzeiler:** Aus jedem wöchentlichen YouTube-Sonntagsgespräch (A&H — Annette & Herbert) automatisch starke, berührende Shorts erstellen — inhaltlich ausgewählt, nicht mechanisch. Bessere Alternative zu den StreamYard-KI-Clips.

**Sprache:** Deutsch.

## Beteiligte
- **Annette Himmelstoß** — Coachin, Inhaberin (himmelstosscoaching.de), Stimme & Gesicht des Kanals
- **Herbert** — Ehemann, zweite Stimme im Sonntagsgespräch (A&H = Annette & Herbert)
- **Christian Seitz** — Technik/Dev; Projekt wird später für ihn auf **GitHub** hochgeladen
- **Claude** — macht die Arbeit (Transkript → Auswahl → Schnitt → Branding)

## Oberster Filter: Impact ÷ Ressourcen
```
Wert = Impact (Wirkung aufs Ziel) ÷ Ressourcen (💰 Geld + ⏰ Zeit + 💚 Emotionen/Nerv)
```
- 🚀 Riesen-Impact rein in den Plan, 🐭 homöopathische Spielereien lassen.
- **Annette-/Frau-Test:** Könnte Annette den Workflow im Notfall ohne Christian bedienen? Wenn nein → Komplexität runter.
- **Wer macht die Arbeit?** Annette/Christian = teuer. Claude = nachts kostenlos, automatisiert > einmalig.
- Empfehlungen durch die CEO-Brille filtern, bevor sie ausgesprochen werden.

## Dateiübersicht (immer zuerst lesen: A + B, Log-Index aus C; E/G bei Schnitt-Arbeit)
- `A - Projektbeschreibung-Shorts-V01.md` — Was, für wen, warum, Setup
- `B - Aufgaben-Shorts.md` — Phasen, Aufgaben, Meilensteine, Specs
- `C - Protokoll-Shorts.md` — Log-Index + Änderungsverlauf (neueste oben)
- `E - Style-Guide-Shorts.md` — Qualitäts-Messlatte: Format, Hook, Framing, Untertitel, Sprache
- `F - Entscheidungen-Shorts.md` — Warum hinter den Festlegungen (Tools, Quelle, Plattform …)
- `G - Meta-Verfahren-Shorts-V01.md` — wiederverwendbares Rahmenwerk (Basis für späteren Skill)
- `01-Workflow-Technik/` — Schnitt-Script, Installations-Notizen, ffmpeg/yt-dlp-Setup
- `02-Quellen-Transkripte/` — heruntergeladene Transkripte je Folge (+ Session-Template)
- `03-Shorts-Output/` — fertige Shorts, je Folge ein Unterordner
- `04-Marketing-Distribution/` — Titel/Beschreibungen/Hashtags, Posting-Plan, Newsletter-Anbindung
- `xold/` — Mülleimer (nie löschen, hierhin verschieben)

## Arbeitsregeln
- **Bei jedem Gesprächsstart:** A + B lesen, Log-Index aus C überfliegen. Kurz Stand zusammenfassen, 2–3 nächste To-dos vorschlagen.
- **Nach jedem abgeschlossenen Schritt:** sofort C (Protokoll) aktualisieren + Log-Index pflegen.
- **Nach Context-Compact:** A + B erneut lesen.
- **Dateien NIE löschen** → nach `xold/`. Neue Version = neue Nummer (V01→V02), alte nach `xold/`.
- **Dateireferenzen aktuell halten** (Pfade in dieser CLAUDE.md sofort nachziehen).
- **Nach außen nur PDF, nie DOCX.**
- **Diktierfehler:** Annette diktiert oft — Namen, Domains, Fachbegriffe gegenchecken.
- **Projektreview** nach je 10 erledigten Aufgaben (Stand, Doppelungen, Struktur, Aufräumen).

## Technik-Kontext (Stand Setup)
- Rechner: Windows. Installiert ✅: `git`, `yt-dlp` (2026.03.17), `ffmpeg` (N-124716), `python` 3.12.10. `faster-whisper` in Installation.
- Python liegt unter `%LOCALAPPDATA%\Programs\Python\Python312\python.exe` (Windows-Store-Platzhalter „python" verdeckt es ggf. → vollen Pfad nutzen). PATH in neuer Shell ggf. aus Registry frisch laden.
- **StreamYard hat KEINE öffentliche API** → keine direkte Anbindung. Quelle = Originalaufnahme aus StreamYard-Bibliothek (Download) oder das veröffentlichte Video auf YouTube (yt-dlp).
- StreamYard-KI-Clips: limitiert (6 Generierungen, Stand Setup 2/6 genutzt), Qualität unbefriedigend → wir bauen eigene Shorts.

## Referenz / verbundene Projekte
- HSC-Website: himmelstosscoaching.de · [[project_hsc_website]]
- Logo & Farben: Blau **#14507D**, Koralle **#E0998C** · [[reference_logo]]
- Datenschutz-Linie beachten · [[feedback_datenschutz]]
