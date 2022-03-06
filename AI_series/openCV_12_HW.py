import cv2
import face_recognition as recog
import numpy

width = 640
height = 360

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

# Enter code here:
face_aman = recog.load_image_file('C:/Users/amans/Documents/AI_python/WIN_20220216_20_50_01_Pro.jpg')
face_locas = recog.face_locations(face_aman)[0]
face_encodings = recog.face_encodings(face_aman)[0]

while True:
    ignore,  frame = cam.read()
    unknown_face = frame
    unkown_faces_locas = recog.face_locations(unknown_face)
    print(unkown_faces_locas)
    unknown_face_encodings = recog.face_encodings(unknown_face)
    if unkown_faces_locas:
        match = recog.compare_faces([face_encodings], unknown_face_encodings[0])
        if True in match:
            top, right, bottom, left = unkown_faces_locas[0]
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.putText(frame, 'Aman Sood', (left, top), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255), 2)
    cv2.imshow('Window 1', frame)
    cv2.moveWindow('Window 1',0,0)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
