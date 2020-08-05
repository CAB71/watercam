'''
Script to classify the captured images. 
It reads the images, displays them and saves them again with the selected value.
'''

# ----- Imports -------
import os
#import shutil
import cv2
#from matplotlib import pyplot as plt

# -------- change to image folder and start classification ------
os.chdir("/Users/c/Documents/")


for f in os.listdir():

    file_name, file_ext = os.path.splitext(f)
    if file_ext == ".jpg":							# only use jpg

        img = cv2.imread(f, cv2.IMREAD_COLOR)		# read and display image
        cv2.imshow(f, img)

        key = cv2.waitKey(0)						# wait for a key
        print(key)
        if key == 48:  # 0-key
            key = 0
        elif key == 49:  # 1 -key
            key = 1
        elif key == 50:  # 2 -key
            key = 2
        elif key == 51:  # 3 -key
            key = 3
        elif key == 52:  # 4 -key
            key = 4
        elif key == 53:  # 5 -key
            key = 5
        elif key == 54:  # 6 -key
            key = 6
        elif key == 55:  # 7 -key
            key = 7
        elif key == 56:  # 8 -key
            key = 8
        elif key == 57:  # 9 -key
            key = 9
        elif key == 101:  # e -key
            key = "e"
        elif key == 110:  # n -key
            continue
            # break
        # if ESC pressed, quit script
        elif key == 27:
            cv2.destroyAllWindows()					# close image
            break
        else:
            key = "e" # classify as image error

        shutil.move(								# move and rename file to new folder
            "/Users/c/Documents/" + f,
            "/Users/c/Documents/class/"
            + str(key)
            + "_"
            + f,
        )
        cv2.destroyAllWindows()
