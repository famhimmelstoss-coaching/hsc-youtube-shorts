#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
make_ass.py — Stufe [5] CAPTION: erzeugt gebrandete Karaoke-Untertitel (.ass)
aus den Wort-Zeitmarken des Transkript-JSON, für ein Zeitfenster eines Clips.

Untertitel-Stil: weiße Wörter, das gerade gesprochene Wort färbt sich Koralle
(#E0998C) ein (Karaoke \\k). Marken-Outline. Sitzt im unteren Bereich.

Aufruf:
  python make_ass.py TRANSKRIPT.json --from 1367.0 --to 1395.8 --zero 1366.8 --out A.ass

  --from / --to : Quell-Zeitfenster in Sekunden (welche Wörter aufnehmen)
  --zero        : Quell-Zeit, die im Clip = 0 s ist (das -ss des Schnitts)
  Ausgabe-Zeit eines Wortes = Quellzeit - zero.
"""
import argparse, json, sys

# Markenfarben als .ass (&HAABBGGRR)
CORAL = "&H008C99E0"   # #E0998C  -> gesprochen (Primary)
WHITE = "&H00FFFFFF"   # ungesprochen (Secondary)
OUTLINE = "&H00301A0A"  # dunkel, für Lesbarkeit
PLAYRES_X, PLAYRES_Y = 1080, 1920

MAX_WORDS = 4       # Wörter pro Untertitel-Zeile
MAX_DUR   = 1.6     # max. Sekunden pro Zeile
GAP_SPLIT = 0.6     # neue Zeile bei Sprechpause > x s


def cc(t):
    if t < 0: t = 0
    h = int(t // 3600); t -= h*3600
    m = int(t // 60);  t -= m*60
    s = int(t);        c = int(round((t - s)*100))
    if c == 100: s += 1; c = 0
    return f"{h:d}:{m:02d}:{s:02d}.{c:02d}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("json")
    ap.add_argument("--from", dest="t0", type=float, required=True)
    ap.add_argument("--to",   dest="t1", type=float, required=True)
    ap.add_argument("--zero", type=float, default=0.0)
    ap.add_argument("--out",  required=True)
    ap.add_argument("--fontsize", type=int, default=58)
    ap.add_argument("--marginv", type=int, default=210)
    a = ap.parse_args()

    data = json.load(open(a.json, encoding="utf-8"))
    words = []
    for seg in data.get("segments", []):
        for w in seg.get("words", []):
            if w["end"] > a.t0 and w["start"] < a.t1:
                txt = w["word"].strip()
                if txt:
                    words.append((w["start"], w["end"], txt))
    if not words:
        print("WARNUNG: keine Wörter im Fenster gefunden", file=sys.stderr)

    # in Zeilen gruppieren
    lines, cur = [], []
    for w in words:
        if cur:
            dur = w[1] - cur[0][0]
            gap = w[0] - cur[-1][1]
            if len(cur) >= MAX_WORDS or dur > MAX_DUR or gap > GAP_SPLIT:
                lines.append(cur); cur = []
        cur.append(w)
    if cur: lines.append(cur)

    head = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {PLAYRES_X}
PlayResY: {PLAYRES_Y}
WrapStyle: 2
ScaledBorderAndShadow: yes
YCbCr Matrix: TV.709

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: HSC,Arial,{a.fontsize},{CORAL},{WHITE},{OUTLINE},&H64000000,-1,0,0,0,100,100,0,0,1,5,2,2,90,90,{a.marginv},1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    ev = []
    for ln in lines:
        start = ln[0][0]; end = ln[-1][1]
        cursor = start
        parts = []
        for (ws, we, txt) in ln:
            k = max(1, int(round((we - cursor)*100)))
            cursor = we
            parts.append(f"{{\\k{k}}}{txt}")
        text = " ".join(parts)
        ev.append(f"Dialogue: 0,{cc(start - a.zero)},{cc(end - a.zero)},HSC,,0,0,0,,{text}")

    with open(a.out, "w", encoding="utf-8") as f:
        f.write(head + "\n".join(ev) + "\n")
    print(f"OK: {len(lines)} Untertitel-Zeilen -> {a.out}")


if __name__ == "__main__":
    main()
