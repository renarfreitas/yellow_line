from concurrent.futures import BrokenExecutor
import cv2
import os

USERNAME = 'admin'
PASSWORD = 'admin'
IP = '192.168.1.107'
PORT = '8081'

os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"

URL = '//{}:{}@{}/'.format(USERNAME, PASSWORD, IP, PORT)
print('Conectado com: ' + URL)

cap = cv2.VideoCapture(URL, cv2.CAP_FFMPEG)

while True:
    ret, frame = cap.read()
    if ret == False:
        print("Sem frame")
        break
    else:

        cv2.imshow('VIDEO', frame)
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()