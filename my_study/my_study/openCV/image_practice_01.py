import cv2
cat_img = cv2.imread("image_video/cat_1.jpg",0)
cv2.imshow('load image',cat_img)
key = cv2.waitKey(5) 
 
if key == ord('s'): #s키가 입력된거면 이미지 저장
 
    cv2.imwrite( 'gray_cat.jpg', cat_img )
 
 
cv2.destroyWindow( 'load image')
