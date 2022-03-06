import cv2
import numpy

width = 1080
height = 720

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

# Enter code here:
face_cascade = cv2.CascadeClassifier('C:/Users/amans/Documents/AI_python/haar/haarcascade_frontalface_default.xml')
while True:
    ignore,  frame = cam.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # It is easier to process a gray scale image for faces.
    faces = face_cascade.detectMultiScale(frame_gray, 1.3, 5)

    for face in faces:
        x, y, w, h = face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.imshow('Window 1', frame)
    cv2.moveWindow('Window 1',0,0)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
