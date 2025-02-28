import cv2
import matplotlib.pyplot as plt
import numpy as np  # Import numpy

# Read input image
img = cv2.imread('images1.jfif')

# Flip the image horizontally
flipped = cv2.flip(img, 1)

# Convert to grayscale
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Resize the image
stretch_near = cv2.resize(img, (780, 540), interpolation=cv2.INTER_LINEAR)

# Apply Gaussian blur
Gaussian = cv2.GaussianBlur(img, (7, 7), 0)

# Image translation
height, width = img.shape[:2]
quarter_height, quarter_width = height / 4, width / 4
T = np.float32([[1, 0, quarter_width], [0, 1, quarter_height]])
img_translation = cv2.warpAffine(img, T, (width, height))

# Display images using OpenCV
cv2.imshow('Flipped Image', flipped)
cv2.waitKey(0)
cv2.imshow('Grayscale', gray_image)
cv2.waitKey(0)
cv2.imshow('Magnify', stretch_near)
cv2.waitKey(0)
cv2.imshow('Gblur', Gaussian)
cv2.waitKey(0)
cv2.imshow('Translation', img_translation)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()

# Function to divide the image into quadrants
def divide_image_into_quadrants(image):
    height, width = image.shape[:2]
    mid_x, mid_y = int(width / 2), int(height / 2)
    
    top_left = image[:mid_y, :mid_x]
    top_right = image[:mid_y, mid_x:]
    bottom_left = image[mid_y:, :mid_x]
    bottom_right = image[mid_y:, mid_x:]
    
    return top_left, top_right, bottom_left, bottom_right

# Load image to divide into quadrants
img = cv2.imread('images1.jfif')

# Divide the image into quadrants
quadrants = divide_image_into_quadrants(img)

# Access individual quadrants
top_left = quadrants[0]
top_right = quadrants[1]
bottom_left = quadrants[2]
bottom_right = quadrants[3]

# Convert BGR to RGB for Matplotlib display
top_left_rgb = cv2.cvtColor(top_left, cv2.COLOR_BGR2RGB)
top_right_rgb = cv2.cvtColor(top_right, cv2.COLOR_BGR2RGB)
bottom_left_rgb = cv2.cvtColor(bottom_left, cv2.COLOR_BGR2RGB)
bottom_right_rgb = cv2.cvtColor(bottom_right, cv2.COLOR_BGR2RGB)

# Plot quadrants using Matplotlib
plt.figure(figsize=(10, 10))

# Show the top-left quadrant
plt.subplot(2, 2, 1)
plt.imshow(top_left_rgb)
plt.title('Top Left')
plt.axis('off')

# Show the top-right quadrant
plt.subplot(2, 2, 2)
plt.imshow(top_right_rgb)
plt.title('Top Right')
plt.axis('off')

# Show the bottom-left quadrant
plt.subplot(2, 2, 3)
plt.imshow(bottom_left_rgb)
plt.title('Bottom Left')
plt.axis('off')

# Show the bottom-right quadrant
plt.subplot(2, 2, 4)
plt.imshow(bottom_right_rgb)
plt.title('Bottom Right')
plt.axis('off')

# Show the plot with all quadrants
plt.tight_layout()
plt.show()
cv2.waitKey(0)
