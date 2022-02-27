import cv2
import mediapipe

# Please don't change these variables
width = 1260
height = 720

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
width += 20
# Enter code here:
def faces_mesh_landmarks(frame):
    """Returns an array with all the landmarks for individual faces. Data structure: [[landmark, landmark], [landmark]]"""
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    multi_face_meshes_class = face_mesh_analyser.process(frameRGB)
    multi_faces_meshes = []
    if multi_face_meshes_class.multi_face_landmarks:

        for single_face_mesh in multi_face_meshes_class.multi_face_landmarks:
            single_face_landmarks = []
            # drawing_object.draw_landmarks(frame, single_face_mesh, mediapipe.solutions.face_mesh.FACE_CONNECTIONS, 
            # draw_spec_circle, draw_spec_line)  # Circle spec is specified first, after the line spec.
            for landmark in single_face_mesh.landmark:  # single_mesh_landmark has 468 landmarks!
                # cv2.circle(frame, (int(landmark.x * width), int(landmark.y * height)), 1, (255, 0, 0), thickness=2)
                # cv2.putText(frame, str(counter), (int(landmark.x * width), int(landmark.y * height)), font, .4, (0, 0, 255), 1)
                x_normal = int(landmark.x * width)
                y_normal = int(landmark.y * height)
                single_face_landmarks.append((x_normal, y_normal))
            multi_faces_meshes.append(single_face_landmarks)
    return multi_faces_meshes

font = cv2.FONT_HERSHEY_COMPLEX_SMALL
face_mesh_analyser = mediapipe.solutions.face_mesh.FaceMesh(False, 1, .5, .5)
drawing_object = mediapipe.solutions.drawing_utils
draw_spec_circle = drawing_object.DrawingSpec(thickness = 0, circle_radius = 0, color = (255, 255, 255))
draw_spec_line = drawing_object.DrawingSpec(thickness = 3, circle_radius = 2, color = (0, 0, 255))  # We specify the circle_rad
# even though there will be no circles in a line because this is a, 'style' and we ust specify everything.
while True:
    ignore,  frame = cam.read()
    multi_faces_meshes = faces_mesh_landmarks(frame=frame)
    for single_face_mesh in multi_faces_meshes:
        cv2.rectangle(frame, single_face_mesh[70], single_face_mesh[340], (0, 255, 0), 2)  # Makes a green box around 
        # both the eyes
    cv2.imshow('Window 1', frame)
    cv2.moveWindow('Window 1',0,0)
    if cv2.waitKey(1) == ord('q'):
        break
    
cam.release()
