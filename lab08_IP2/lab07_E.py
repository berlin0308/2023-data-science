import numpy as np
from skimage import io
from skimage.filters import threshold_local
import cv2
import matplotlib.pyplot as plt
import imutils
from imutils.perspective import four_point_transform
from skimage.filters.rank import mean
from skimage.morphology import square


def scan_document(img): 
    scanned = img.copy()

    gray_img = cv2.cvtColor(scanned, cv2.COLOR_BGR2GRAY)
    blur_img = cv2.GaussianBlur(gray_img, (3,3), 0)
    # blur_img = mean(blur_img, square(3))

    canny = cv2.Canny(blur_img, 20, 90)
    kernel = np.ones((3,3))
    canny = cv2.dilate(canny, kernel, iterations = 3)
    cnts = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts = sorted(cnts, key = cv2.contourArea, reverse=True)[:1]
    for c in cnts:
        peri = cv2.arcLength(c,True)
        approx = cv2.approxPolyDP(c, 0.01*peri, True)
        if len(approx)==4:
            screenCnt = approx
            break
    scanned = cv2.cvtColor(scanned, cv2.COLOR_BGR2RGB)
    cv2.drawContours(scanned, [screenCnt], -1, (0,0,0), 2)
    cv2.imwrite('resultE1.jpg', scanned)
    warped = four_point_transform(scanned, screenCnt.reshape(4, 2))
    warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
    T = threshold_local(warped, 43, offset = 15, method = 'gaussian', mode='constant')
    scanned = (warped>T)*255

    return scanned

def main():
    img = io.imread('invoice.jpg')
    scanned = scan_document(img)
    cv2.imwrite('resultE2.jpg', scanned)

if __name__ == "__main__":
    main()
    
    