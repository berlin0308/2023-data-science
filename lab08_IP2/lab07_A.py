import cv2
from skimage import io
import numpy as np
from scipy.signal import convolve2d
import matplotlib.pyplot as plt

def main():
    img = io.imread('Samoyed.jpg')
    filtA = np.array([[-1,-1,-1],[2,2,2],[-1,-1,-1]])
    filtB = np.array([[-1,-1,2],[-1,2,-1],[2,-1,-1]])
    filtC = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
    filtD = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
    filtE = np.array([[0,-1,0],[1,0,1],[0,-1,0]])

    cv2.imwrite('resultA1.jpg', cv2.filter2D(img, -1, filtA))
    cv2.imwrite('resultA2.jpg', cv2.filter2D(img, -1, filtB))
    cv2.imwrite('resultA3.jpg', cv2.filter2D(img, -1, filtC))
    cv2.imwrite('resultA4.jpg', cv2.filter2D(img, -1, filtD))
    cv2.imwrite('resultA5.jpg', cv2.filter2D(img, -1, filtE))

if __name__ == "__main__":
    main()
    
    
