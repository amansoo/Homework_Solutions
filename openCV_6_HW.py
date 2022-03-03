import cv2
import numpy

def on_mouse(event, x_pos, y_pos, flags, params):
    global evt
    global row_1
    global row_2
    global column_1
    global column_2
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Left button clicked, did it at " + str(x_pos) + "x and " + str(y_pos) + "y")
        evt = event # So that we know the integer value of the event, 
                    # we simply can't use the event variable since its scope is the function
        row_1 = y_pos
        column_1 = x_pos
    if event == cv2.EVENT_LBUTTONUP:
        print("Left button let go, did it at " + str(x_pos) + "x and " + str(y_pos) + "y")
        evt = event
        row_2 = y_pos
        column_2 = x_pos
    if event == cv2.EVENT_RBUTTONDOWN:
        evt = event
        print("Button Clicked, event number: {}".format(event))


width = 1080
height = 720
evt = 0

cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

cv2.namedWindow('Window 1')
cv2.setMouseCallback('Window 1', on_mouse)
while True:
    ignore,  frame = cam.read()
    if evt == 4:
        frame_roi = frame[row_1:row_2, column_1:column_2]
        cv2.imshow("Window 2", frame_roi)
        cv2.moveWindow("Window 2", 1100, 0)
    elif evt == 2:
        cv2.destroyWindow("Window 2")
        evt = 0

    cv2.imshow('Window 1', frame)
    cv2.moveWindow('Window 1',0,0)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
