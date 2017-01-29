import cv2
import numpy as np
from matplotlib import pyplot as plt
import Image
from PIL import Image
import os.path


filename = os.path.join('line.png')
img = Image.open(filename)


width, height = img.size
print "Dimensions:", img.size, "Total pixels:", width * height

WHITE_MIN = np.array([0,0,0], np.uint8)
WHITE_MAX = np.array([0,0,0], np.uint8)

img = cv2.imread("line.png")
print img 
dst = cv2.inRange(img, WHITE_MIN, WHITE_MAX)
no_white = cv2.countNonZero(dst)
no_white=width*height - no_white
print('The number of white pixels is: ' + str(no_white))

target = open("MarriageLineLength.txt",'w')

data = str(no_white)
target.write(data)
target.write("\n")

target.close()

#cv2.namedWindow("opencv")
#cv2.imshow("opencv",img)
