import cv2
import numpy

width = 640
height = 360
evt = 0
def on_mouse(event, x_pos, y_pos, flags, params):
    global x
    global y
    global evt
    if event == cv2.EVENT_LBUTTONDOWN:
        x = x_pos
        y = y_pos
        evt = event


cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

# Enter code here:
cv2.namedWindow('Window 1')
cv2.setMouseCallback('Window 1', on_mouse)

while True:
    ignore,  frame = cam.read()
    if evt == 1:
        picked = numpy.zeros((250, 250, 3), dtype=numpy.uint8)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        colour = hsv[y][x]
        print(colour)
        picked[:, :] = colour
        hsv = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
        cv2.putText(picked, str(colour), (0, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 1)
        cv2.imshow('Picked Colour', picked)
        cv2.moveWindow('Picked Colour', width, 0)   
        cv2.imshow('HSV', hsv)
        evt = 0
    
    cv2.imshow('Window 1', frame)
    cv2.moveWindow('Window 1',0,0)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
