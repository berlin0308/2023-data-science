import cv2
from skimage import io
import numpy as np
import matplotlib.pyplot as plt
import imutils
import math

def main():
    rice = io.imread('./lab09-1/SingleRice.jpg')
    showRice = rice.copy()

    rice = cv2.cvtColor(rice, cv2.COLOR_BGR2GRAY)

    ret, rice = cv2.threshold(rice, 71, 100, cv2.THRESH_BINARY)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(10,10))
    rice = cv2.erode(rice, kernel, iterations = 2)
    rice = cv2.dilate(rice, kernel, iterations = 3)

    contours = cv2.findContours(rice, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    contours = sorted(contours, key = cv2.contourArea, reverse=True)[:1]

    for contour in contours:
        cv2.drawContours(showRice,[contour],-1,(255,0,0),5)

    plt.show()
    plt.imsave('resultB.jpg', showRice, cmap='gray')

if __name__ == "__main__":
    main()
    
    
