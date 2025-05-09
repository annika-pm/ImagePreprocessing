import cv2
import numpy as np
import matplotlib.pyplot as plt

image=cv2.imread(r'D:\4SF22CI015\wall-39.jpg')

if image is None:
    raise FileNotFoundError("The image file 'nature.jpg' was not found.")

_, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

kernel = np.ones((3, 3), np.uint8)

eroded = cv2.erode(binary_image, kernel, iterations=1)
dilated = cv2.dilate(binary_image, kernel, iterations=1)
opening = cv2.morphologyEx(binary_image, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel)

titles = ['Original Binary', 'Erosion', 'Dilation', 'Opening', 'Closing']
images = [binary_image, eroded, dilated, opening, closing]

plt.figure(figsize=(15, 8))
for i in range(5):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.show()
