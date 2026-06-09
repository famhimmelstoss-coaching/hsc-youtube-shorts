# G — Meta-Verfahren: Shorts aus einem Langvideo (V01)

> **Zweck:** Das wiederverwendbare Rahmenwerk hinter dem Projekt. Wöchentlich anwendbar und so beschrieben, dass daraus später ein **Claude-Skill** wird (eine Folge = ein Befehl). Wächst mit jedem Durchlauf.

## Warum dieses Dokument
Das Sonntagsgespräch kommt jede Woche. Der Weg „Langvideo → mehrere starke Shorts" wiederholt sich identisch. Statt jedes Mal neu zu überlegen, halten wir hier den Ablauf, die Werkzeuge und die Vorlagen fest. Ziel: irgendwann sagt Annette nur noch „mach die Shorts vom Sonntagsgespräch" und der Skill erledigt den deterministischen Teil; Claude steuert das Urteilsvermögen (Momentauswahl, Titel).

## Das Rahmenwerk auf einen Blick
```
[1] INGEST      Quellvideo holen        →  Video.mp4
        │        (StreamYard-Download / yt-dlp)
[2] TRANSCRIBE  faster-whisper          →  Transkript + Wort-Zeitmarken (JSON/SRT)
        │
[3] SELECT      Claude wählt nach Sinn  →  Edit Decision List (EDL):
        │        3–6 Momente               Start–Ende, Titel, Hook, Begründung
        │        → Annette gibt frei
[4] CUT         ffmpeg trim + 9:16      →  Roh-Clips (Hook zuerst)
        │
[5] CAPTION     .ass-Karaoke einbrennen →  gebrandete Shorts
        │        + Logo + Audio-Norm
[6] PACKAGE     Ablage + Textbausteine  →  03-Shorts-Output/[Folge]/ + Titel/Beschreibung/Hashtags
        │
[7] PUBLISH     Freigabe → YouTube      →  veröffentlicht + Log in C
```
**Wer macht was:** [1][2][4][5][6] = Script/Claude automatisch · **[3] Auswahl + Titel = Claudes Urteil** (der eigentliche Mehrwert) · **[3-Freigabe] + [7] = Annette**.

## Stufen im Detail

### [1] INGEST
- **Input:** StreamYard-Aufnahme **oder** YouTube-Link.
- **Schritte:** StreamYard → „Herunterladen" (manuell, Browser); YouTube → `yt-dlp <link>`.
- **Output:** eine MP4 im Arbeitsordner.
- **Offen/Prüfen:** StreamYard „Lokale Aufnahmen" (Einzelspuren je Person) für besseres Framing.

### [2] TRANSCRIBE
- **Tool:** `faster-whisper`, Modell `large-v3`, Sprache `de`, `word_timestamps=True`.
- **Output:** Transkript mit Segment- **und Wort**-Zeitmarken → `02-Quellen-Transkripte/JJJJ-MM-TT-[Folge].json` (+ lesbares .md/.srt).

### [3] SELECT (Kern — Claudes Urteil)
- **Input:** Transkript.
- **Schritte:** ganzes Gespräch inhaltlich erfassen; 3–6 Momente nach den Kriterien aus `E` (Style-Guide, Abschnitt 6) wählen; je Moment Start/Ende auf Wort-Ebene festlegen, Titel + Hook + 1-Satz-Begründung.
- **Output:** **EDL** als Tabelle (siehe Session-Template). Annette streicht/ergänzt → Freigabe.

### [4] CUT
- **Tool:** ffmpeg. Trim auf Zeitfenster; ggf. Hook-Satz nach vorn; Skalierung/Crop auf 1080×1920 nach Framing-Stufe (E, Abschnitt 3).
- **Output:** stumm-geschnittene 9:16-Roh-Clips (Bild+Originalton).

### [5] CAPTION
- **Tool:** .ass aus Wort-Zeitmarken erzeugen (Karaoke-Highlight, Markenfarben), `ffmpeg -vf "subtitles=...ass"` einbrennen; Logo-Overlay; Audio auf −14 LUFS.
- **Output:** fertiger Short.

### [6] PACKAGE
- Ablage `03-Shorts-Output/[Folge]/`; je Short ein Textblock (Titel/Beschreibung/Hashtags) in `04-Marketing-Distribution/` — floskelfrei (E, Abschnitt 5).

### [7] PUBLISH
- Annette sichtet/gibt frei → Upload als YouTube Short → Log-Eintrag in `C`.

## Skill-Reifegrad (was zum Skill noch generalisiert wird)
- **Parameter:** Quelle (Datei/Link), Anzahl Shorts, Längenfenster, Framing-Stufe, Branding-Set.
- **Deterministisch (Script):** [1][2][4][5][6]. **Urteil (Claude):** [3] + Titel.
- **Reproduzierbarkeit:** Script(e) in `01-Workflow-Technik/`, später Repo für Christian (GitHub).
- **Generalisierbar über das Sonntagsgespräch hinaus:** jedes Langvideo → Shorts (Webinare, Interviews, Vorträge).

## Anwendungs-Beispiele
| # | Folge | Datum | Ergebnis |
|---|---|---|---|
| 1 | „Berührt sein – ein Wegweiser zu deinen innersten Sehnsüchten" | 2026-06-07 | Pilot — in Arbeit |
