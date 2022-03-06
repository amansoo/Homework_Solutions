import cv2

width = 1080
height = 720

rows = int(input("How many rows?\n"))
columns = int(input("How many columns?\n"))

cam=cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    ignore,  frame = cam.read()
    frame = cv2.resize(frame, (int(width / columns), int(height / columns)))
    # cv2.imshow('Window 1', frame)
    # cv2.moveWindow('Window 1', 0, 0)
    for i in range(0, rows):
        for j in range(columns):
            window_name = "Window " + str(i) + "x" + str(j)
            cv2.imshow(window_name, frame)
            cv2.moveWindow(window_name, int(width / columns) * j, int(height / columns) * i)
    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
