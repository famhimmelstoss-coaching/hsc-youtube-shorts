# C — Protokoll: YouTube-Shorts aus dem Sonntagsgespräch

> Änderungsprotokoll. Was wurde wann gemacht? Aufgaben/Planung → siehe `B - Aufgaben-Shorts.md`.

## Log-Index (Schnellübersicht)

| Log | Datum | Beschreibung |
|-----|-------|-------------|
| LOG-006 | 2026-06-10 | Short A final = Markenblau v6 (57s); Verlauf vertagt; GitHub-Push (öffentlich) |
| LOG-005 | 2026-06-10 | Short A fertig: A&H-Variante (~53s), Markenblau, Karaoke-Untertitel; Pipeline validiert |
| LOG-004 | 2026-06-09 | Pilot „Berührt sein": Video geladen (720p), Layout analysiert, Transkription gestartet |
| LOG-003 | 2026-06-09 | Fundament-Ausbau: Werkzeuge installiert, E/F/G angelegt, Entscheidungen fixiert |
| LOG-002 | 2026-06-09 | StreamYard gesichtet — Bibliothek, KI-Clips, Download-Optionen, keine API |
| LOG-001 | 2026-06-09 | Projektstart — Struktur, CLAUDE.md, A/B/C, Werkzeug-Check |

---

## Protokoll-Verlauf (neueste oben!)

### LOG-006 — 2026-06-10 — Short A final (Markenblau) + GitHub
- **Feinschliff Short A** (Annettes Wünsche): keine angeschnittenen Wörter → Schnitte per `silencedetect` exakt in die Sprechpausen gelegt; „Nachklang"-Pause 0,8 s an den Übergängen; Teil 2 bis „…in dieser Dankbarkeit" verlängert (Echo zu Teil 1). Finale Fassung: **Short_A v6, Markenblau, 57 s** (im Projekt + Desktop).
- **Verlauf (blau→lachs) versucht, vertagt:** (1) Optik — Voll-Höhen-Verlauf macht den unteren Rand matschig → Untertitel leiden; Boden muss blau bleiben. (2) Technik — Verlauf-Overlay bläht die Videospur auf (Overlay läuft übers fg-Ende hinaus). **Fix fürs nächste Mal:** `overlay=...:shortest=1`, Verlauf nur in den oberen Rand (z. B. blau ab Bildmitte), `-vsync cfr`. Auf Annettes Wunsch erst beim nächsten Short sauber umsetzen.
- **GitHub:** Projekt öffentlich gepusht (Sonntagsgespräch ist öffentlich), damit Christian den Short prüfen und auf YouTube stellen kann. Account `famhimmelstoss-coaching`.
- Offen: Shorts C, B, D, G (später); YouTube-Link für Beschreibung.

