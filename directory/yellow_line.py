import cv2
cap = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eyesCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
smileCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

while True:
    _, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor = 1.1,
        minNeighbors = 5,
        minSize = (30, 30)
    )

    #Face detection
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
    
    #Eyes detection
    eyes = eyesCascade.detectMultiScale(gray, 1.2, 18)
    for (x, y, w, h) in eyes:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)

    #Smiles
    smiles = smileCascade.detectMultiScale(gray, 1.7, 20)
    for (x, y, w, h) in smiles:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 0, 255), 2)

    cv2.imshow("video", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()