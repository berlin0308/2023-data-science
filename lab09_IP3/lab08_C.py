import cv2
from skimage import io
from skimage import filters
import numpy as np
import matplotlib.pyplot as plt

def main():
    xray = io.imread('./lab09-1/Xray.png')
    xray = xray.astype(np.float32)
    xray/=255
    mean_kernel = np.ones((5,5),np.float32)/25
    xray_denoised_A = filters.laplace(xray)
    xray_denoised_B = xray-xray_denoised_A
    xray_denoised_C = (filters.sobel_h(xray_denoised_B)**2+filters.sobel_v(xray_denoised_B)**2)**0.5
    xray_denoised_D = cv2.filter2D(xray_denoised_C,-1,mean_kernel)
    xray_denoised_E = cv2.multiply(xray_denoised_B, xray_denoised_D)
    xray_denoised_F = xray+xray_denoised_E
    xray_denoised_G = np.array((xray_denoised_F/255)**0.5)

    fig = plt.figure(figsize=(11,7))
    ax1 = fig.add_subplot(2,4,1)
    ax1.imshow(xray, cmap='gray')
    ax1.set_title('original image')
    ax2 = fig.add_subplot(2,4,2)
    ax2.imshow(xray_denoised_A, cmap='gray')
    ax2.set_title('(a)')
    ax3 = fig.add_subplot(2,4,3)
    ax3.imshow(xray_denoised_B, cmap='gray')
    ax3.set_title('(b)')
    ax4 = fig.add_subplot(2,4,4)
    ax4.imshow(xray_denoised_C, cmap='gray')
    ax4.set_title('(c)')
    ax5 = fig.add_subplot(2,4,5)
    ax5.imshow(xray_denoised_D, cmap='gray')
    ax5.set_title('(d)')
    ax6 = fig.add_subplot(2,4,6)
    ax6.imshow(xray_denoised_E, cmap='gray')
    ax6.set_title('(e)')
    ax7 = fig.add_subplot(2,4,7)
    ax7.imshow(xray_denoised_F, cmap='gray')
    ax7.set_title('(f)')
    ax8 = fig.add_subplot(2,4,8)
    ax8.imshow(xray_denoised_G, cmap='gray')
    ax8.set_title('(g)')
    plt.show()

    plt.imsave('resultC1.jpg', xray_denoised_A, cmap='gray')
    plt.imsave('resultC2.jpg', xray_denoised_B, cmap='gray')
    plt.imsave('resultC3.jpg', xray_denoised_C, cmap='gray')
    plt.imsave('resultC4.jpg', xray_denoised_D, cmap='gray')
    plt.imsave('resultC5.jpg', xray_denoised_E, cmap='gray')
    plt.imsave('resultC6.jpg', xray_denoised_F, cmap='gray')
    plt.imsave('resultC7.jpg', xray_denoised_G, cmap='gray')

if __name__ == "__main__":
    main()
    
    
