# Generate the SRT file from the uploaded CSV

import os
import csv
from dotenv import load_dotenv

load_dotenv()

csv_path = os.getenv("CSV_FILE", "")
fps = 29.996455224836243
duration = 0.8

rows = []
with open(csv_path, "r") as f:
    reader = csv.DictReader(f)
    for r in reader:
        rows.append((int(r["pushup_number"]), int(r["frame"])))


def frame_to_time(frame):
    t = frame / fps
    h = int(t // 3600)
    m = int((t % 3600) // 60)
    s = int(t % 60)
    ms = int((t - int(t)) * 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def frame_to_time_with_offset(frame, offset):
    t = frame / fps + offset
    h = int(t // 3600)
    m = int((t % 3600) // 60)
    s = int(t % 60)
    ms = int((t - int(t)) * 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


srt_lines = []

for idx, frame in rows:
    start = frame_to_time(frame)
    end = frame_to_time_with_offset(frame, duration)

    srt_lines.append(str(idx))
    srt_lines.append(f"{start} --> {end}")
    srt_lines.append(f"{idx}")
    srt_lines.append("")

srt_content = "\n".join(srt_lines) + "\n\n"  # For safer inclusion of all srt codes

out_path = os.getenv("SRT_FILE", "")
with open(out_path, "w") as f:
    f.write(srt_content)
