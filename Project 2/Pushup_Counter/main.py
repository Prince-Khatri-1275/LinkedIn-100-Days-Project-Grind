import os
import cv2
from dotenv import load_dotenv
import mediapipe as mp

mp_pose = mp.solutions.pose # type: ignore
mp_drawings = mp.solutions.drawing_utils # type: ignore

pose = mp_pose.Pose(
    model_complexity=1,
    min_detection_confidence=0.6,
    min_tracking_confidence=0.6
)

load_dotenv()
VIDEO_PATH = os.environ["VIDEO_PATH"]

vid = cv2.VideoCapture(VIDEO_PATH)
running = True

def scale_down(fragment, scaling_factor=0.25):
    h, w, _ = fragment.shape
    new_dims = int(w*scaling_factor), int(h*scaling_factor)
    return cv2.resize(fragment, new_dims)

i = 0
while vid.isOpened() and running:
    i += 1
    
    if i%5:
        continue
    
    ret, frame = vid.read()
    
    if not ret:
        continue
    
    img = scale_down(frame, scaling_factor=0.2)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    results = pose.process(img_rgb)
    if results.pose_landmarks:
        mp_drawings.draw_landmarks(
            img,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS
        )
    
    cv2.imshow("Video", img)
    # print(i)
    
    key = cv2.waitKey(1)
    
    if key == ord("q"):
        running = False

cv2.destroyAllWindows()
vid.release()
