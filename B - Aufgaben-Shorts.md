# B — Aufgaben: YouTube-Shorts aus dem Sonntagsgespräch

> Phasen, Aufgaben, Meilensteine, Specs. Änderungsverlauf → siehe `C - Protokoll-Shorts.md`.
>
> **Legende:** 📄 Dokument/Text · ⚙️ Technik/Code · 👁️ Perspektivwechsel · ◆ Meilenstein
> **Bewertung:** Claude (✅ allein / ⚠️ teils / ❌ Mensch) · Impact (🔴🟡🟢) · Aufwand (💰⏰💚 je 🟢🟡🔴) · Risiko (🔴🟡🟢)

## Aufgaben nach Phasen

### Phase 1 — Infrastruktur (INFRA)

> Status: 🔄 In Arbeit — Werkzeuge bereitstellen, damit überhaupt geschnitten werden kann.

| Nr | Aufgabe | Claude | Impact | Aufwand | Braucht | Risiko | Rollback | Status |
|---|---|---|---|---|---|---|---|---|
| INFRA-01 | ⚙️ Projektstruktur + CLAUDE.md/A/B/C/E/F/G anlegen | ✅ | 🔴 | 💰🟢 ⏰🟡 💚🟢 | — | 🟢 | — | ✅ Erledigt |
| INFRA-02 | ⚙️ yt-dlp + ffmpeg per winget installieren | ✅ | 🔴 | 💰🟢 ⏰🟡 💚🟢 | — | 🟢 | deinstallieren | ✅ Erledigt |
| INFRA-03 | ⚙️ Python 3.12 + faster-whisper installieren (Import getestet ✅) | ✅ | 🔴 | 💰🟢 ⏰🟡 💚🟢 | — | 🟢 | deinstallieren | ✅ Erledigt |
| INFRA-04 | ⚙️ Quelle: StreamYard-Original (entschieden, → F E-003) | ✅ | 🔴 | 💰🟢 ⏰🟢 💚🟢 | — | 🟢 | — | ✅ Erledigt |
| INFRA-05 | ⚙️ YouTube-Kanal-Link + Folge-Link erfassen (für Routine/Fallback) | ⚠️ | 🟡 | 💰🟢 ⏰🟢 💚🟢 | Annette: Links | 🟢 | — | ⬜ Offen |
| INFRA-06 | 🔎 StreamYard „Lokale Aufnahmen" prüfen: Einzelspuren je Person? (Framing-Qualität) | ⚠️ | 🔴 | 💰🟢 ⏰🟢 💚🟢 | Annette: Browser-OK | 🟢 | — | ⬜ Offen |
| ◆ | **M1: Werkzeuge laufen, Quelle steht, Fundament-Doks (E/F/G) da** | | | | | | | 🔄 In Arbeit |

### Phase 2 — Schnitt-Engine (CUT)

> Status: ⬜ Offen — das Herzstück: aus Transkript Momente wählen und Shorts bauen.

