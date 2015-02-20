import cv2
import numpy as np


def produce_black_image(dimensionList):
    
    x, y, z = dimensionList[0], dimensionList[1], dimensionList[2]
    
    return np.zeros((x,y,z), np.uint8)

def threshold_image(image):
    
    ret,thresh = cv2.threshold(image,220,255,cv2.THRESH_BINARY)
    
    return thresh



im = cv2.imread('Blueye.jpg')

blackIm = produce_black_image(im.shape)

subtractedImage = blackIm - im 

smallSub = cv2.resize(subtractedImage, (0,0), fx=0.5, fy=0.5) 

threshed = threshold_image(smallSub)

cv2.imshow("frame", threshed)

cv2.waitKey() 