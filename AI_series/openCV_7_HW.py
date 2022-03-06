import cv2
import numpy

width = 1280
height = 720
x_pos = 0
y_pos = 0




def on_change(val):
    global x_pos
    print("Trackbar X's value changed to {}".format(val))
    x_pos = val

def on_change2(val):
    global y_pos
    print("Trackbar Y's value changed to {}".format(val))
    y_pos = val


def on_change3(val):
    width = val
    height = int((width * 9) / 16)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

cv2.namedWindow('Trackbar Window')
cv2.resizeWindow('Trackbar Window', 400, 200)  #TODO: Try to delete.
cv2.moveWindow('Trackbar Window', 1080, 0)

cv2.createTrackbar('Trackbar X', 'Trackbar Window', 0, 567, on_change)
cv2.createTrackbar('Trackbar Y', 'Trackbar Window', 0, 238, on_change2)
cv2.createTrackbar('Trackbar Size', 'Trackbar Window', width, 1920, on_change3)
while True:
    ignore,  frame = cam.read()

    cv2.imshow('Window 1', frame)
    cv2.moveWindow('Window 1', x_pos, y_pos)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows
