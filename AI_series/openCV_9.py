import cv2
import numpy as np

width = 640
height = 360
hue_low = 0
hue_high = 179
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


cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
cv2.namedWindow('Trackbars')
cv2.moveWindow('Trackbars', width, 0)

# Enter code here:

cv2.createTrackbar('Hue Low', 'Trackbars', 0, 179, on_change_1)
cv2.createTrackbar('Hue High', 'Trackbars', 179, 179, on_change_2)
cv2.createTrackbar('Sat Low', 'Trackbars', 0, 255, on_change_3)
cv2.createTrackbar('Sat High', 'Trackbars', 255, 255, on_change_4)
cv2.createTrackbar('Val Low', 'Trackbars', 0, 255, on_change_5)
cv2.createTrackbar('Val High', 'Trackbars', 255, 255, on_change_6)

while True:
    ignore,  frame = cam.read()
    frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    low_requists = np.array([hue_low, sat_low, val_low])  # This will define ATLEAST what hue, sat and val the pixel mist have 
                                                          # in order to be taken in.
    upper_requists = np.array([hue_high, sat_high, val_high])  # This will define ATMOST what hue, sat and val the pixel mist have 
                                                               # in order to be taken in.

    my_mask = cv2.inRange(frame_HSV, low_requists, upper_requists)

    object = cv2.bitwise_and(frame, frame, mask=my_mask)
    cv2.imshow('Your Object', object)
    cv2.moveWindow('Your Object', width, height)
    cv2.imshow('Mask', my_mask)
    cv2.moveWindow('Mask', 0, height)
    cv2.imshow('Window 1', frame)
    cv2.moveWindow('Window 1',0,0)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
