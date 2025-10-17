import cv2

img = cv2.imread('images/img.png') 


kernel_size = (3, 3)
avg_blur = cv2.blur(img,(10,10))
gaussian_blur = cv2.GaussianBlur(img, kernel_size, 0)
median_blur = cv2.medianBlur(img, 7)
cv2.imshow("Original Image", img)
cv2.imshow("Averaging Blur", avg_blur)
cv2.imshow("Gaussian Blur", gaussian_blur)
cv2.imshow("Median Blur", median_blur)


cv2.waitKey(0)
cv2.destroyAllWindows()