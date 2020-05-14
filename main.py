import cv2
import numpy as np
img=cv2.imread('T2.jpg')  #image loading  (enter the path of your image)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (7,7), 0)     #GAUSSAIAN BLUR
thresh=cv2.threshold(blur,200,255,cv2.THRESH_BINARY_INV)[1]
thresh_os=cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_BINARY_INV)[1]
thresh_OTSU=cv2.threshold(blur,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)[1]          #OSTU THRERSHOLDING

#dialation and opening
kernel=np.ones((5,5),np.uint8)       #KERNEL THAT I PASSED THROUGH THE IMAGE FOR THE DILATION PROCESS
dialate=cv2.dilate(thresh_OTSU,kernel,iterations=4)
opening=cv2.morphologyEx(thresh_OTSU,cv2.MORPH_OPEN,kernel,iterations=4) #this didnt worked for me


#forming boxes
contours = cv2.findContours(dialate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)    #HEICHEIRCHY SET TO EXTERNAL SO THAT ONLY THE PARENT CONTOUR SHOULD BE SHOWN
print(contours)
contours = contours[0] if len(contours) == 2 else contours[1]
for c in contours:
    x,y,w,h = cv2.boundingRect(c)
    cv2.rectangle(img, (x, y), (x + w, y + h), (36,255,12), 2)  #MAKING BOXES 


cv2.imshow('result',img)
cv2.imshow('thresh',dialate)
#cv2.imshow('threshos',thresh_os)
cv2.imshow('treshostu',thresh_OTSU)
cv2.waitKey()
