from PIL import ImageGrab
import numpy as np
import cv2


def grab_screen(_driver = None):
    
    screen =  np.array((ImageGrab.grab(bbox=(10,30,350,650))) )
    image = process_img(screen)#processing image as required
    #cv2.imshow("yes",image)
    #key = cv2.waitKey(5000)
    
    #if key == ord('s'): #s키가 입력된거면 이미지 저장
    #    cv2.destroyWindow(screen)
        
    return image

def process_img(image):
    #game is already in grey scale canvas, canny to get only edges and reduce unwanted objects(clouds)
    # resale image dimensions
    #image = cv2.resize(image, (0,0), fx = 0.5, fy = 0.5) 
    #crop out the dino agent from the frame
    
    #image = image[100:600,:] #img[y:y+h, x:x+w]
    #image = cv2.resize(image, (0,0), fx = 0.5, fy = 0.5) 
    image = cv2.Canny(image, threshold1 = 120, threshold2 = 250) #apply the canny edge detection
    return  image 


def grab_train():
    screen =  np.array((ImageGrab.grab(bbox=(10,300,300,500)))) 
    image = process_img(screen)#processing image as required
    #cv2.imshow("yes",image)
    #key = cv2.waitKey(3000)
    return image
import matplotlib.pyplot as plt
large_image = grab_screen()
small_image = cv2.imread("./image_video/start_button.PNG",0)
small_image = process_img(small_image)
w,h = small_image.shape[::-1]

methods = ['cv2.TM_CCOEFF']
methods = eval(methods[0])
result = cv2.matchTemplate(small_image, large_image,methods)

min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(result)
top_left = max_loc
bottom_right =(top_left[0]+w,top_left[1]+h)
#cv2.rectangle(large_image,top_left,bottom_right,255,5)

threshold = .8
loc = np.where(result >= threshold)
print(loc)
import pyautogui
pyautogui.click(top_left[0]+w/2,top_left[1]+h/2)


'''
x = 2520
y = 414
mouse.leftClick(x, y)
#키를 눌러주는 tool
import win32com.client
shell = win32com.client.Dispatch("WScript.Shell")
shell.SendKeys('asdasd')
'''


