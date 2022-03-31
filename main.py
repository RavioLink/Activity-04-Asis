import cv2
import numpy as np

filePath = 'Dizzy.jpg'
imgflag = 1
image = cv2.imread(filePath,imgflag)
cv2.imshow('Dizzy', image)


filepath2 = input("Paste here the directory of your image: ")
imgflag2 = int(input("input image flag here (1/0/-1): "))
image2 = cv2.imread(filepath2,imgflag2)
cv2.imshow('Second Image Loader',image2)


cv2.waitKey(0)
cv2.destroyAllWindows()
