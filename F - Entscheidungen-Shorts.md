# F — Entscheidungen: YouTube-Shorts aus dem Sonntagsgespräch

> Das **Warum** hinter den wichtigen Festlegungen. Neueste oben.

## Entscheidungs-Index

| Nr | Datum | Entscheidung |
|---|---|---|
| E-010 | 2026-06-10 | Short-Look: Markenblau-Hintergrund (Blur verworfen); Sprecher-Kacheln als Paar-Shot |
| E-009 | 2026-06-09 | Ab nächster Folge Transkription mit large-v3-turbo (Standard im Script) |
| E-008 | 2026-06-09 | Künftig „Lokale Aufnahmen" in StreamYard vor dem Stream aktivieren |
| E-007 | 2026-06-09 | StreamYard-Transkript ist kostenpflichtig → wir transkribieren lokal mit Whisper |
| E-006 | 2026-06-09 | Projekt gründlich als Skill-Fundament bauen (Meta-Verfahren G) |
| E-005 | 2026-06-09 | Untertitel: eingebrannte .ass-Karaoke-Captions, gebrandet |
| E-004 | 2026-06-09 | Veröffentlichung nur auf YouTube Shorts |
| E-003 | 2026-06-09 | Quelle: StreamYard-Originalaufnahme (Download) |
| E-002 | 2026-06-09 | Transkription: faster-whisper lokal (Python) |
| E-001 | 2026-06-09 | Schnitt-Werkzeuge: yt-dlp + ffmpeg (winget) |

---

## Entscheidungen (neueste oben)

### E-010 — 2026-06-10 — Short-Look: Markenblau + Paar-Kachel
**Entscheidung:** Hochkant-Hintergrund = Markenblau (#14507D), nicht unscharfer Video-Blur. Sprecher werden als Kachel-Ausschnitt formatfüllend zentriert; bei A&H die gemeinsame Kachel (Paar-Shot).
**Begründung:** Der Blur-Hintergrund ist derselbe gestreckte Frame → wirkt unten „verdoppelt" (Annettes Rückmeldung). Markenblau ist ruhiger, edler, on-brand. Annette sitzt im Original am linken Rand angeschnitten → Solo-Crop ungünstig; Paar-Shot löst das und ist markig.
**Auswirkung:** Standard-Framing für alle Shorts dieser Folge. Crop 408×355 @ (6,150) entfernt Kommentar- und Namens-Overlay; pad auf 1080×1920 in #14507D. Untertitel via `make_ass.py` (Karaoke, Koralle-Highlight).

### E-009 — 2026-06-09 — Transkription künftig mit large-v3-turbo
**Entscheidung:** Ab der nächsten Folge nutzt `transcribe.py` standardmäßig `large-v3-turbo` (statt large-v3).
**Begründung:** large-v3 läuft auf der CPU mit nur ~0,53× Echtzeit (60-Min-Gespräch ≈ 110 Min Rechenzeit). Turbo ist ~5–6× schneller bei praktisch gleicher deutscher Qualität → Transkript in ~10–15 Min. Verkürzt auch das Zeitfenster, in dem etwas schiefgehen könnte.
**Auswirkung:** Script-Default = large-v3-turbo; large-v3 bleibt als Qualitäts-Reserve per `--model large-v3`. **Pilot „Berührt sein" läuft noch mit large-v3 fertig** (nicht neu gestartet, da schon > Hälfte durch).

### E-008 — 2026-06-09 — „Lokale Aufnahmen" künftig aktivieren
**Entscheidung:** Bei kommenden Sonntagsgesprächen in StreamYard die Funktion „Lokale Aufnahmen" vor dem Stream einschalten.
**Begründung:** Beim „Berührt sein"-Stream waren keine lokalen Aufzeichnungen vorhanden („Keine lokalen Aufzeichnungen") → nur die kombinierte 3-Kachel-Aufnahme verfügbar. Lokale Aufnahmen liefern pro Person eine saubere Einzelspur (laut Plan bis 4K) → idealer Hochkant-Zuschnitt = deutlich bessere Shorts. Kostet nur einen Klick vor dem Stream.
**Auswirkung:** Pilot „Berührt sein" nutzt die kombinierte Aufnahme (Framing-Stufe 2: Crop auf die aktive Kachel). Ab nächster Folge bessere Quelle möglich. **Hinweis:** „Lokale Aufnahmen in 4K" ist ggf. ein Advanced-Plan-Feature → vor dem nächsten Stream prüfen, was der aktuelle Plan erlaubt.

