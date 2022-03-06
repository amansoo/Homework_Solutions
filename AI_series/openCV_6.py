import cv2
import numpy

def on_mouse(event, x_pos, y_pos, flags, params):
    global evt
    global pnt
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Left button clicked, did it at " + str(x_pos) + "x and " + str(y_pos) + "y")
        evt = event  # So that we know the integer value of the event, 
                    # we simply can't use the event variable since its scope is the function
        pnt = (x_pos, y_pos)
    if event == cv2.EVENT_LBUTTONUP:
        print("Left button let go, did it at " + str(x_pos) + "x and " + str(y_pos) + "y")
        evt = event
        pnt = (x_pos, y_pos)


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
mouse_clicks = 0
while True:
    ignore,  frame = cam.read()
    if evt == 1:  # Comparing it to 1 because that is the value assiciated with left button down
        cv2.circle(frame, pnt, 25, (255, 0, 0), 2)
        mouse_clicks += 1
        evt = 0
    elif evt == 4:
        cv2.circle(frame, pnt, 25, (0, 0, 255), 2)
    cv2.rectangle(frame, (0, 0), (250, 50), (0, 255, 0), -1)
    cv2.putText(frame, "Mouse Clicks: {}".format(mouse_clicks), (0, 20), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 0), 2)
    cv2.imshow('Window 1', frame)
    cv2.moveWindow('Window 1',0,0)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
