import cv2
import numpy as np
from matplotlib import pyplot as plt
import Image
from PIL import Image
import os.path


filename = os.path.join('blueLined.jpg')
img = Image.open(filename)

width, height = img.size
print "Dimensions:", img.size, "Total pixels:", width * height

WHITE_MIN = np.array([255,255,255], np.uint8)
WHITE_MAX = np.array([255,255,255], np.uint8)

BLACK_MIN = np.array([0,0,0], np.uint8)
BLACK_MAX = np.array([0,0,0], np.uint8)

img = cv2.imread("blueLined.jpg")
dst = cv2.inRange(img, WHITE_MIN, WHITE_MAX)
no_white = cv2.countNonZero(dst)
dst = cv2.inRange(img, BLACK_MIN, BLACK_MAX)
no_black = cv2.countNonZero(dst)

no_blue = (width*height) - no_white - no_black

print('The number of blue pixels is: ' + str(no_blue))
print('The number of white pixels is: ' + str(no_white))
print('The number of black pixels is: ' + str(no_black))

target = open("handshape.txt",'a')

data = str(no_blue)
target.write(data)
target.write("\n")

target.close()
