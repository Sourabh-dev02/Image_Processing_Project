#read image using cv2 take input image
import cv2
import numpy as np
path=r'input\img1.png'
def read_image(path):
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5),cv2.BORDER_DEFAULT)
    ret, thresh = cv2.threshold(blur, 200, 255,cv2.THRESH_BINARY_INV)
    contours, hierarchies = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    blank = np.zeros(thresh.shape[:2],dtype='uint8')
    cv2.drawContours(blank, contours, -1,(255, 0, 0), 1)
    for i in contours:
        M = cv2.moments(i)
        if M['m00'] != 0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            cv2.drawContours(img, [i], -1, (0, 255, 0), 2)
            cv2.circle(img, (cx, cy), 7, (0, 0, 255), -1)
            cv2.putText(img, "center", (cx - 20, cy - 20),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
    return img

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
