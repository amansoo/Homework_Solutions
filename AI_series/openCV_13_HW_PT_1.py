import os
import cv2
import face_recognition as recog
import pickle

starting_dir = 'C:/Users/amans/Documents/AI_python/demo_images/known'

data = []

for root, dirs, files in os.walk(starting_dir):
    print("You are in the directory: {}".format(root))
    print("Folders in the directory: {}".format(dirs))
    print("FIles in the directory: {}".format(files))

    for file in files:
        full_path = starting_dir + '/' + file
        picture = recog.load_image_file(full_path)
        pictureBGR = cv2.cvtColor(picture, cv2.COLOR_RGB2BGR)  # This is becasue .jpg are saved in the RBG colour space and CV
        name = file[:-4]
        # wants BGR
        face_encoding = recog.face_encodings(pictureBGR)[0]
        data.append([name, face_encoding])

with open('my_data.pkl', 'wb') as md:
    pickle.dump(data, md)
