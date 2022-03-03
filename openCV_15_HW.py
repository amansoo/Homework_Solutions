import time
import cv2
import mediapipe

width = 1260
height = 720

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

# Enter code here:

def multi_hands_landmarks(frame) -> list:
    frame_RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Mediapipe works with RGB
    multi_hands_landmarks_class = hands_analyser.process(frame_RGB)  # Tries to finds hands and saves the complicated 
    # array in variable.
    if multi_hands_landmarks_class.multi_hand_landmarks:  # Breaks the data set in a simple 21 landmarks for each hand.

        for single_hand_landmarks in multi_hands_landmarks_class.multi_hand_landmarks:
            my_hand = []
            for single_landmark in single_hand_landmarks.landmark:
                x_normal = int(single_landmark.x * width)
                y_normal = int(single_landmark.y * height)

                my_hand.append((x_normal, y_normal))  # Resets every hand iteration
            my_hands.append(my_hand)

    return my_hands

hands_analyser = mediapipe.solutions.hands.Hands(False, 1, .5, .5)  # Create an object to recognise hands
# ^ takes 4 params: true if image is still, false if live. 2 for how mnay hands to detect. .5, .5 should remain same.

draw_hands = mediapipe.solutions.drawing_utils  # create an object to then draw these hands out.

box_width = 126
box_height = 25

circle_center_row = int(height / 2)
circle_center_column = int(width / 2)

iteration_row = 10
iteration_column = 10

score = 0
while True:
    my_hands = []
    ignore,  frame = cam.read()
    multi_hands_landmarks_data = multi_hands_landmarks(frame)

    for single_hand_landmarks in multi_hands_landmarks_data:
        cv2.rectangle(frame, (int(single_hand_landmarks[8][0] - box_width / 2), 0), 
        (int(single_hand_landmarks[8][0] + box_width / 2), box_height), (0, 0, 0), -1)
    
    cv2.circle(frame, (circle_center_column, circle_center_row), 25, (0, 255, 255), -1)

    # The below four cases will reverse the direction of the ball if it hits the bottom, left or right corners and crash
    # if it hits the top one
    
    if circle_center_row + 25 >= height:
        iteration_row *= -1  
    if circle_center_column + 25 >= width or circle_center_column - 25 <= 0:
        iteration_column *= -1

    if circle_center_row - 25 <= box_height and \
    circle_center_column in range(single_hand_landmarks[8][0] - int(box_width / 2), single_hand_landmarks[8][0] + int(box_width / 2)):
        iteration_row *= -1
        score += 1
    if circle_center_row - 25 <= 0:
        break
    cv2.rectangle(frame, (0, 650), (200, height), (0, 0, 0,), -1)
    cv2.putText(frame, f'Score: {score}', (0, height), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (255, 255, 255), 1)
    circle_center_column += iteration_column
    circle_center_row += iteration_row

    cv2.imshow('Window 1', frame)
    cv2.moveWindow('Window 1',0,0)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
