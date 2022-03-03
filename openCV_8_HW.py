import cv2
import numpy

width = 1080
height = 720


# Enter code here:
saturation = 255
frame_sat = numpy.zeros((256, 720, 3), dtype=numpy.uint8)
frame_val = numpy.zeros((256, 720, 3), dtype=numpy.uint8)

for i in range(0, 255):
    for j in range(0, 719):
        frame_sat[i:i + 1, j:j + 1] = [int(j / 4), i, 255]

for i in range(0, 255):
    for j in range(0, 719):
        frame_val[i:i + 1, j:j + 1] = [int(j / 4), 255, i]

frame_sat = cv2.cvtColor(frame_sat, cv2.COLOR_HSV2BGR)
frame_val = cv2.cvtColor(frame_val, cv2.COLOR_HSV2BGR)
while True:
    cv2.imshow('Window 1', frame_sat)
    cv2.moveWindow('Window 1', 0, 0)

    cv2.imshow('Window 2', frame_val)
    cv2.moveWindow('Window 2', 0, 300)
    if cv2.waitKey(1) == ord('q'):
        break
