import cv2
import numpy as np


img = cv2.imread('images/limon.png')    

hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
lower_green = np.array([25, 40, 40])
upper_green = np.array([95, 255, 255])
    
initial_mask = cv2.inRange(hsv_img, lower_green, upper_green)

kernel = np.ones((5, 5), np.uint8)

opening_mask = cv2.morphologyEx(initial_mask, cv2.MORPH_OPEN, kernel)
    
closing_mask = cv2.morphologyEx(initial_mask, cv2.MORPH_CLOSE, kernel)


cv2.imshow("1. Initial Mask (Noisy)", initial_mask)
cv2.imshow("2. Opening Result (Removes noise)", opening_mask)
cv2.imshow("3. Closing Result (Fills holes)", closing_mask)
    
cv2.waitKey(0)
cv2.destroyAllWindows()