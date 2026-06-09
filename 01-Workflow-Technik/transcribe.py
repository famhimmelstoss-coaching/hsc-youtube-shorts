#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
transcribe.py — Stufe [2] TRANSCRIBE des Shorts-Workflows.

Transkribiert ein Video/Audio mit faster-whisper (lokal, deutsch) und schreibt:
  - <name>.srt   (Segment-Untertitel, zum Lesen/Prüfen)
  - <name>.txt   (Fließtext)
  - <name>.json  (Segmente MIT Wort-Zeitmarken -> Basis für Karaoke-Untertitel & exakten Schnitt)

Aufruf (Python-Vollpfad nötig, da der Windows-Store-Platzhalter "python" verdeckt):
  & "$env:LOCALAPPDATA\\Programs\\Python\\Python312\\python.exe" transcribe.py "C:\\Pfad\\zum\\Video.mp4" --out "C:\\Pfad\\zu\\02-Quellen-Transkripte"

Optionen:
  --model   large-v3-turbo (Standard, ~5-6x schneller, top DE-Qualität) | large-v3 (Reserve, max. Qualität) | medium
  --out     Zielordner (Standard: Ordner der Eingabedatei)
  --lang    Sprache (Standard: de)
"""
import argparse
import json
import os
import sys
import time


def fmt_ts(seconds: float) -> str:
    """Sekunden -> SRT-Zeitstempel HH:MM:SS,mmm"""
    if seconds < 0:
        seconds = 0
    ms = int(round(seconds * 1000))
    h, ms = divmod(ms, 3600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def main() -> int:
    ap = argparse.ArgumentParser(description="Transkription mit faster-whisper")
    ap.add_argument("input", help="Pfad zu Video- oder Audiodatei")
    ap.add_argument("--out", default=None, help="Zielordner (Standard: Ordner der Eingabe)")
    ap.add_argument("--model", default="large-v3-turbo",
                    help="Whisper-Modell (Standard: large-v3-turbo; Reserve: large-v3)")
    ap.add_argument("--lang", default="de", help="Sprache (Standard de)")
    args = ap.parse_args()

    src = os.path.abspath(args.input)
    if not os.path.isfile(src):
        print(f"FEHLER: Datei nicht gefunden: {src}", file=sys.stderr)
        return 2

    out_dir = os.path.abspath(args.out) if args.out else os.path.dirname(src)
    os.makedirs(out_dir, exist_ok=True)
    base = os.path.splitext(os.path.basename(src))[0]
    srt_path = os.path.join(out_dir, base + ".srt")
    txt_path = os.path.join(out_dir, base + ".txt")
    json_path = os.path.join(out_dir, base + ".json")

    try:
        from faster_whisper import WhisperModel
    except ImportError:
        print("FEHLER: faster-whisper ist nicht installiert "
              "(pip install faster-whisper).", file=sys.stderr)
        return 3

    threads = os.cpu_count() or 4
    print(f"[1/3] Modell laden: {args.model} (CPU, int8, {threads} Threads) ...", flush=True)
    model = WhisperModel(args.model, device="cpu", compute_type="int8", cpu_threads=threads)

    print(f"[2/3] Transkribiere: {os.path.basename(src)} (Sprache={args.lang}) ...", flush=True)
    t0 = time.time()
    segments, info = model.transcribe(
        src,
        language=args.lang,
        word_timestamps=True,
        vad_filter=True,                       # Stille/Pausen herausfiltern
        vad_parameters={"min_silence_duration_ms": 500},
        beam_size=5,
    )
    total = float(getattr(info, "duration", 0) or 0)

    seg_list = []
    with open(srt_path, "w", encoding="utf-8") as fsrt, \
         open(txt_path, "w", encoding="utf-8") as ftxt:
        for i, seg in enumerate(segments, 1):
            text = (seg.text or "").strip()
            words = []
            if seg.words:
                for w in seg.words:
                    words.append({"start": round(w.start, 3),
                                  "end": round(w.end, 3),
                                  "word": w.word})
            seg_list.append({"id": i,
                             "start": round(seg.start, 3),
                             "end": round(seg.end, 3),
                             "text": text,
                             "words": words})
            # SRT
            fsrt.write(f"{i}\n{fmt_ts(seg.start)} --> {fmt_ts(seg.end)}\n{text}\n\n")
            # TXT
            ftxt.write(text + "\n")
            # Fortschritt
            if total:
                pct = min(100, int(seg.end / total * 100))
                print(f"    {fmt_ts(seg.end)} / {fmt_ts(total)}  ({pct}%)", flush=True)

    with open(json_path, "w", encoding="utf-8") as fjson:
        json.dump({"source": src,
                   "language": getattr(info, "language", args.lang),
                   "duration": round(total, 2),
                   "model": args.model,
                   "segments": seg_list},
                  fjson, ensure_ascii=False, indent=2)

    dt = time.time() - t0
    print(f"[3/3] FERTIG in {dt/60:.1f} min — {len(seg_list)} Segmente.", flush=True)
    print(f"  SRT : {srt_path}")
    print(f"  TXT : {txt_path}")
    print(f"  JSON: {json_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