| Nr | Aufgabe | Claude | Impact | Aufwand | Braucht | Risiko | Rollback | Status |
|---|---|---|---|---|---|---|---|---|
| CUT-01 | ⚙️ Quellvideo geladen (720p) + Transkript (Whisper läuft) | ✅ | 🔴 | 💰🟢 ⏰🟡 💚🟢 | — | 🟡 | erneut ziehen | 🔄 In Arbeit |
| CUT-02 | 📄 Transkript inhaltlich analysieren → 3–6 beste Momente (mit Zeitfenster + Begründung) | ✅ | 🔴 | 💰🟢 ⏰🟡 💚🟢 | CUT-01 | 🟢 | neu auswählen | ⬜ Offen |
| CUT-03 | ⚙️ ffmpeg-Schnitt: Zeitfenster → 9:16, Hook zuerst | ✅ | 🔴 | 💰🟢 ⏰🔴 💚🟡 | CUT-02 | 🟡 | Revert | ⬜ Offen |
| CUT-04 | ⚙️ Untertitel einbrennen, gebrandet (#14507D/#E0998C, Logo) | ✅ | 🔴 | 💰🟢 ⏰🔴 💚🟡 | CUT-03 | 🟡 | Revert | ⬜ Offen |
| CUT-05 | ⚙️ Alles als wiederholbares Script bündeln (1 Befehl pro Folge) | ✅ | 🔴 | 💰🟢 ⏰🟡 💚🟢 | CUT-01..04 | 🟡 | Revert | ⬜ Offen |
| CUT-06 | ⚙️ Code-Review Phase 2 | ✅ | 🟡 | 💰🟢 ⏰🟡 💚🟢 | — | 🟢 | — | ⬜ Offen |
| ◆ | **M2: Ein Befehl erzeugt aus 1 Folge 3–6 fertige Shorts** | | | | | | | ⬜ Offen |

### Phase 3 — Pilot „Berührt sein" (PILOT)

> Status: ⬜ Offen — echter Durchlauf am Gespräch vom 7. Juni 2026.

| Nr | Aufgabe | Claude | Impact | Aufwand | Braucht | Risiko | Rollback | Status |
|---|---|---|---|---|---|---|---|---|
| PILOT-01 | ⚙️ „Berührt sein" durch den Workflow jagen → Shorts in `03-Shorts-Output/` | ✅ | 🔴 | 💰🟢 ⏰🟡 💚🟢 | M2 | 🟡 | neu | ⬜ Offen |
| PILOT-02 | 📄 Textbausteine je Short (Titel/Beschreibung/Hashtags), floskelfrei | ✅ | 🔴 | 💰🟢 ⏰🟢 💚🟢 | PILOT-01 | 🟢 | — | ⬜ Offen |
| PILOT-03 | 👁️ Vergleich: unsere Shorts vs. StreamYard-Clips — was ist besser, was fehlt? | ✅ | 🔴 | 💰🟢 ⏰🟢 💚🟡 | PILOT-01 | 🟢 | — | ⬜ Offen |
| PILOT-04 | 👁️ Freigabe durch Annette | ❌ | 🔴 | 💰🟢 ⏰🟢 💚🟢 | Annette: Sichtung | 🟢 | — | ⬜ Offen |
| ◆ | **M3: Pilot freigegeben — Shorts überzeugen Annette** | | | | | | | ⬜ Offen |

### Phase 4 — Routine & Übergabe (FLOW)

> Status: ⬜ Offen — wöchentlich tragfähig machen + Christian/GitHub.

| Nr | Aufgabe | Claude | Impact | Aufwand | Braucht | Risiko | Rollback | Status |
|---|---|---|---|---|---|---|---|---|
| FLOW-01 | 📄 Session-Template je Folge nutzen (`02-Quellen-Transkripte/`) | ✅ | 🟡 | 💰🟢 ⏰🟢 💚🟢 | M3 | 🟢 | — | ⬜ Offen |
| FLOW-02 | ⚙️ GitHub-Repo vorbereiten + Script hochladen (für Christian) | ✅ | 🟡 | 💰🟢 ⏰🟡 💚🟢 | Annette: OK, Repo-Name | 🟡 | privat halten | ⬜ Offen |
| FLOW-03 | ⚙️ Optional: wöchentliche Automatik (neues Sonntagsgespräch erkennen) | ⚠️ | 🟡 | 💰🟢 ⏰🔴 💚🟡 | Routine steht | 🟡 | abschalten | ⬜ Offen |
| FLOW-04 | 👁️ Perspektivwechsel: Zielgruppensicht auf einen kompletten Short-Durchlauf | ✅ | 🔴 | 💰🟢 ⏰🟢 💚🟡 | Annette: Review | 🟢 | — | ⬜ Offen |
| ◆ | **M4: Wöchentliche Routine läuft, Christian kann übernehmen** | | | | | | | ⬜ Offen |

### Phase META — Skill-Vorlage pflegen (durchgängig parallel)

> Das Meta-Verfahren `G` wird nach jeder Phase mit den echten Schritten gefüttert, bis daraus ein Claude-Skill werden kann.

| Nr | Aufgabe | Claude | Impact | Aufwand | Braucht | Risiko | Rollback | Status |
|---|---|---|---|---|---|---|---|---|
| META-01 | 📄 Grundgerüst `G - Meta-Verfahren` (Rahmenwerk, 7 Stufen) | ✅ | 🔴 | 💰🟢 ⏰🟡 💚🟢 | — | 🟢 | — | ✅ Erledigt |
| META-02 | 📄 Nach Pilot: Schnitt-/Caption-Schritte konkretisieren (echte ffmpeg-Befehle, .ass-Vorlage) | ✅ | 🔴 | 💰🟢 ⏰🟡 💚🟢 | M3 | 🟢 | — | ⬜ Offen |
| META-03 | ⚙️ Daraus einen Claude-Skill bauen (`/shorts-aus-langvideo` o.ä.) | ✅ | 🔴 | 💰🟢 ⏰🔴 💚🟢 | Routine steht | 🟡 | — | ⬜ Offen |
| ◆ | **M5: Skill nutzbar — „mach die Shorts vom Sonntagsgespräch"** | | | | | | | ⬜ Offen |

## Aufgabenbeschreibungen (Specs)

### CUT-02 — Momentauswahl nach Sinn (das eigentliche Unterscheidungsmerkmal)
**Was:** Aus dem Transkript mit Zeitmarken die 3–6 Stellen finden, die als Short funktionieren.
**Kriterien:** (1) emotionaler Bogen oder klare Erkenntnis; (2) kleiner Geschichts-Charakter (Anfang–Mitte–Ende); (3) starker erster Satz als Hook; (4) verständlich ohne Kontext des Gesamtgesprächs; (5) Authentizität statt Floskel.
**Output:** Liste mit Zeitfenster (Start–Ende), Titelvorschlag, Begründung „warum dieser Moment". Annette kann streichen/ergänzen, bevor geschnitten wird.

### CUT-03/04 — 9:16-Schnitt + gebrandete Untertitel
**Crop:** auf die sprechende Person fokussieren (nicht starre Mitte). Hook ggf. nach vorn ziehen.
**Untertitel:** wortweise/zeilenweise, große lesbare Schrift, Markenfarben, dezentes A&H-Logo oben (wie im Stream).
**Quelle Untertitel-Timing:** Whisper-Zeitmarken bevorzugt; sonst YouTube-Auto-Untertitel.

## Meilensteine (Übersicht)
```
◆ M1: Werkzeuge + Quelle + Fundament-Doks    🔄 in Arbeit
│
◆ M2: Ein Befehl → 3–6 Shorts                ⬜ offen
│
◆ M3: Pilot „Berührt sein" freigegeben       ⬜ offen
│
◆ M4: Wöchentliche Routine + GitHub          ⬜ offen
│
◆ M5: Skill nutzbar                          ⬜ offen
```