### LOG-005 — 2026-06-10 — Short A fertig (A&H-Variante)
- Transkript (1053 Segmente) komplett gelesen → Momentauswahl (A–G) in `02-Quellen-Transkripte/..._Auswahl.md`.
- **Look-Entscheidung:** Markenblau-Hintergrund (Blur-Variante verworfen — „Verdopplung" durch gestreckten Hintergrund). → F E-010.
- **Short A gebaut:** 3 Teile (Annette/Annette/Herbert), ~53 s, 9:16, sauberer Kachel-Zuschnitt (crop 408×355@6,150 — entfernt Kommentar- UND Namens-Overlay), Markenblau-Pad, **Karaoke-Untertitel** aus Wort-Zeitmarken, Audio −14 LUFS.
- **Neue Werkzeuge:** `01-Workflow-Technik/make_ass.py` (Karaoke-.ass-Generator). Pipeline `Transkript → Auswahl → make_ass → ffmpeg crop/pad/subtitles → concat` end-to-end **validiert**.
- **Deliverables:** `03-Shorts-Output/2026-06-07_Beruehrt-sein/Short-A_...AundH.mp4` + Texte in `04-Marketing-Distribution/..._Texte.md`. Kopie auf Desktop.
- Offen: Annettes finale Sichtung; YouTube-Link fürs Beschreibungs-`[LINK]`; Shorts C, B, D, G.

### LOG-004 — 2026-06-09 — Pilot „Berührt sein": Material & Analyse
- **Browser/StreamYard:** „Lokale Aufnahmen" = keine vorhanden (Funktion war nicht aktiv) → künftig aktivieren (F E-008). Transkript-Download kostenpflichtig → lokal mit Whisper (F E-007).
- **Video geladen:** kombinierte Aufnahme, **1280×720, 30 fps, h264, ~60,6 Min, 1,36 GB**. Lokaler Arbeitsordner (NICHT OneDrive): `%USERPROFILE%\Shorts-Arbeit\2026-06-07_Beruehrt-sein\2026-06-07_Beruehrt-sein.mp4`.
- **Layout-Analyse (frame_1200):** 3 Kacheln à ~415×405 — links Annette & Herbert (Annette am linken Rand teils angeschnitten), Mitte Christian, rechts Godiwa; oben A&H-Logo-Band; unten zeitweise eingebranntes YouTube-Kommentar-Overlay. → Einzel-Hochkant von Annette schwierig; Framing-Varianten beim Schnitt zeigen.
- **Werkzeug-Script:** `01-Workflow-Technik/transcribe.py` (faster-whisper → SRT/TXT/JSON mit Wort-Zeitmarken) angelegt.
- **Transkription gestartet** (Hintergrund, large-v3) → Ausgabe nach `02-Quellen-Transkripte/`.
- CPU: 16 Kerne.

### LOG-003 — 2026-06-09 — Fundament-Ausbau (Skill-tauglich)
- Annette-Vorgabe: gründlich bauen, wird wöchentlich + späterer Skill → solides Fundament.
- **Installiert & verifiziert:** yt-dlp (2026.03.17) ✅, ffmpeg (N-124716) ✅, Python 3.12.10 ✅, faster-whisper 1.2.1 ✅ (Import getestet). Werkzeugkette komplett.
- **Entscheidungen fixiert (→ F):** Quelle = StreamYard-Original (E-003), nur YouTube Shorts (E-004), Untertitel = .ass-Karaoke eingebrannt (E-005), Transkription = faster-whisper large-v3 (E-002), Skill-Fundament (E-006).
- **Neue Dokumente:** `E - Style-Guide` (Qualitäts-Messlatte), `F - Entscheidungen`, `G - Meta-Verfahren` (7-Stufen-Rahmenwerk als Skill-Vorlage).
- **B aktualisiert:** INFRA-Phase fortgeschrieben, Phase META (Skill-Vorlage) ergänzt, M5 (Skill) als Meilenstein.
- **Wispr Flow ≠ Whisper** geklärt (Diktier-App vs. Transkriptions-Engine).
- Offen: faster-whisper fertigstellen + Modell-Test; StreamYard „Lokale Aufnahmen" prüfen (Framing); Pilot-Download „Berührt sein".

### LOG-002 — 2026-06-09 — StreamYard-Recherche
- StreamYard-Konto „K" im Chrome gesichtet (Team-Bibliothek).
- **Bibliothek:** alle bisherigen Sonntagsgespräche vorhanden; aktuellstes „Berührt sein – ein Wegweiser zu deinen innersten Sehnsüchten", 7. Juni 2026, 1:00:35. Teilnehmer: Annette & Herbert, Christian, Godiwa Jung.
- **KI-Clips:** bereits 2 Generierungen erstellt (8. Juni 09:41 + 7. Juni 11:01), alle „Hohe Viralität". Titel u.a. „Als unser Hund Sternchen starb…", „Gänsehaut beim Lesen…", „Berührtsein macht lebendig…".
- **Limits:** KI-Clips 2/6 Generierungen genutzt; Speicher 31,6/50 Std.
- **Funktionen pro Video:** Herunterladen (Originalaufnahme), Bearbeiten, Clips erstellen; pro Clip: Anpassen, Teilen, Herunterladen.
- **Befund:** Keine öffentliche StreamYard-API → keine Programm-Anbindung. Weg: Original/YouTube herunterladen und eigene Shorts bauen.
- Noch NICHT heruntergeladen (Download = Annettes Freigabe nötig).

### LOG-001 — 2026-06-09 — Projektstart
- Projektordner unter `02_Marketing/_Allgemein/YouTube-Shorts-Sonntagsgespraech/` angelegt.
- Unterordner: 01-Workflow-Technik, 02-Quellen-Transkripte, 03-Shorts-Output, 04-Marketing-Distribution, xold.
- CLAUDE.md, A (Projektbeschreibung V01), B (Aufgaben), C (Protokoll) erstellt.
- Werkzeug-Check: git ✅ vorhanden; yt-dlp / ffmpeg / python fehlen.
- Übergabeprotokoll aus Vor-Chat eingearbeitet (yt-dlp + ffmpeg-Ansatz).
