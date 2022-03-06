import os
import cv2
import face_recognition as recog

starting_dir = 'C:/Users/amans/Documents/AI_python/demo_images/known'

for root, dirs, files in os.walk(starting_dir):
    print("You are in the directory: {}".format(root))
    print("Folders in the directory: {}".format(dirs))
    print("FIles in the directory: {}".format(files))
    for file in files:
        full_path = starting_dir + '/' + file
        print(full_path)  # For debugging purposes
        picture = recog.load_image_file(full_path)
        pictureBGR = cv2.cvtColor(picture, cv2.COLOR_RGB2BGR)  # This is becasue .jpg are saved in the RBG colour space and CV
        name = file[:-4]
        # wants BGR
        cv2.imshow(name, pictureBGR)
        cv2.waitKey(2500)
        cv2.destroyAllWindows()  # So that after the window is shown for the amount of time, it gets destroyed
