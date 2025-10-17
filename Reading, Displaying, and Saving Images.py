import cv2

# Reading an image 
image1 =cv2.imread('images/img.png',cv2.IMREAD_COLOR)  #read an image in color mode
image2=cv2.imread('images/img.png',cv2.IMREAD_GRAYSCALE) #read an image in grayscale mode
image3=cv2.imread('images/img.png',cv2.IMREAD_UNCHANGED) #read an image including alpha channel

# Displaying the image
cv2.imshow('İmage Color',image1)
cv2.imshow('Image Grayscale',image2)
cv2.imshow('Image Unchanged',image3)

cv2.waitKey(0) #wait until a key is pressed

# saving the image
cv2.imwrite('images/image_color.png',image1) #save the color image
cv2.imwrite('images/image_grayscale.png',image2) #save the grayscale image
cv2.imwrite('images/image_unchanged.png',image3) #save the unchanged image

cv2.destroyAllWindows() #close all the opened windows

