import cv2
import numpy

width = 1080
height = 720
x_pos = int(width / 2)
y_pos = int(height / 2)

def on_change(val):
    global x_pos
    print("Trackbar X's value changed to {}".format(val))
    x_pos = val


def on_change2(val):
    global y_pos
    print("Trackbar Y's value changed to {}".format(val))
    y_pos = val


cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

cv2.namedWindow('Trackbar Window')
cv2.resizeWindow('Trackbar Window', 300, 100)
cv2.moveWindow('Trackbar Window', 1080, 0)

cv2.createTrackbar('Trackbar X', 'Trackbar Window', 0, 1080, on_change)
cv2.createTrackbar('Trackbar Y', 'Trackbar Window', 0, 720, on_change2)

while True:
    ignore,  frame = cam.read()
    cv2.circle(frame, (x_pos, y_pos), 25, (255, 0, 0), 2)
    cv2.imshow('Window 1', frame)
    cv2.moveWindow('Window 1',0,0)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
