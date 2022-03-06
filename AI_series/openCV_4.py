import cv2
import numpy
width = 1089
height = 720

cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    ignore,  frame = cam.read()

    # frame[120:200, 120:200] = [0, 0, 255]
    cv2.putText(frame, "Aman Sood", (30, 40), cv2.FONT_HERSHEY_DUPLEX, 1, [0, 0, 255], 2)
    cv2.imshow('Window 1', frame)
    cv2.moveWindow('Window 1',0,0)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
