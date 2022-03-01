import cv2
import numpy
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
def face_rec(frame) -> list:
    """Returns with a box around the face"""
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    faces_class = face_detection_analyser_mp.process(frameRGB)
    faces_location = []
    if faces_class.detections:
        for face in faces_class.detections:
            face_location = []
            # print(faces.detections)
            top_left = (int(face.location_data.relative_bounding_box.xmin * width), 
            int(face.location_data.relative_bounding_box.ymin * height))
            bottom_right = (int((face.location_data.relative_bounding_box.xmin + face.location_data.relative_bounding_box.width) * width),
            int((face.location_data.relative_bounding_box.ymin + face.location_data.relative_bounding_box.height) * height))

            face_location.append(top_left)
            face_location.append(bottom_right)
            # cv2.rectangle(frame, top_left, bottom_right, (0, 0, 255), 2)
            faces_location.append(face_location)
    return faces_location


def return_pose_landmarks(frame) -> list:
    """This function takes a frame, processes it (in RGB), finds all the landmarks in it and appends them to a list 
    which resets every frame"""
    my_landmarks = []
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Because mediapipe works in RGB.
    pose_landmarks_class = pose_analyser.process(frameRGB)
    if pose_landmarks_class.pose_landmarks:
        # print(pose_landmarks_class.pose_landmarks)
        for landmark in pose_landmarks_class.pose_landmarks.landmark:  # pose_landmarks_class.pose_landmarks.landmark has
            # all the landmarks in an array, so we iterate over individual landmark(s).
            my_landmarks.append((int(landmark.x * (width)), int(landmark.y * height)))
    return my_landmarks


def get_my_hands(frame):
    """Return an array with multi_hand_landmarks. A bit like this: [[(x, y), (x2, y2)], [(x, y), (x, y)]
    Also returns handedness of each hand)"""
    my_hands = []
    hands_handedness = []
    frame_RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Mediapipe works with RGB
    multi_hands_landmarks_class = hands_analyser.process(frame_RGB)  # Tries to finds hands and saves the complicated 
    # array in variable.
    if multi_hands_landmarks_class.multi_hand_landmarks:  # Breaks the data set in a simple 21 landmarks for each hand.
        for hand_handedness in multi_hands_landmarks_class.multi_handedness:  # .multi_handedness returns a nested array with two
            # items, one for each type of hand and related information
            hand_handedness = hand_handedness.classification[0].label
            hands_handedness.append(hand_handedness)

        for single_hand_landmarks in multi_hands_landmarks_class.multi_hand_landmarks:
            my_hand = []
            for single_landmark in single_hand_landmarks.landmark:
                x_normal = int(single_landmark.x * width)
                y_normal = int(single_landmark.y * height)
                cv2.circle(frame, (x_normal, y_normal), 15, (255, 0, 0), -1)
                my_hand.append((x_normal, y_normal))  # Resets every hand iteration
            my_hands.append(my_hand)
    return my_hands, hands_handedness


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


face_mesh_analyser = mediapipe.solutions.face_mesh.FaceMesh(False, 1, .5, .5)
drawing_object = mediapipe.solutions.drawing_utils
draw_spec_circle = drawing_object.DrawingSpec(thickness=0, circle_radius=2, color=(0, 255, 0))
draw_spec_line = drawing_object.DrawingSpec(thickness = 2, color=(255, 0, 0))
face_detection_analyser_mp = mediapipe.solutions.face_detection.FaceDetection()
pose_analyser = mediapipe.solutions.pose.Pose(False, False, True, .5, .5)
hands_analyser = mediapipe.solutions.hands.Hands(False, 2, .5, .5)
while True:
    ignore,  frame = cam.read()
    my_hands, hands_handedness = get_my_hands(frame)
    identified_gesture = 'Unknown'
    if my_hands:
        for hand_landmarks in my_hands:
            if hand_landmarks[8][1] < hand_landmarks[12][1] and hand_landmarks[8][1] < hand_landmarks[16][1]:
                if hand_landmarks[8][0] > hand_landmarks[12][0] and hand_landmarks[8][0] > hand_landmarks[16][0]:
                    if hand_landmarks[20][1] < hand_landmarks[12][1] and hand_landmarks[20][1] < hand_landmarks[16][1]:
                        if hand_landmarks[20][0] < hand_landmarks[12][0] and hand_landmarks[20][1] < hand_landmarks[16][0]:
                            identified_gesture = 'Hook m Horns'
            if hand_landmarks[8][0] > hand_landmarks[20][0] and hand_landmarks[8][1] < hand_landmarks[20][1]:
                if hand_landmarks[20][1] > hand_landmarks[4][1]:
                        identified_gesture = 'We are #1'
    cv2.putText(frame, identified_gesture, (0, 35), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
    cv2.imshow('Window 1', frame)
    cv2.moveWindow('Window 1',0,0)
    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
