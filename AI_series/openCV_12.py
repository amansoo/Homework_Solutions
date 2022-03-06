import cv2
from cv2 import COLOR_RGB2BGR
import face_recognition as FR

font = cv2.FONT_HERSHEY_SIMPLEX
# Training on DONNY
the_donald = FR.load_image_file('C:/Users/amans/Documents/AI_python/demo_images/known/Donald Trump.jpg')
faces_location = FR.face_locations(the_donald)[0]
donny_encoding = FR.face_encodings(the_donald)[0]

# Trainging on Nancy
nancy = FR.load_image_file('C:/Users/amans/Documents/AI_python/demo_images/known/Nancy Pelosi.jpg')
faces_location = FR.face_locations(nancy)[0]
nancy_encoding = FR.face_encodings(nancy)[0]

names = ['Donny', 'Nancy']
encodings = [donny_encoding, nancy_encoding]

unknown_faces = FR.load_image_file('C:/Users/amans/Documents/AI_python/demo_images/unknown/u1.jpg')
unknown_faces_BGR = cv2.cvtColor(unknown_faces, COLOR_RGB2BGR)
unknown_faces_locas = FR.face_locations(unknown_faces)
unknown_encodings = FR.face_encodings(unknown_faces)

for unknown_face_loca, unknown_encoding in zip(unknown_faces_locas, unknown_encodings):
    top, right, bottom, left = unknown_face_loca

    name_of_person_found = 'Unknown Person'  # So that later we can put this if we don't know the person.
    cv2.rectangle(unknown_faces_BGR, (left, top), (right, bottom), (255, 0, 0), 2)
    match_array = FR.compare_faces(encodings, unknown_encoding)
    print(match_array)

    if True in match_array:
        match_index = match_array.index(True)
        name_of_person_found = names[match_index]
        print(name_of_person_found)
    cv2.putText(unknown_faces_BGR, name_of_person_found, (left, top), font, 1, (255, 0, 0), 2)

cv2.imshow("Face Recog", unknown_faces_BGR)
cv2.waitKey(20000)
