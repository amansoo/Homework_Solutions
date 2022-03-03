import cv2
cam = cv2.VideoCapture(0)

while True:
    ignore, frame = cam.read()
    # First window
    cv2.imshow("Window 1", frame)
    cv2.moveWindow("Window 1", 0, 0)

    cv2.imshow("Window 2", frame)
    cv2.moveWindow("Window 2", 950, 400)

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Window 3", gray_frame)
    cv2.moveWindow("Window 3", 950, 0)

    cv2.imshow("Window 4", gray_frame)
    cv2.moveWindow("Window 4", 0, 400)

    if cv2.waitKey(1) == ord("q"):
        break
