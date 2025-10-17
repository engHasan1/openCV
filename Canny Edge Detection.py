import cv2

img = cv2.imread('images/img.png')

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blur_img=cv2.GaussianBlur(gray_img,(3,3),0)

canny_img = cv2.Canny(blur_img, 100, 200)

cv2.imshow("Original Image", img)
cv2.imshow("Gray Image", gray_img)
cv2.imshow("Blurred Image", blur_img)
cv2.imshow("Canny Edge Detection", canny_img)
cv2.waitKey(0)
cv2.destroyAllWindows()