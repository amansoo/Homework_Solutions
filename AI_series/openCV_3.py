import cv2
import numpy as np

cam=cv2.VideoCapture(0)

while True:
    frame = np.zeros([360, 720, 3], dtype=np.uint8)
    frame[:, :] = [255, 0 , 255]
    cv2.imshow("Window 1", frame)
    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
