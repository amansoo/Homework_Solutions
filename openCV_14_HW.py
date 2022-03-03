import cv2
import mediapipe
from numpy import array

width = 1260
height = 720

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

# Enter code here:


def pinkie_circle(frame) -> None:
    frame_RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Mediapipe works with RGB
    multi_hands_landmarks_class = hands_analyser.process(frame_RGB)  # Tries to finds hands and saves the complicated 
    # array in variable.
    if multi_hands_landmarks_class.multi_hand_landmarks:  # Breaks the data set in a simple 21 landmarks for each hand.

        for single_hand_landmarks in multi_hands_landmarks_class.multi_hand_landmarks:
            my_hand = []
            print(single_hand_landmarks.landmark)
            for single_landmark in single_hand_landmarks.landmark:
                x_normal = int(single_landmark.x * width)
                y_normal = int(single_landmark.y * height)
                my_hand.append((x_normal, y_normal))  # Resets every hand iteration

            cv2.circle(frame, (my_hand[20]), 25, (255, 0, 0), -1)



hands_analyser = mediapipe.solutions.hands.Hands(False, 2, .5, .5)  # Create an object to recognise hands
# ^ takes 4 params: true if image is still, false if live. 2 for how mnay hands to detect. .5, .5 should remain same.

draw_hands = mediapipe.solutions.drawing_utils  # create an object to then draw these hands out.

while True:
    ignore,  frame = cam.read()
    pinkie_circle(frame)
    cv2.imshow('Window 1', frame)
    cv2.moveWindow('Window 1',0,0)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
