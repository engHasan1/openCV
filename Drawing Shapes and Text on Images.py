import cv2 

img=cv2.imread('images/img.png')

# # Drawing a Line
# cv2.line(img,(0,180),(720,180),(255,255,255),5)
# cv2.imshow('Image with Line',img)

# # Drawing a Rectangle
# cv2.rectangle(img,(110,30),(610,330),(255,255,255),5)
# cv2.imshow('Image with Rectangle',img)

# # Drawing a Circle
# h,w=img.shape[:2]
# cv2.circle(img,(w//2,h//2),100,(255,255,255),5)
# cv2.imshow('Image with Circle',img)

# Writing Text on Image
cv2.putText(img,'OpenCV Lib.',(10,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
cv2.imshow('Image with Text',img)

cv2.waitKey(0)
cv2.destroyAllWindows()