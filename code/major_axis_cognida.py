import cv2
import numpy as np
import math
path=r'input\img1.png'
path2=r'input\img2.png'
path3=r'input\img3.png'
path4=r'input\img4.png'
def read_image(path2):
    img = cv2.imread(path2,0)
    ret,thresh = cv2.threshold(img,127,255,0)
    contours,hierarchy = cv2.findContours(thresh, 1, 2)
    cnt = contours[0]
    ellipse = cv2.fitEllipse(cnt)
    (xc,yc),(d1,d2),angle = ellipse
    result = img.copy()
    cv2.ellipse(result, ellipse, (0, 255, 0), 3)
    rmajor = max(d1,d2)/2
    if angle > 90:
        angle = angle - 90
    else:
        angle = angle + 90
    
    xtop = xc + math.cos(math.radians(angle))*rmajor
    ytop = yc + math.sin(math.radians(angle))*rmajor
    xbot = xc + math.cos(math.radians(angle+180))*rmajor
    ybot = yc + math.sin(math.radians(angle+180))*rmajor

    cv2.line(result, (int(xtop),int(ytop)), (int(xbot),int(ybot)), (255, 255, 0), 2)
    cv2.imwrite("output.jpg", result)

    cv2.imshow("output", thresh)
    cv2.imshow("output", result)
    cv2.waitKey(3000)
    cv2.destroyAllWindows()
    
read_image(path)
read_image(path2)
read_image(path3)
read_image(path4)