### E-007 — 2026-06-09 — Transkription lokal (StreamYard-Transkript kostenpflichtig)
**Entscheidung:** Transkript wird lokal mit faster-whisper erzeugt, nicht aus StreamYard geladen.
**Begründung:** Der StreamYard-Transkript-Download ist hinter dem „Advanced"-Plan (Bezahlschranke). Kein Kauf nötig — Whisper liefert das ohnehin genauer (Wort-Zeitmarken für Karaoke-Untertitel) und kostenlos.
**Auswirkung:** Quelle = nur das heruntergeladene Video; Transkript entsteht lokal. Bestätigt E-002.

### E-006 — 2026-06-09 — Gründliches Fundament als Skill-Vorlage
**Entscheidung:** Der Workflow wird bewusst gründlich und sauber dokumentiert aufgebaut, nicht „quick & dirty". Ein Meta-Verfahren-Dokument (`G`) hält das wiederverwendbare Rahmenwerk fest.
**Begründung:** Das Sonntagsgespräch ist wöchentlich → der Workflow wiederholt sich dauerhaft und soll später ein eigener Claude-Skill werden. Einmal gut gebaut spart Woche für Woche Zeit und Nerven (💚) und ist die Grundlage für die Generalisierung.
**Auswirkung:** Zusätzliche Dokumente E (Style-Guide) und G (Meta-Verfahren). Höherer Anfangsaufwand, hoher Compound-Effekt.

### E-005 — 2026-06-09 — Untertitel als gebrannte .ass-Karaoke-Captions
**Entscheidung:** Untertitel werden im .ass-Format gestaltet (wortweises Highlight wie bei guten Reels/Shorts) und fest ins Bild eingebrannt — in Markenfarben, mit Markenschrift und dezentem A&H-Logo.
**Begründung:** Der größte sichtbare Qualitätsunterschied zu StreamYard. .ass erlaubt präzises Timing (aus den Whisper-Wort-Zeitmarken), große Lesbarkeit und Marken-Look. Eingebrannt = funktioniert überall, auch ohne dass der Zuschauer Untertitel aktiviert.
**Auswirkung:** Wir brauchen Wort-Zeitmarken (→ E-002 faster-whisper liefert die).

### E-004 — 2026-06-09 — Nur YouTube Shorts
**Entscheidung:** Die Shorts gehen ausschließlich auf YouTube. Instagram Reels und TikTok werden bewusst nicht bespielt.
**Begründung:** Fokus statt Verzettelung — volle Energie auf einen Kanal (Annettes ausdrückliche Entscheidung). Das Format (9:16) bliebe kompatibel, falls man später doch erweitert.
**Auswirkung:** Textbausteine nur für YouTube. Spart Aufwand pro Folge.

### E-003 — 2026-06-09 — Quelle: StreamYard-Originalaufnahme
**Entscheidung:** Quellmaterial ist die Originalaufnahme aus der StreamYard-Bibliothek (manueller Download), nicht das YouTube-Video.
**Begründung:** Beste Bildqualität ohne YouTube-Re-Encode. StreamYard hat keine API → Download läuft manuell über den Browser. Für die spätere Routine bleibt der YouTube-Weg (yt-dlp) als vollautomatisierbarer Fallback.
**Auswirkung:** Pro Folge ein manueller Download-Schritt. Zu prüfen: „Lokale Aufnahmen" in StreamYard (separate Einzelspuren je Person → ideal für sauberen Hochkant-Zuschnitt).

### E-002 — 2026-06-09 — Transkription mit faster-whisper (lokal)
**Entscheidung:** Transkription über **faster-whisper** (CTranslate2), lokal auf dem Windows-PC, Modell large-v3 für Deutsch.
**Begründung:** Genaues deutsches Transkript inkl. **Wort-Zeitmarken** (Basis für Karaoke-Untertitel und exakten Schnitt). faster-whisper ist leicht und schnell auf der CPU (kein PyTorch-Riese), unbegrenzt und kostenlos. Wispr Flow (Annettes Diktier-Abo) ist NICHT dasselbe und kann Videodateien nicht verschriften.
**Auswirkung:** Python wird benötigt (installiert E-001-Folgeschritt). Modell lädt einmalig (~1–3 GB).

### E-001 — 2026-06-09 — Schnitt-Werkzeuge yt-dlp + ffmpeg
**Entscheidung:** yt-dlp (Download/Untertitel) und ffmpeg (Schnitt) per winget installiert.
**Begründung:** Standard, kostenlos, skriptbar, von Christian wartbar. Beide laufen (verifiziert).
**Auswirkung:** Basis für die ganze Pipeline steht.
