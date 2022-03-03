import cv2
import mediapipe
from numpy import pad

# Please don't change these variables
width = 1260  # Note this does not return an image with 1260 pixels, rather 1280.
height = 720

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

# Enter code here:
paddle_1_postion = 100
paddle_2_position = 100

circle_center_row = int(height / 2)
circle_center_column = int(width / 2)
circle_radius = 25
iteration_row = 5
iteration_column = 5


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


hands_analyser = mediapipe.solutions.hands.Hands(False, 2, .5, .5)
drawing_landmarks = mediapipe.solutions.drawing_utils

while True:
    ignore,  frame = cam.read()
    my_hands, hands_handedness = get_my_hands(frame)  # my_hands gets only location of landmarks of each hand.
    print(hands_handedness)
    if hands_handedness:
        if 'Left' in hands_handedness:  # IS RIGHT!!
            left_index = hands_handedness.index('Left')
            for single_hand_landmarks in [my_hands[left_index]]:
                paddle_1_postion = single_hand_landmarks[17][1]  # [1] because we want the y value.

    if hands_handedness:
        if 'Right' in hands_handedness:
            right_index = hands_handedness.index('Right')
            for single_hand_landmarks in [my_hands[right_index]]:  # An extra [] is used so that we can get ONLY the second hand landmarks.
                # but not allll the landmarks one bye one, all landmarks at ONCE.
                paddle_2_position = single_hand_landmarks[17][1]
    
    cv2.rectangle(frame, (0, paddle_1_postion), (0 + 20, (paddle_1_postion + 100)), (255, 0, 0), -1)
    cv2.rectangle(frame, (width, paddle_2_position), (width + 20, (paddle_2_position + 100)), (255, 0, 0,), -1)
    cv2.circle(frame, (circle_center_column, circle_center_row), circle_radius, (0, 0, 255), -1)
    if circle_center_row - 25 <= 0 or circle_center_row + 25 >= height:
        iteration_row *= -1
    
    if circle_center_column <= 20 and circle_center_row in range(paddle_1_postion, paddle_1_postion + 101):
        iteration_column *= -1
    elif circle_center_column >= 1260 and circle_center_row in range(paddle_2_position, paddle_2_position + 101):
        iteration_column *= -1
    if circle_center_column <= 20 and circle_center_row not in range(paddle_1_postion, paddle_1_postion + 101):
        break
    elif circle_center_column >= 1260 and circle_center_row not in range(paddle_2_position, paddle_2_position + 101):
        break
    
    circle_center_column += iteration_column
    circle_center_row += iteration_row
    cv2.imshow('Window 1', frame)
    cv2.moveWindow('Window 1',0,0)
    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
