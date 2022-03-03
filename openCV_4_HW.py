import time
import cv2
import numpy
width = 1080
height = 720
cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 60)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
time_last = time.time()

time.sleep(0.1)
while True:
    time_taken = time.time() - time_last
    time_last = time.time()
    fps = int(1 / time_taken)
    ignore,  frame = cam.read()
    cv2.rectangle(frame, (0, 4), (150, 45), (0, 0, 255), -1)
    cv2.putText(frame, f"FPS: {fps}", (0, 30), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('Window 1', frame)
    cv2.moveWindow('Window 1',0,0)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
