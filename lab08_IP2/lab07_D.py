import cv2
from skimage import io
import numpy as np
import matplotlib.pyplot as plt
import imutils

yellow_lower = np.array([87,170,50])
yellow_upper = np.array([100,255,255])

def main():
    A = 0
    Fan = io.imread('YellowFan.png')
    hsv = cv2.cvtColor(Fan, cv2.COLOR_BGR2HSV)

    yellow_output = cv2.inRange(hsv, yellow_lower, yellow_upper)
    yellow_mask = cv2.bitwise_and(Fan, Fan, mask=yellow_output)
    blur = cv2.GaussianBlur(yellow_mask,(11,11),0)
    yellow_mask = cv2.erode(blur, None, iterations=3)
    yellow_mask = cv2.dilate(yellow_mask, None, iterations=3)
    c = cv2.cvtColor(yellow_mask, cv2.COLOR_HSV2RGB)
    c = cv2.cvtColor(yellow_mask, cv2.COLOR_RGB2GRAY)
    th2, c = cv2.threshold(c, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    contours = cv2.findContours(c, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 
    contours = imutils.grab_contours(contours)
    contours = sorted(contours, key = cv2.contourArea, reverse=True)[:3]

    for contour in contours:
        area = cv2.contourArea(contour)
        if(area > 270):
            A += area

    print('area:', A)
    plt.show()
    plt.imsave('resultD.jpg', c, cmap='gray')

if __name__ == "__main__":
    main()
    
    
