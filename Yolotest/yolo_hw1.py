import cv2
import torch
import numpy as np
import os
from glob import glob

# Load YOLOv5s model (pretrained)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
model.eval()

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
            cv2.rectangle(display, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(display, label, (x1, y1 - 5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

        cv2.imshow(window, display)
        key = cv2.waitKey(30) & 0xFF
        if key == 27:  # ESC
            break
        elif key == ord('n'):
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

        for *box, conf, cls in results.xyxy[0].cpu().numpy():
            x1, y1, x2, y2 = map(int, box)
            label = f"{model.names[int(cls)]}: {conf:.2f}"
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
            cv2.putText(frame, label, (x1, y1 - 5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)

        cv2.imshow(window, frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

webcam_detection()
