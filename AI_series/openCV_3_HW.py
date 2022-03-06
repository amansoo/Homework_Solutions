import cv2
import numpy as np

cam=cv2.VideoCapture(0)
frame = np.zeros([360, 360], dtype=np.uint8)
frame[:, :] = 255

while True:
    for i in range(0, 5, 2):
        for j in range(0, 5, 2):
            frame[int(360 / 5 * i):int(360 / 5 * i + 72), int(360 / 5) * j:int(360 / 5 * j) + 72] = 0

    for i in range(1, 5, 2):
        for j in range(1, 6, 2):
             frame[int(360 / 5 * i):int(360 / 5 * i + 72), int(360 / 5) * j:int(360 / 5 * j) + 72] = 0

    cv2.imshow("Window 1", frame)
    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
