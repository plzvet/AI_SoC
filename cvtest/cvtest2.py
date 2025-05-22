import cv2

def nothing(x):
    pass

cv2.namedWindow("Webcam Filter")

cv2.createTrackbar("Mode", "Webcam Filter", 0, 3, nothing)
cv2.createTrackbar("Blur ksize", "Webcam Filter", 1, 20, nothing)
cv2.createTrackbar("Thresh", "Webcam Filter", 127, 255, nothing)
cv2.createTrackbar("Canny Th1", "Webcam Filter", 50, 255, nothing)
cv2.createTrackbar("Canny Th2", "Webcam Filter", 150, 255, nothing)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    mode = cv2.getTrackbarPos("Mode", "Webcam Filter")
    blur_ksize = cv2.getTrackbarPos("Blur ksize", "Webcam Filter")
    thresh_val = cv2.getTrackbarPos("Thresh", "Webcam Filter")
    canny_th1 = cv2.getTrackbarPos("Canny Th1", "Webcam Filter")
    canny_th2 = cv2.getTrackbarPos("Canny Th2", "Webcam Filter")

    output = frame.copy()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if mode == 1:
        k = blur_ksize if blur_ksize % 2 == 1 else blur_ksize + 1
        output = cv2.GaussianBlur(frame, (k, k), 0)
    elif mode == 2:
        _, output = cv2.threshold(gray, thresh_val, 255, cv2.THRESH_BINARY)
        output = cv2.cvtColor(output, cv2.COLOR_GRAY2BGR)
    elif mode == 3:
        edges = cv2.Canny(gray, canny_th1, canny_th2)
        output = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    cv2.imshow("Webcam Filter", output)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
