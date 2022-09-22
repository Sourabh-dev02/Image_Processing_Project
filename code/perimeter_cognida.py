#read image using cv2 take input image
import cv2
import numpy as np
path=r'input\img1.png'
def read_image(path):
    img = cv2.imread(path,0)
    ret,thresh = cv2.threshold(img,127,255,0)
    contours,hierarchy = cv2.findContours(thresh, 1, 2)
    cnt = contours[0]
    M = cv2.moments(cnt)
    perimeter = cv2.arcLength(cnt,True)
    print(perimeter)
    image = cv2.putText(img, "Perimeter of input image: %d" %perimeter, (50,50), 1, 1, (0,255,0), 1, cv2.LINE_AA)
    return image

path2=r'input\img2.png'
path3=r'input\img3.png'
path4=r'input\img4.png'

cv2.imshow("output",read_image(path))
cv2.waitKey(3000)
cv2.imshow("output",read_image(path2))
cv2.waitKey(3000)
cv2.imshow("output",read_image(path3))
cv2.waitKey(3000)
cv2.imshow("output",read_image(path4))
cv2.waitKey(3000)
cv2.destroyAllWindows()
