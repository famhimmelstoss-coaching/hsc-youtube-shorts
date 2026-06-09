# A — Projektbeschreibung: YouTube-Shorts aus dem Sonntagsgespräch (V01)

**Stand:** 2026-06-09

## Kurzübersicht
**Was:** Ein wiederholbarer Workflow, der aus jedem wöchentlichen **Sonntagsgespräch** (≈ 60 Min, A&H = Annette & Herbert, live über StreamYard auf den YouTube-Kanal gestreamt) mehrere **Shorts** (vertikal, 9:16) erstellt — die stärksten, berührendsten Momente, **inhaltlich ausgewählt**, mit sauberen Untertiteln und A&H-Branding.

**Für wen:** Die Zielgruppe des Kanals — Menschen, die persönliche Entwicklung, Berührtsein, echtes Leben suchen (HSC-Klientel). Shorts sollen neue Zuschauer auf den Kanal und in die Sonntagsgespräche ziehen.

**Warum:** Die KI-Clips von StreamYard sind „nicht überzeugend" (mechanische Auswahl, generische Untertitel, schwache Hooks). Ziel: Clips, bei denen die Zielgruppe denkt „Das will ich sehen — wer ist das?" statt „nett, scrolle weiter".

## Das Problem mit den StreamYard-KI-Clips (Ausgangslage)
- Auswahl nach Audio-Energie / „Viralität", nicht nach Sinn & emotionalem Bogen.
- Hook in den ersten 1–2 Sekunden fehlt oft → Leute scrollen weg.
- Untertitel-Stil generisch, kein Marken-Look (Farben #14507D / #E0998C, Logo).
- Framing/Crop teils unruhig.
- Limitiert: nur 6 Neu-Generierungen pro Video.

Beispiel-Titel der bisherigen StreamYard-Clips zum „Berührt sein"-Gespräch (als Referenz, was thematisch erkannt wurde):
- „Als unser Hund Sternchen starb — Dankbarkeit statt Trauma" (1:07)
- „Wie Entschleunigung das Kochen verwandelt"
- „Gänsehaut beim Lesen: Alte Klöster riefen Erinnerung"
- „Berührtsein macht lebendig: Annette vor Verletzlichkeit"

→ Die Themen sind brauchbar, die **Umsetzung** ist das Problem. Genau da setzen wir an.

## Zielzustand (woran wir Erfolg messen)
1. Pro Sonntagsgespräch **3–6 fertige Shorts**, ohne dass Annette etwas schneiden muss.
2. Jeder Short: starker Hook in Sekunde 1, klarer emotionaler/inhaltlicher Bogen, lesbare gebrandete Untertitel, sauberes 9:16-Framing.
3. Mitgelieferter Text-Block pro Short: Titel, Beschreibung, Hashtags (YouTube Shorts; optional Reels/TikTok).
4. Reproduzierbar als Script → Christian kann es auf GitHub übernehmen/warten.

## Beteiligte & Rollen
- **Annette** — Inhalt, Freigabe, Stimme/Gesicht.
- **Herbert** — zweite Stimme im Gespräch.
- **Christian Seitz** — Technik, übernimmt Script später via GitHub.
- **Claude** — Transkript holen, Momente nach Sinn auswählen, schneiden (ffmpeg), Untertitel + Branding, Textbausteine.

## Quelle & Plattform (entschieden — siehe F)
- **Aufnahme-Quelle:** ✅ **StreamYard-Originalaufnahme** (beste Qualität, kein YouTube-Re-Encode). Download manuell über die StreamYard-Bibliothek (keine API). YouTube/yt-dlp bleibt als automatisierbarer Fallback für die spätere Routine.
- **StreamYard:** keine öffentliche API → keine Programm-Anbindung, keine automatische Verbesserung „von innen". Wir bauen außen herum.
- **Veröffentlichung:** ✅ **Nur YouTube Shorts.** Instagram Reels / TikTok bewusst gestrichen — volle Energie auf einen Kanal. Format (9:16) bliebe kompatibel, falls man später doch erweitert.

## Technik / Setup
- **Windows.** Vorhanden: `git` ✅.
- **Zu installieren:** `yt-dlp` (Download + Untertitel), `ffmpeg` (Schnitt), optional `python` + Whisper (präzises deutsches Transkript mit Zeitmarken).
- **Transkript-Wege:** YouTube-Auto-Untertitel (schnell) ODER Whisper lokal (genauer, besonders bei Namen/Fachwörtern).
- **Schnitt:** ffmpeg — Zuschnitt auf Zeitfenster, Crop/Scale auf 9:16, Untertitel einbrennen, Logo/Marken-Look.

## Stil-Vorgaben (Default — in B verfeinerbar)
- Format **9:16 vertikal**, Länge **20–60 Sek** pro Short.
- **Hook zuerst:** der stärkste Satz/Moment in Sekunde 1.
- **Untertitel eingebrannt**, gut lesbar, Markenfarben #14507D / #E0998C, dezentes A&H-Logo.
- Auswahl **nach Sinn**: berührende Momente, klare Aussagen, kleine Geschichten mit Anfang–Mitte–Ende.
- **Keine Marketing-Floskeln** in Titeln/Texten (vgl. [[feedback_anti_floskeln]]).

## Format & Umfang pro Folge
- 1 Quellvideo (~60 Min) → 3–6 Shorts à 20–60 Sek + je ein Textblock (Titel/Beschreibung/Hashtags).

## Zeitrahmen
- Wöchentlich (Sonntagsgespräch). Erst **ein Pilot** mit dem „Berührt sein"-Gespräch (7. Juni 2026), dann Routine.

## Zugangsdaten / Quellen
- StreamYard-Bibliothek: im Chrome-Profil eingeloggt (Konto „K"). Video „Berührt sein – ein Wegweiser zu deinen innersten Sehnsüchten", 7. Juni 2026.
- YouTube-Kanal: _Link nachtragen._
- Logo lokal: `.claude\assets\Himmelstoss_Logo.png` · [[reference_logo]]

## Nächste Schritte
1. Werkzeuge installieren (yt-dlp, ffmpeg, ggf. Whisper).
2. Quelle festlegen (StreamYard-Download vs. YouTube).
3. Pilot „Berührt sein": Transkript → Momentauswahl → 3–6 Shorts → Freigabe durch Annette.
4. Workflow als Script festhalten, GitHub-Repo für Christian vorbereiten.
