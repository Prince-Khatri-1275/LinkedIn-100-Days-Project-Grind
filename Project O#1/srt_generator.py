import os
import csv
import cv2
from dotenv import load_dotenv

load_dotenv()

csv_path = os.getenv("CSV_FILE_PATH")
video_path = os.getenv("VIDEO_PATH")
srt_path = os.getenv("SRT_FILE_PATH")

duration = 0.8  # subtitle duration


if not csv_path or not video_path or not srt_path:
    raise ValueError("CSV_FILE, VIDEO_FILE, and SRT_FILE must be set in .env")


# ---------------------------
# Get video metadata
# ---------------------------

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    raise RuntimeError("Could not open video.")

fps = cap.get(cv2.CAP_PROP_FPS)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

video_duration = total_frames / fps

cap.release()


# ---------------------------
# Read CSV
# ---------------------------

rows = []

with open(csv_path, "r", newline="") as f:
    reader = csv.DictReader(f)

    for r in reader:
        rows.append((int(r["pushup_number"]), int(r["frame"])))


# ---------------------------
# Time conversion
# ---------------------------


def frame_to_srt_time(frame):

    t = frame / fps

    h = int(t // 3600)
    m = int((t % 3600) // 60)
    s = int(t % 60)
    ms = int(round((t - int(t)) * 1000))

    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def frame_to_srt_time_offset(frame, offset):

    t = frame / fps + offset

    # prevent subtitle from exceeding video length
    t = min(t, video_duration - 0.01)

    h = int(t // 3600)
    m = int((t % 3600) // 60)
    s = int(t % 60)
    ms = int(round((t - int(t)) * 1000))

    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


# ---------------------------
# Build SRT
# ---------------------------

srt_lines = []

for idx, frame in rows:

    start = frame_to_srt_time(frame)
    end = frame_to_srt_time_offset(frame, duration)

    srt_lines.append(str(idx))
    srt_lines.append(f"{start} --> {end}")
    srt_lines.append(str(idx))
    srt_lines.append("")


srt_content = "\n".join(srt_lines) + "\n\n"


# ---------------------------
# Save file
# ---------------------------

with open(srt_path, "w", encoding="utf-8") as f:
    f.write(srt_content)


print("SRT generated successfully")
print("Video FPS:", fps)
print("Total Frames:", total_frames)
print("Pushups:", len(rows))
print("Saved to:", srt_path)
