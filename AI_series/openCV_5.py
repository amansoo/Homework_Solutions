import cv2
import numpy

width = 1080
height = 720
cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    ignore,  frame = cam.read()
    frame_roi = frame[300:420, 480:600]
    frame_roi_gray = cv2.cvtColor(frame_roi, cv2.COLOR_BGR2GRAY)
    frame_roi_bgr_gray = cv2.cvtColor(frame_roi_gray, cv2.COLOR_GRAY2BGR)
    frame[300:420, 480:600] = frame_roi_bgr_gray
    cv2.imshow('Window ROI', frame_roi)
    cv2.moveWindow('Window ROI', 1100, 0)

    cv2.imshow('Window 1', frame)
    cv2.moveWindow('Window 1',0,0)
    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
