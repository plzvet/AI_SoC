import cv2
import torch
import numpy as np
import os
from glob import glob
from datetime import datetime

model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
model.eval()

SAVE_DIR = "person_captures"
os.makedirs(SAVE_DIR, exist_ok=True)

def detect_and_show_static(img_path):
    img = cv2.imread(img_path)
    if img is None:
        print(f"Failed to load {img_path}")
        return

    window = 'Image Detection'
    cv2.namedWindow(window)
    cv2.createTrackbar('Confidence %', window, 50, 100, lambda x: None)

    while True:
        thresh = cv2.getTrackbarPos('Confidence %', window) / 100.0
        model.conf = thresh
        results = model(img)

        display = img.copy()
        for *box, conf, cls in results.xyxy[0].cpu().numpy():
            x1, y1, x2, y2 = map(int, box)
            label = f"{model.names[int(cls)]}: {conf:.2f}"
            color = (0, 255, 0) if int(cls) == 0 else (255, 0, 0)
            cv2.rectangle(display, (x1, y1), (x2, y2), color, 2)
            cv2.putText(display, label, (x1, y1 - 5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

        cv2.imshow(window, display)
        key = cv2.waitKey(30) & 0xFF
        if key in (27, ord('n')):
            break

    cv2.destroyWindow(window)

img_files = glob(os.path.expanduser('~/Pictures/*.[jp][pn]g'))
for img_path in img_files:
    print("Showing:", img_path)
    detect_and_show_static(img_path)

def webcam_detection():
    window = 'WebCam Detection'
    cv2.namedWindow(window)
    cv2.createTrackbar('Confidence %', window, 50, 100, lambda x: None)

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Webcam open failed")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        thresh = cv2.getTrackbarPos('Confidence %', window) / 100.0
        model.conf = thresh

        results = model(frame)
        detections = results.xyxy[0].cpu().numpy()

        person_detected = False
        for x1, y1, x2, y2, conf, cls in detections:
            cls = int(cls)
            label = f"{model.names[cls]}: {conf:.2f}"
            color = (255, 0, 0)
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), color, 2)
            cv2.putText(frame, label, (int(x1), int(y1) - 5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

            if cls == 0:
                person_detected = True

        if person_detected:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
            save_path = os.path.join(SAVE_DIR, f"person_{timestamp}.jpg")
            cv2.imwrite(save_path, frame)
            print(f"??? Person detected! Saved to {save_path}")

        cv2.imshow(window, frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

webcam_detection()
