import cv2 #importing OpenCV library
import numpy as np
import matplotlib.pyplot as plt



img = cv2.imread('fee.jpg', cv2.IMREAD_COLOR) #read the img from the disk and the img is read as colored img
cv2.imshow('Original Image',img) # display the img on the screen
cv2.waitKey(0)
 
image_border3 = cv2.copyMakeBorder(img, 300, 250, 100, 50, cv2.BORDER_REFLECT)
cv2.imshow('cool image',image_border3)#cool effect
cv2.waitKey(0)

denoised_image = cv2.fastNlMeansDenoisingColored(img, None, 15, 8, 8, 15)
cv2.imshow('blur',denoised_image)#blur effect
cv2.waitKey(0)

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray_image, 100, 200)
cv2.imshow('grey',edges)#cogreyol effect
cv2.waitKey(0)

image = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('Rotated image',image)
cv2.waitKey(0) 

image1 = cv2.flip(img, 0)
cv2.imshow('flipped image image',image1) 
cv2.waitKey(0) 
#cv2.imshow('Original Image',img) # display the img on the screen

img = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_CONSTANT, None, value = 0) #border to the image
cv2.imshow('Bordered Image',img)

cv2.waitKey(0)          #Weight until user closes the img 
cv2.destroyAllWindows() #delete or remove the windows opened by the users

print("Properties :",img.shape) # gives the number of rows,colums and channel

print("Pixel Size :",img.size)

down_width = 300
down_height = 200
down_points = (down_width, down_height)
resized_down = cv2.resize(img, down_points, interpolation= cv2.INTER_LINEAR)
 
#upscale the img using new  width and height
up_width = 600
up_height = 400
up_points = (up_width, up_height)
resized_up = cv2.resize(img, up_points, interpolation= cv2.INTER_LINEAR)
 
# Display images
cv2.imshow('Resized Down by defining height and width', resized_down)
cv2.waitKey()
cv2.imshow('Resized Up img by defining height and width', resized_up)
cv2.waitKey()

image = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('Rotated image',img)
print(img)