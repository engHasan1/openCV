import cv2

img=cv2.imread('images/img.png')

if img is None :
    print('image not found')
else:
    # images properties
    print('image properties')
    (h,w,c)=img.shape
    print('height:{}'.format(h))
    print('width:{}'.format(w))
    print('channels:{}'.format(c))
    print('image size:{}'.format(img.size))
    print('image datatype:{}'.format(img.dtype))

    # Accessing a specific pixel and editing it

    img[:,:10]=[0,0,0]
    img[:10,:]=[0,0,0]
    img[:,-10:]=[0,0,0]
    img[-10:,:]=[0,0,0]

    img[h//2-100:h//2+100,w//2-100:w//2+100]=[255,255,255]


    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    