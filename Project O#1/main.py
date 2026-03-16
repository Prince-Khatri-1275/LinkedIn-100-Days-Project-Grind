import cv2
import os
from dotenv import load_dotenv
import csv

load_dotenv()

VIDEO_PATH:str = os.getenv("VIDEO_PATH", "")
SCALE:float = float(os.getenv("SCALE", 1.0))
OUTPUT_FILE:str = os.getenv("CSV_FILE", "")

cap = cv2.VideoCapture(VIDEO_PATH)

if not cap.isOpened():
    print("Error opening video.")
    exit()

fps = cap.get(cv2.CAP_PROP_FPS)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

print("FPS:", fps)
print("Total Frames:", total_frames)

frame_no = 0
paused = False
pushup_frames = []

while True:

    if not paused:
        ret, frame = cap.read()
        if not ret:
            break
        frame_no += 1
    else:
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_no)
        ret, frame = cap.read()

    if SCALE != 1.0:
        frame = cv2.resize(frame, None, fx=SCALE, fy=SCALE)

    info = f"Frame: {frame_no}/{total_frames} | Pushups: {len(pushup_frames)}"
    status = "PAUSED" if paused else "PLAYING"

    cv2.putText(frame, info, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    cv2.putText(
        frame, status, (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255), 2
    )

    cv2.imshow("Pushup Labeler", frame)

    key = cv2.waitKey(30) & 0xFF

    if key == ord("k"):
        pushup_frames.append(frame_no)
        print(f"Pushup marked at frame {frame_no}")

    elif key == ord("u"):
        if pushup_frames:
            removed = pushup_frames.pop()
            print(f"Removed pushup at frame {removed}")

    elif key == ord(" "):
        paused = not paused
        print("Paused" if paused else "Playing")

    elif key == ord("d") and paused:
        frame_no = min(frame_no + 1, total_frames - 1)

    elif key == ord("a") and paused:
        frame_no = max(frame_no - 1, 0)

    elif key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

print("Saving results...")

os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

with open(OUTPUT_FILE, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["pushup_number", "frame"])
    for i, frame in enumerate(pushup_frames, 1):
        writer.writerow([i, frame])

print("Saved to:", OUTPUT_FILE)
