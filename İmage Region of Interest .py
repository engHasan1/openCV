import cv2 

img=cv2.imread('images/img.png')

if img is None :
    print('image not found')
else:
    # The general formula (roi = image[startY:endY, startX:endX])
    Roi=img[90:270,110:610]

    cv2.imshow('Original Image',img)
    cv2.imshow('Region of Interest',Roi)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


    