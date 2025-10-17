import cv2
from matplotlib import pyplot as plt


img = cv2.imread('images/limon.png')

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
gray_hist = cv2.calcHist([gray_img], [0], None, [256], [0, 256])

colors = ('b', 'g', 'r')
plt.figure() 
plt.title("Color Histogram")
plt.xlabel("Bins (Intensity)")
plt.ylabel("# of Pixels")

for i, col in enumerate(colors):
    color_hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(color_hist, color=col)
    plt.xlim([0, 256])


plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins (Intensity)")
plt.ylabel("# of Pixels")
plt.plot(gray_hist)
plt.xlim([0, 256]) 
    

plt.show()

cv2.imshow("Original Image", img)
cv2.imshow("Grayscale Image", gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()