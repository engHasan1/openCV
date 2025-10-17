import cv2

# Load the pre-trained Haar Cascade classifier for face detection
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# open the webcam (0 is usually the default camera)
cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read() # read a frame from the webcam
    if not ret:
        break
    else:
        # Convert the frame to grayscale as Haar Cascade works better on grayscale images
        gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        # Apply Gaussian blur to the grayscale frame to reduce noise and improve detection accuracy
        bluur_frame=cv2.GaussianBlur(gray_frame,(5,5),0)
        # Detect faces in the frame
        faces=face_cascade.detectMultiScale(bluur_frame,scaleFactor=1.1,minNeighbors=5)
        # Draw rectangles around the detected faces and label them
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(frame,'Face Detected',(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.9,(0,255,0),2)

        # Display the frame with detected faces
        cv2.imshow('Face Detection',frame)
        if cv2.waitKey(1)& 0xff==ord('q'):
            break
cap.release()
cv2.destroyAllWindows()
