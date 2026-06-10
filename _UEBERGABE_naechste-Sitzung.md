# 🔄 Übergabe — nächste Sitzung (YouTube-Shorts Sonntagsgespräch)

> **Neue Sitzung so starten:** Claude Code im Projektordner öffnen, diese Datei + `CLAUDE.md` lesen lassen. Dann „Bau Short D" sagen. Alles Nötige steht hier.
> Stand: 2026-06-10. Verfasst nach sehr langem Chat → frischer Start.

## ✅ Was fertig ist
- **Short A** („Sternchen & Dankbarkeit", A&H, **57 s, Markenblau**) — fertig, abgenommen.
  - Datei: `03-Shorts-Output/2026-06-07_Beruehrt-sein/Short-A_Sternchen-Dankbarkeit_AundH.mp4`
  - Desktop: `Short A ansehen.mp4`
- **Auf GitHub gepusht (öffentlich):** https://github.com/famhimmelstoss-coaching/hsc-youtube-shorts (Account `famhimmelstoss-coaching`, gh CLI eingeloggt). Christian prüft + lädt auf YouTube.
- **Werkzeuge installiert:** yt-dlp, ffmpeg, Python 3.12, faster-whisper. Transkript der Folge liegt vor (Wort-Zeitmarken).

## ▶️ SOFORT ALS NÄCHSTES: Short D bauen (von Annette freigegeben)
Plan + genaue Stellen: **`02-Quellen-Transkripte/2026-06-07_Beruehrt-sein_Short-D-Plan.md`**
Kurz: 3 Teile, Annette spricht (Paar-Shot), ~50 s:
1. Hook 2:41 — Schlaganfälle → „anfälliger fürs Berührtsein, ständig Tränen"
2. 53:56 — „verlangsamt … ich koche sonst in 10 Min, das ging nicht mehr"
3. 55:02 — „diese Verlangsamung holt die Seele rein … dadurch stimmiger"
**Neu beim Rahmen:** Verlauf **oben Lachs → unten Blau** (siehe unten).

## 🎨 Verlauf-Rahmen (NEU, beim Bauen von D umsetzen)
- Annette-Wunsch: StreamYard-Farben gespiegelt — **oben Lachs, unten Blau**. Beim Bauen kurz StreamYard öffnen und **exakte Farbwerte abnehmen** (Marke: Blau `#14507D`, Koralle/Lachs `#E0998C`).
- **Boden MUSS blau bleiben** (Untertitel-Lesbarkeit, Koralle-Highlight braucht dunklen Grund).
- **Technik-Fix (Short A scheiterte hier):** Verlauf-Overlay blähte die Videospur auf. Lösung: `overlay=(W-w)/2:(H-h)/2:shortest=1`, zusätzlich `,fps=30` und `-vsync cfr -r 30`. Concat per **concat-Filter (re-encode)**, NICHT `-c copy` (gab kaputte Dauer). Vorher an EINEM Teil testen (ffprobe-Dauer prüfen!), bevor alles gerendert wird.
- Alternative, falls Verlauf zickt: einfach **Markenblau** nehmen (wie Short A) — funktioniert sicher.

## 🔧 Bewährte Pipeline (aus Short A — bitte genau so)
**Pfade:**
- Quellvideo (lokal, NICHT OneDrive): `%USERPROFILE%\Shorts-Arbeit\2026-06-07_Beruehrt-sein\2026-06-07_Beruehrt-sein.mp4` (1280×720, 30 fps, ~60,6 Min)
- Python: `%LOCALAPPDATA%\Programs\Python\Python312\python.exe`
- Transkript-JSON (Wort-Zeitmarken): `02-Quellen-Transkripte\2026-06-07_Beruehrt-sein.json`
- Skripte: `01-Workflow-Technik\transcribe.py`, `01-Workflow-Technik\make_ass.py`
- Render-Tempordner: `C:\Temp\shortsA` (umlautfrei — wichtig für libass/`subtitles=`)

**PATH in jeder PowerShell frisch laden:**
`$env:Path = [Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [Environment]::GetEnvironmentVariable("Path","User")`

**Schritte pro Short:**
1. **Saubere Schnitte:** exakte Wort-Zeiten via `dump.py` (in C:\Temp\shortsA) bzw. JSON; Schnittpunkte mit `silencedetect=noise=-32dB:d=0.05` in die echten Sprechpausen legen → **keine angeschnittenen Wörter** (Annette achtet darauf!).
2. **Untertitel (Karaoke):** `make_ass.py JSON --from S --to E --zero SS --out teil.ass` (weiß → Koralle pro Wort, sitzt unten).
3. **Bild:** Kachel Annette&Herbert: `crop=408:355:6:150` (entfernt Kommentar-/Namens-Overlay), `scale=1080:-2`, dann Hintergrund (Markenblau via `pad=1080:1920:(ow-iw)/2:(oh-ih)/2:color=0x14507D` ODER Verlauf-Overlay s.o.), `subtitles='C\:/Temp/shortsA/teil.ass'`.
4. **Nachklang:** `tpad=stop_mode=clone:stop_duration=0.8` (Video) + `apad=pad_dur=0.8` (Audio) am Teil-Ende. Ton: `loudnorm=I=-14:TP=-1.5:LRA=11`, `-ar 48000`.
5. **Zusammenfügen:** concat-Filter mit Neukodierung (`concat=n=3:v=1:a=1`), `-preset veryfast -crf 20`. **Dauer mit ffprobe prüfen** (~50–60 s, nicht aufgebläht!).

**Datei zeigen (Desktop ist OneDrive-umgeleitet!):**
- Ziel: `[Environment]::GetFolderPath('Desktop')` (NICHT `%USERPROFILE%\Desktop`).
- Lose Kopie + `Start-Process explorer.exe "<ordner>"`, damit Annette es sofort findet.

**Wach-Modus** bei langen Läufen (SetThreadExecutionState, Flags 0x80000000|1|2; am Ende nur 0x80000000).

## ⚙️ Berechtigungen
Annette nutzt **Auto-Modus** (Shift+Tab im Eingabefeld) → keine Settings-Änderung nötig, läuft autonom durch.

## 📌 Danach offen
- YouTube-Link fürs Beschreibungs-`[LINK]` in `04-Marketing-Distribution/..._Texte.md` (Annette/Christian beim Upload).
- Weitere Shorts: **C** (Christian – Gänsehaut), **B** (Godiwa – „das Ja an die Seele"), **G** (Herbert – Musik), evtl. **F** (Welpe), **E** (schöne Orte). Auswahl: `..._Auswahl.md`.
- Nach jedem fertigen Short: GitHub aktualisieren (commit + push).
- Perspektive: aus dem Ganzen später einen **Skill** bauen (Meta-Verfahren `G`).
- Ab nächster Folge: Transkription mit `large-v3-turbo` (schneller).
