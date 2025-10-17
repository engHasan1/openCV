import cv2

img = cv2.imread('images/limon.png')


gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blurred_img = cv2.GaussianBlur(gray_img, (3, 3), 0)
ret, binary_image = cv2.threshold(blurred_img, 180, 255, cv2.THRESH_BINARY_INV)

contours, hierarchy = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print(f"تم العثور على {len(contours)} محيط.")

img_with_contours = img.copy()
    
cv2.drawContours(img_with_contours, contours, -1, (0, 255, 0), 3)

cv2.imshow("Original Image", img)
cv2.imshow("Binary Image (Input for Contours)", binary_image)
cv2.imshow("Image with Contours", img_with_contours)

cv2.waitKey(0)
cv2.destroyAllWindows()