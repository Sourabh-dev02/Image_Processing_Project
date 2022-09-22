#read image using cv2 take input image
import cv2
import numpy as np
path=r'input\img1.png'
def read_image(path):
    img = cv2.imread(path,0)
    ret,thresh = cv2.threshold(img,127,255,0)
    contours,hierarchy = cv2.findContours(thresh, 1, 2)
    cnt = contours[0]
    (x,y),radius = cv2.minEnclosingCircle(cnt)
    center = (int(x),int(y))
    radius = int(radius)
    cv2.circle(img,center,radius,(0,255,0),2)
    # image = cv2.putText(img, "encapsulated by circle", (50,50), 1, 1, (0,255,0), 1, cv2.LINE_AA)
    return img

path2=r'input\img2.png'
def read_image(path2):
    img2 = cv2.imread(path2,0)
    ret2,thresh2 = cv2.threshold(img2,127,255,0)
    contours,hierarchy = cv2.findContours(thresh2, 1, 2)
    cnt2= contours[0]
    (x,y),radius = cv2.minEnclosingCircle(cnt2)
    center = (int(x),int(y))
    radius = int(radius)
    cv2.circle(img2,center,radius,(0,255,0),2)
    # image = cv2.putText(img, "encapsulated by circle", (50,50), 1, 1, (0,255,0), 1, cv2.LINE_AA)
    return img2
    

path3=r'input\img3.png'
def read_image(path3):
    img3 = cv2.imread(path3,0)
    ret3,thresh3 = cv2.threshold(img3,127,255,0)
    contours3,hierarchy = cv2.findContours(thresh3, 1, 2)
    cnt = contours3[0]
    (x,y),radius = cv2.minEnclosingCircle(cnt)
    center = (int(x),int(y))
    radius = int(radius)
    cv2.circle(img3,center,radius,(0,255,0),2)
    # image = cv2.putText(img, "encapsulated by circle", (50,50), 1, 1, (0,255,0), 1, cv2.LINE_AA)
    return img3

path4=r'input\img4.png'

def read_image(path4):
    img4 = cv2.imread(path4,0)
    ret4,thresh4 = cv2.threshold(img4,127,255,0)
    contours4,hierarchy = cv2.findContours(thresh4, 1, 2)
    cnt4 = contours4[0]
    (x,y),radius = cv2.minEnclosingCircle(cnt4)
    center = (int(x),int(y))
    radius = int(radius)
    cv2.circle(img4,center,radius,(0,255,0),2)
    # image = cv2.putText(img, "encapsulated by circle", (50,50), 1, 1, (0,255,0), 1, cv2.LINE_AA)
    return img4

cv2.imshow("output",read_image(path))
cv2.waitKey(3000)
cv2.imshow("output",read_image(path2))
cv2.waitKey(3000)
cv2.imshow("output",read_image(path3))
cv2.waitKey(3000)
cv2.imshow("output",read_image(path4))
cv2.waitKey(3000)
cv2.destroyAllWindows()
