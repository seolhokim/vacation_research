from PIL import ImageGrab
import numpy as np
import cv2
def grab_screen(_driver = None):
    
    screen =  np.array((ImageGrab.grab(bbox=(18,120,550,1250))) )
    image = process_img(screen)#processing image as required
    cv2.imshow("yes",image)
    key = cv2.waitKey(5000)
    
    if key == ord('s'): #s키가 입력된거면 이미지 저장
 
      
        cv2.destroyWindow(screen)


def process_img(image):
    #game is already in grey scale canvas, canny to get only edges and reduce unwanted objects(clouds)
    # resale image dimensions
    #image = cv2.resize(image, (0,0), fx = 0.5, fy = 0.5) 
    #crop out the dino agent from the frame
    
    image = image[300:800,:] #img[y:y+h, x:x+w]
    image = cv2.resize(image, (0,0), fx = 0.5, fy = 0.5) 
    image = cv2.Canny(image, threshold1 = 100, threshold2 = 200) #apply the canny edge detection
    return  image 




grab_screen()


