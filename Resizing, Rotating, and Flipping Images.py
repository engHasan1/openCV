import cv2 

img=cv2.imread('images/img.png')    


# # Resizing the image

# resized_img_with_Cubic=cv2.resize(img,(360,180),interpolation=cv2.INTER_CUBIC) #resize with cubic interpolation It is the best for zooming, and it is slower but provides more accurate results.
# resized_img_with_Linear=cv2.resize(img,(360,180),interpolation=cv2.INTER_LINEAR) #resize with linear interpolation It is the default method, and it is a good and balanced option for both cases.
# resized_img_with_Area=cv2.resize(img,(360,180),interpolation=cv2.INTER_AREA) #resize with area interpolation It is the best for shrinking.
# resized_img_with_Nearest=cv2.resize(img,(360,180),interpolation=cv2.INTER_NEAREST) #resize with nearest interpolation
# resized_img_with_Lanczos=cv2.resize(img,(360,180),interpolation=cv2.INTER_LANCZOS4) #resize with lanczos interpolation

# cv2.imshow('Resized Image with Cubic Interpolation',resized_img_with_Cubic)
# cv2.imshow('Resized Image with Linear Interpolation',resized_img_with_Linear)
# cv2.imshow('Resized Image with Area Interpolation',resized_img_with_Area)
# cv2.imshow('Resized Image with Nearest Interpolation',resized_img_with_Nearest)
# cv2.imshow('Resized Image with Lanczos Interpolation',resized_img_with_Lanczos)

# ----------------------------------

# # Rotating the image
# (h,w)=img.shape[:2]
# center=(w//2,h//2)
# M=cv2.getRotationMatrix2D(center,45,1.0) #get the rotation matrix
# rotated_img=cv2.warpAffine(img,M,(w,h)) #rotate the image
# cv2.imshow('Rotated Image',rotated_img)

# ----------------------------------

# Flipping the image
flipped_image_0=cv2.flip(img,0) #flip around x-axis
flipped_image_1=cv2.flip(img,1) #flip around y-axis
flipped_image_minus_1=cv2.flip(img,-1) #flip around both axis

cv2.imshow('Original Image',img)
cv2.imshow('Flipped Image around x-axis',flipped_image_0)
cv2.imshow('Flipped Image around y-axis',flipped_image_1)
cv2.imshow('Flipped Image around both axis',flipped_image_minus_1)
cv2.waitKey(0)
cv2.destroyAllWindows()

