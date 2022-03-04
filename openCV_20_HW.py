# A breif explanation of how the program works:
# First, we calculate the distance of each point on one hand relative to itself and other points on the hands.
# We continue this for the points in the hand. This is our distance matrix for a known gesture.
# Then, when the user is ready, they show us their gesture. We also calculate the distance matrix for this gesture.
# We subtract the unknown gesture from the known gesture (values of them) and add them to the error
# This, 'error' tells us how far off the gesture is from our trained gesture, if not too far off, we can safely recognise it as
# the gesture or else mark it as unknown
import cv2
import numpy
import mediapipe

# Please don't change these variables
width = 720
height = 640

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
width += 20
# Enter code here:
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


def find_distance(hands_landmarks: list) -> list:
    """Return a distance matrix for all the points, to all the points"""
    distance_matrix = numpy.zeros([len(hands_landmarks), len(hands_landmarks)], dtype='float')
    for row in range(0, len(hands_landmarks)):
        for column in range(0, len(hands_landmarks)):
            # Distance formula is: Δx^2 + Δy*2 = d^2
            distance_matrix[row][column] = ((hands_landmarks[row][0] - hands_landmarks[column][0]) ** 2 + (hands_landmarks[row][1] - hands_landmarks[column][1])** 2) ** (1. / 2.)
    return distance_matrix


def find_error(known_gesture, unknown_gesture, key_points):
    error = 0
    for row in key_points:
        for column in key_points:
            error = error + abs(known_gesture[row][column] - unknown_gesture[row][column])
    return error


gestures_amount = int(input('How many gestures do you want to train?\n'))
gesture_names = []
for i in range(0, gestures_amount):
    gesture_name = input('Please enter gesture name {}:\n'.format(i))
    gesture_names.append(gesture_name)

hands_analyser = mediapipe.solutions.hands.Hands(False, 2, .5, .5)

key_points_array = [0,4,5,9,13,17,8,12,16,20]
known_gestures_distances_array = []
train = True
current_trainee = 0
while True:
    ignore,  frame = cam.read() 
    my_hands, hands_handedness = get_my_hands(frame)
    if train == True:
        if my_hands != []:
            print('Please enter {0}'.format(gesture_names[current_trainee]))
            if cv2.waitKey(1) & 0xff == ord('t'):
                known_gesture = find_distance(my_hands[0])
                known_gestures_distances_array.append(known_gesture)
                current_trainee += 1
                if current_trainee == gestures_amount:
                    train = False

    if train == False:
        if my_hands != []:
            for index, known_gesture_distance in enumerate(known_gestures_distances_array):
                unknown_gesture_distance = find_distance(my_hands[0])
                error = find_error(known_gesture_distance, unknown_gesture_distance, key_points=key_points_array)
                if error < 3000:
                    cv2.putText(frame, gesture_names[index], (0, 50), cv2.FONT_HERSHEY_COMPLEX, 3, (0, 255, 0), 2)
    cv2.imshow('Window 1', frame)
    cv2.moveWindow('Window 1',0,0)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()
