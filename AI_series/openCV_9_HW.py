import cv2
import numpy as np

width = 640
height = 360
hue_low = 0
hue_high = 179
hue_low_2 = 0
hue_high_2 = 179
sat_low = 0
sat_high = 255
val_low = 0
val_high = 255


def on_change_1(val):
    global hue_low
    hue_low = val


def on_change_2(val):
    global hue_high
    hue_high = val


def on_change_3(val):
    global sat_low
    sat_low = val


def on_change_4(val):
    global sat_high
    sat_high = val


def on_change_5(val):
    global val_low
    val_low = val

    
def on_change_6(val):
    global val_high
    val_high = val


def on_change_7(val):
    global hue_low_2
    hue_low_2 = val


def on_change_8(val):
    global hue_high_2
    hue_high_2 = val


cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
cv2.namedWindow('Trackbars')
cv2.moveWindow('Trackbars', width, 0)
cv2.resizeWindow('Trackbars', 360, 360)
# Enter code here:

cv2.createTrackbar('Hue Low', 'Trackbars', 0, 179, on_change_1)
cv2.createTrackbar('Hue High', 'Trackbars', 179, 179, on_change_2)
cv2.createTrackbar('Sat Low', 'Trackbars', 0, 255, on_change_3)
cv2.createTrackbar('Sat High', 'Trackbars', 255, 255, on_change_4)
cv2.createTrackbar('Val Low', 'Trackbars', 0, 255, on_change_5)
cv2.createTrackbar('Val High', 'Trackbars', 255, 255, on_change_6)

cv2.createTrackbar('Hue Low 2', 'Trackbars', 0, 179, on_change_7)
cv2.createTrackbar('Hue High 2', 'Trackbars', 179, 179, on_change_8)

while True:
    ignore,  frame = cam.read()
    frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    low_requists = np.array([hue_low, sat_low, val_low])  # This will define ATLEAST what hue, sat and val the pixel must have 
                                                          # in order to be taken in.
    low_requists_2 = np.array([hue_low_2, sat_low, val_low])

    upper_requists = np.array([hue_high, sat_high, val_high])  # This will define ATMOST what hue, sat and val the pixel must have 
                                                               # in order to be taken in.
    upper_requists_2 = np.array([hue_high_2, sat_high, val_high])

    my_mask = cv2.inRange(frame_HSV, low_requists, upper_requists)
    my_mask2 = cv2.inRange(frame_HSV, low_requists_2, upper_requists_2)
    my_masks = cv2.add(my_mask, my_mask2)
    object = cv2.bitwise_and(frame, frame, mask=my_masks)

    cv2.imshow('Your Object', object)
    cv2.moveWindow('Your Object', 0, height)
    cv2.imshow('Window 1', frame)
    cv2.moveWindow('Window 1',0,0)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
