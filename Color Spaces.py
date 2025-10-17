import cv2 

img=cv2.imread('images/img.png')

converted_img_to_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
converted_img_to_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
converted_img_to_lab=cv2.cvtColor(img,cv2.COLOR_BGR2Lab)
cv2.imshow('Original Image',img)
cv2.imshow('Gray Image',converted_img_to_gray)
cv2.imshow('HSV Image',converted_img_to_hsv)
cv2.imshow('Lab Image',converted_img_to_lab)
cv2.waitKey(0)
cv2.destroyAllWindows()
