import cv2
import numpy as np

img=cv2.imread('images/limon.png')

# # thresholding 
# gray_imag=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# ret,thresh=cv2.threshold(gray_imag,190,255,cv2.THRESH_BINARY)

# # cv2.imshow('Original Image',img)
# # cv2.imshow('Gray Image',gray_imag)
# # cv2.imshow('Threshold Image',thresh)

#-------------------

# # Masking
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_green = np.array([30, 40, 40])  
upper_green = np.array([90, 255, 255])
mask = cv2.inRange(hsv_img, lower_green, upper_green)
result = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow("1. Original Image", img)
cv2.imshow("2. The Mask (White = Green)", mask)
cv2.imshow("3. Final Result (Isolated Green)", result)
cv2.waitKey(0)
cv2.destroyAllWindows()

