import cv2
capture = cv2.VideoCapture(0)
while(True):
    ret, frame = capture.read()
    img_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    cv2.imshow("카메라 영상", img_gray)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
capture.release()
cv2.destroyWindow("카메라 영상")
