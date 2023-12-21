import cv2
from skimage import io
from skimage import filters
from skimage import morphology
from skimage.filters import threshold_local
import numpy as np
import matplotlib.pyplot as plt
import fingerprint_enhancer
from skimage.morphology import disk, square, rectangle, diamond, skeletonize, thin


finger = io.imread('./lab09-1/Fingerprint.tif')
img = finger.copy()
finger = cv2.GaussianBlur(finger, (5,5), 0)
T = threshold_local(finger, 85, offset =10, method = 'gaussian', mode = 'constant')
finger = (finger<T)*255

finger = fingerprint_enhancer.enhance_Fingerprint(img)
finger = morphology.binary_erosion(finger, disk(1))
finger = morphology.binary_dilation(finger, disk(1))
finger = morphology.remove_small_holes(finger, 70, connectivity=1)
finger = morphology.remove_small_objects(finger, 20, connectivity=2)
finger = morphology.thin(finger)
finger = finger+0
ROI_finger = cv2.ellipse(np.zeros((480,400)), (227,232), (195,152), 90, 0, 360, (255,255,255), -1)

plt.imsave('intermidiate.jpg',img, cmap='gray')
img = io.imread('intermidiate.jpg')

for i in range(1, finger.shape[0]-1):
    for j in range(1, finger.shape[1]-1):
        CN =0.5*(np.abs(finger[i-1,j-1]-finger[i,j-1])+np.abs(finger[i,j-1]-finger[i+1,j-1])+np.abs(finger[i+1,j-1]-finger[i+1,j])+np.abs(finger[i+1,j]-finger[i+1,j+1])
            +np.abs(finger[i+1,j+1]-finger[i,j+1])+np.abs(finger[i,j+1]-finger[i-1,j+1])+np.abs(finger[i-1,j+1]-finger[i-1,j])+np.abs(finger[i-1,j]-finger[i-1,j-1]))
        if CN==1 and finger[i,j]==1 and ROI_finger[i,j]==255:
            cv2.circle(img, (j, i), 10, (0,255,0), 1)
        if CN==3 and finger[i,j]==1 and ROI_finger[i,j]==255:
            cv2.circle(img, (j, i), 10, (255,0,0), 1)
            
plt.imsave('fingerprint.jpg', img)
    
    
    
