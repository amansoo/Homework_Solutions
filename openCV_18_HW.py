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
            cv2.rectangle(frame, top_left, bottom_right, (0, 0, 255), 2)
            faces_location.append(face_location)
    return faces_location


def return_pose_landmarks(frame) -> list:
    """This function takes a frame, processes it (in RGB), finds all the landmarks in it and appends them to a list which resets every frame"""
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
                my_hand.append((x_normal, y_normal))  # Resets every hand iteration
            my_hands.append(my_hand)
    return my_hands, hands_handedness


face_detection_analyser_mp = mediapipe.solutions.face_detection.FaceDetection()
pose_analyser = mediapipe.solutions.pose.Pose(False, False, True, .5, .5)
hands_analyser = mediapipe.solutions.hands.Hands(False, 2, .5, .5)
while True:
    ignore,  frame = cam.read()
    faces_location = face_rec(frame)
    my_landmarks = return_pose_landmarks(frame)
    my_hands, hands_handedness = get_my_hands(frame)
    print(hands_handedness)
    cv2.imshow('Window 1', frame)
    cv2.moveWindow('Window 1',0,0)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
