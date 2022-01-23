import cv2

cap = cv2.VideoCapture()

while True:
    _, frame = cap.read()

    cv2.imshow("detections", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()