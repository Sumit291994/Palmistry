import Tkinter
from Tkinter import *
from Tkinter import Tk
from tkFileDialog import askopenfilename
from socket import *
from thread import *
import sys,os
import time
import Tkinter as tk
from PIL import ImageTk, Image
import Image
import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('out_zoomed.png',0)
rows,cols = img.shape

M = cv2.getRotationMatrix2D((cols/2,rows/2),-25,1)
dst = cv2.warpAffine(img,M,(cols,rows))
cv2.imwrite("rotate.jpg",dst)
