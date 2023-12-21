import numpy as np
import matplotlib.pyplot as plt
import skimage
from skimage import io
import cv2


# Do NOT modifify the function names

def fade_gradually(img):
    processed = img.copy()

    # TODO_B1
    change_ratio = np.linspace(1,0,processed.shape[1])
    processed = cv2.cvtColor(processed,cv2.COLOR_BGR2HLS)
    for i in range(processed.shape[0]):
        processed[i,:,2] = processed[i,:,2]*change_ratio**1.8
    processed = cv2.cvtColor(processed, cv2.COLOR_HLS2BGR)

    return processed


def image_matting(img):
    processed = img.copy()

    # TODO_B2
    processed = cv2.cvtColor(processed, cv2.COLOR_BGR2BGRA)
    for i in range(0,processed.shape[0]): 
        for j in range(0,processed.shape[1]): 
            if processed[i,j,0]<=10 and processed[i,j,1]<=10 and processed[i,j,2]<=10:
                processed[i,j,3] = 0

    return processed




# You are incouraged to test your program in the main function

def main():
    monkey = cv2.imread('monkey_island.jpg') #(500,800,3)
    cat = cv2.imread('cat.jpg') #(829,949,3)
    cv2.imwrite('resultB1.jpg', fade_gradually(monkey))
    cv2.imwrite('resultB2.png', image_matting(cat))


if __name__ == "__main__":
    main()


