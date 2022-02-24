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
width = 1280  # Because my inbuilt does not give me 1260 pixels wide, it gives me 1280, so after I've set it, I reassign
# the variable.

# Enter code here:
def return_pose_landmarks(frame) -> list:
    """This function takes a frame, processes it (in RGB), finds all the landmarks in it and appends them to a list which resets every frame"""
    my_landmarks = []
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Because mediapipe works in RGB.
    pose_landmarks_class = pose_analyser.process(frameRGB)
    if pose_landmarks_class.pose_landmarks:
        # print(pose_landmarks_class.pose_landmarks)
        drawing_object.draw_landmarks(frame, pose_landmarks_class.pose_landmarks, mediapipe.solutions.pose.POSE_CONNECTIONS)
        for landmark in pose_landmarks_class.pose_landmarks.landmark:  # pose_landmarks_class.pose_landmarks.landmark has
            # all the landmarks in an array, so we iterate over individual landmark(s).
            my_landmarks.append((int(landmark.x * (width)), int(landmark.y * height)))
    return my_landmarks
pose_analyser = mediapipe.solutions.pose.Pose(False, False, True, .5, .5)  # First param: Is it still image? False
# Second: Only wanna look at the upper body? False! Wanna smooth the data out? True! Third and fourth: Detection threshold
# Do not worry about it :-)
drawing_object = mediapipe.solutions.drawing_utils
while True:
    ignore,  frame = cam.read()
    my_landmarks = return_pose_landmarks(frame)
    print(my_landmarks)
    cv2.imshow('Window 1', frame)
    cv2.moveWindow('Window 1',0,0)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
