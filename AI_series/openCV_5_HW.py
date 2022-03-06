import cv2
import numpy
import time

width = 1080
height = 720
cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

row_1 = 320
row_2 = 400

column_1 = 480
column_2 = 600
direction = "forward"

while True:
    ignore,  frame = cam.read()

    frame_roi = frame[row_1:row_2, column_1:column_2]

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)

    frame[row_1:row_2, column_1:column_2] = frame_roi
    cv2.imshow('Window 1', frame)
    cv2.moveWindow('Window 1',0,0)
    
    if direction == "forward":
        row_1 += 80
        row_2 += 80
        column_1 += 120
        column_2 += 120

    if direction == "backward":
        row_1 -= 80
        row_2 -= 80
        column_1 -= 120
        column_2 += 120

    if row_2 >= 720 and column_2 >= 1080:
        direction = "backward"
    elif row_1 <= 0 and column_1 <= 0:
        direction = "forward"
    
    if cv2.waitKey(1) == ord('q'):
        break
    
cam.release()
