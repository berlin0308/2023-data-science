import cv2
import os
import mahotas.features
from skimage.feature import Cascade
import pandas as pd
import numpy as np


def extract_image(image):

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(
        blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    # Find contours
    contours, _ = cv2.findContours(
        thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Create a blank mask
    mask = np.zeros_like(gray)

    # Draw contours on the mask
    cv2.drawContours(mask, contours, -1, (255), thickness=cv2.FILLED)

    # Apply the mask to the original image
    result = cv2.bitwise_and(image, image, mask=mask)

    # Display the results
    return result


def fourier_descriptors(contour, num_descriptors=10):
    contour_complex = contour[:, 0, 0] + 1j * contour[:, 0, 1]
    descriptors = np.fft.fft(contour_complex)
    descriptors = np.fft.fftshift(descriptors)
    descriptors = descriptors[:num_descriptors]
    return descriptors


def calculate_texture_features(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Calculate GLCM
    glcm = mahotas.features.haralick(gray_image.astype(np.uint8))
    # Extract specific GLCM features
    contrast = glcm[:, 1].mean()  # Contrast
    dissimilarity = glcm[:, 2].mean()  # Dissimilarity
    homogeneity = glcm[:, 4].mean()  # Homogeneity
    energy = glcm[:, 8].mean()  # Energy
    correlation = glcm[:, 9].mean()  # Correlation
    asm = glcm[:, 10].mean()  # ASM

    texture_features = np.array(
        [contrast, dissimilarity, homogeneity, energy, correlation, asm])

    return texture_features


def extract_features(image_path):
    image = cv2.imread(image_path)
    # image = cv2.imread('fruits_v2\\test\\Apple\\autoxautomAUTOcFFFFFF-2-5_jpg.rf.418872f9dd77627609c7e408a22f44cd.jpg')
    image = extract_image(image)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(
        blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Find contours
    contours, _ = cv2.findContours(
        thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # cv2.imwrite("extracted_image.jpg", image)


    data = []

    for contour in contours:
        descriptors = fourier_descriptors(contour, num_descriptors=20)

    texture_features = calculate_texture_features(image)
    data.append({
        'filepaths': image_path,
        'class': image_path.split('/')[-2],
        'label': '3',
        'phase': 'train',
        'dissimilarity': texture_features[1],
        'homogeneity': texture_features[2],
        'contrast': texture_features[0],
        'energy': texture_features[3],
        'ASM': texture_features[5],
        'correlation': texture_features[4],
        'fourier_descriptors': descriptors,
    })
    return data


def main():


    image_paths = []
    extracted_data = []

    classes = ['Apple','Banana','Carrot','Orange']

    for filename in os.listdir(f'fruits_v2/train/{classes[3]}/'):
        if filename.endswith('.jpg'):
            image_paths.append(
                f'fruits_v2/train/{classes[3]}/' + filename)

    for image_path in image_paths:
        image_features = extract_features(image_path)
        extracted_data.extend(image_features)

    df = pd.DataFrame(extracted_data)
    df = df.drop_duplicates(subset='filepaths', keep='first')
    # csv_filename = 'features.csv'
    # df.to_csv(csv_filename, index=False)
    existing_data = pd.read_csv('features_3.csv')
    combined_data = pd.concat([existing_data, df], ignore_index=True)
    combined_data.to_csv('features_4.csv', index=False)


if __name__ == "__main__":
    # main()
    df = pd.read_csv('features_4.csv')
    print(df)

