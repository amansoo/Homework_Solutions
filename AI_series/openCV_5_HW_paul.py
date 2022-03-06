import cv2

width = 1260
height = 720

box_width = 120
box_height = 60

box_center_row = int(height / 2)
box_center_column = int(width / 2)

iteration_width = 1
iteration_height = 1

cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    ignore,  frame = cam.read()
    
    frame_ROI = frame[int(box_center_row - box_height / 2):int(box_center_row + box_height / 2), 
    int(box_center_column - box_width / 2):int(box_center_column + box_width / 2)]

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)

    frame[int(box_center_row - box_height / 2):int(box_center_row + box_height / 2), 
    int(box_center_column - box_width / 2):int(box_center_column + box_width / 2)] = frame_ROI

    if int(box_center_row + box_height / 2) >= height or int(box_center_row - box_height / 2) <= 0:
        iteration_height *= -1
    if int(box_center_column + box_width / 2) >= width or int(box_center_column - box_width / 2) <= 0:
        iteration_width *= (-1)

    box_center_row += iteration_height
    box_center_column += iteration_width

    cv2.imshow('Window 1', frame)
    cv2.moveWindow('Window 1',0,0)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
