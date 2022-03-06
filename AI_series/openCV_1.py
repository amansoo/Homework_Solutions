import cv2

cam = cv2.VideoCapture(0)

while True:
    ignore, frame = cam.read()
    cv2.imshow('Cam', frame)

    if cv2.waitKey(1) == ord('q'):
        break
cam.release()
