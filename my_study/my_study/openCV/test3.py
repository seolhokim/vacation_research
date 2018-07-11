#start button click
from PIL import ImageGrab
import numpy as np
import cv2
import pyautogui

def real_grab_screen(_driver = None):
    
    screen =  np.array((ImageGrab.grab(bbox=(10,30,350,650))) )
    image = real_process_img(screen)#processing image as required
    return image

def real_process_img(image):
    image = cv2.Canny(image, threshold1 = 100, threshold2 = 200)
    return  image 

#스타트버튼 클릭과 버튼있는지없는지 함수
def start_button_click():
    large_image = real_grab_screen()
    small_image = cv2.imread("./image_video/start_button.PNG",0)
    small_image = real_process_img(small_image)
    if exists(large_image, small_image,0.7):
        w,h = small_image.shape[::-1]
        min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(result)
        top_left = max_loc
        pyautogui.click(top_left[0]+w/2,top_left[1]+h/2)
def exists(image, template, thresh):
    """
    Returns True if template is in Image with probability of at least thresh
    :param image: 
    :param template: 
    :param thresh: 
    :return: 
    """
    digit_res = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(digit_res >= thresh)

    if len(loc[-1]) == 0:
        return False

    for pt in zip(*loc[::-1]):
        if digit_res[pt[1]][pt[0]] == 1:
            return False

    return True

def up_button_exists():
    large_image = real_grab_screen()
    small_image = cv2.imread("./image_video/up_button.PNG",0)
    small_image = real_process_img(small_image)
    
    return (exists(large_image,small_image,0.7))

print(up_button_exists())
