import numpy as np
import matplotlib.pyplot as plt
import skimage
from skimage import io
import cv2


# Do NOT modifify the function names

def my_resize(img, height, width):
    
    # TODO_C1
    processed = img.copy()
    img_height, img_width= processed.shape

    processed = processed.ravel()

    x_ratio = float(img_width - 1) / (width - 1) if width > 1 else 0
    y_ratio = float(img_height - 1) / (height - 1) if height > 1 else 0

    y, x = np.divmod(np.arange(height * width), width)

    x_l = np.floor(x_ratio * x).astype('int32')
    y_l = np.floor(y_ratio * y).astype('int32')

    x_h = np.ceil(x_ratio * x).astype('int32')
    y_h = np.ceil(y_ratio * y).astype('int32')

    x_weight = (x_ratio * x) - x_l
    y_weight = (y_ratio * y) - y_l

    a = processed[y_l * img_width + x_l]
    b = processed[y_l * img_width + x_h]
    c = processed[y_h * img_width + x_l]
    d = processed[y_h * img_width + x_h]

    resized = a * (1 - x_weight) * (1 - y_weight) + \
                b * x_weight * (1 - y_weight) + \
                c * y_weight * (1 - x_weight) + \
                d * x_weight * y_weight

    return resized.reshape(height, width)


def my_rotation(img, angle):
    
    # TODO_C2
    angle_rad = np.deg2rad(angle)

    h, w = img.shape[:2]
    

    # Check if the image is grayscale or color
    if len(img.shape) == 3:
        c = img.shape[2]  # Color channels
    else:
        c = 1  # Grayscale image

    # Calculate the new image dimensions
    new_h = int(abs(h * np.cos(angle_rad)) + abs(w * np.sin(angle_rad)))
    new_w = int(abs(w * np.cos(angle_rad)) + abs(h * np.sin(angle_rad)))

    center_y, center_x = h // 2, w // 2
    new_center_y, new_center_x = new_h // 2, new_w // 2

    # translation_matrix = np.array([
    #     [1, 0, new_center_y - center_y],
    #     [0, 1, new_center_x - center_x],
    #     [0, 0, 1]
    # ])
    # translation_matrix = np.array([
    #     [1, 0, new_center_x - center_x],
    #     [0, 1, new_center_y - center_y],
    #     [0, 0, 1]
    # ])

    translation_matrix = np.array([
    [1, 0, (new_w - w) / 2],
    [0, 1, (new_h - h) / 2],
    [0, 0, 1]
])

    cos_a, sin_a = np.cos(angle_rad), np.sin(angle_rad)
    # This is the rotation matrix for rotating around the center
    rotation_matrix = np.array([
        [cos_a, -sin_a, center_x * (1 - cos_a) + center_y * sin_a],
        [sin_a, cos_a, center_y * (1 - cos_a) - center_x * sin_a],
        [0, 0, 1]
    ])

    transform_matrix = np.dot(translation_matrix, rotation_matrix)


    # Create an output image filled with zeros (black)
    rotated_img = np.zeros((new_h, new_w, c), dtype=img.dtype)

    # inv_transform_matrix = np.linalg.inv(transform_matrix)

    # Inverse mapping for each pixel in the output image
    for i in range(new_h):
        for j in range(new_w):
            # Apply the inverse transformation matrix
            vec = np.array([j, i, 1])
            x, y, _ = np.dot(np.linalg.inv(transform_matrix), vec)
            x = int(round(x))
            y = int(round(y))

            # Nearest neighbor interpolation
            if 0 <= x < w and 0 <= y < h:
                rotated_img[i, j] = img[y, x]
    return rotated_img


# You are incouraged to test your program in the main function

def main():
    cat = cv2.imread('cat.jpg') #(829,949,3)
    monkey = cv2.imread('monkey_island.jpg') #(500,800,3)

    cat = cv2.cvtColor(cat, cv2.COLOR_BGR2GRAY)
    cat = cv2.resize(cat, (600, 600))
    cv2.imwrite('resultC1.jpg', my_resize(cat, 100, 60))
    cv2.imwrite('resultC2.jpg', my_rotation(cat, 20))

    # Rotate RGB image
    cv2.imwrite('resultC3.jpg', my_rotation(monkey, 20))



if __name__ == "__main__":
    main()


