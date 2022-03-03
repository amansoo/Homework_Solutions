import cv2
import numpy
import time

width = 1080
height = 720

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

# Enter code here:
face_cascade = cv2.CascadeClassifier('C:/Users/amans/Documents/AI_python/haar/haarcascade_frontalface_default.xml')  # Load the
# pretrained face detection model
eye_cascade = cv2.CascadeClassifier('haar/haarcascade_eye.xml')
old = time.time()
time.sleep(0.1)
new = time.time()

while True:
    process_time = new - old
    fps = int(1 / process_time)
    old = time.time()
    ignore,  frame = cam.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # It is easier to process a gray scale image for faces.
    faces = face_cascade.detectMultiScale(frame_gray, 1.3, 5)

    cv2.rectangle(frame, (0, 0), (100, 30), (0, 255, 0), -1)
    cv2.putText(frame, 'FPS: {}'.format(fps), (0, 30), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 1)

    for face in faces:
        x, y, w, h = face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        frame_ROI_gray = frame_gray[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(frame_ROI_gray)
        for (x_2, y_2, w_2, h_2) in eyes:
            cv2.rectangle(frame[y:y + h, x:x + w], (x_2, y_2), (x_2 + w_2, y_2 + h_2), (0, 0, 255), 1)

    cv2.imshow('Window 1', frame)
    cv2.moveWindow('Window 1',0,0)

    if cv2.waitKey(1) == ord('q'):
        break
    new = time.time()

cam.release()
