#!/usr/bin/env python
import numpy as np
import cv2 as cv

vc = cv.VideoCapture(0)
cv.namedWindow("Let's Play!")
rval=True
img_name = "opencv_frame_0.png"
if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
    cv.imwrite(img_name, frame)
    print("{} written!".format(img_name))
else:
    rval = False


if(rval):
    img = cv.imread(img_name,0)
    img = cv.medianBlur(img,5)
    cimg = cv.cvtColor(img,cv.COLOR_GRAY2BGR)
    circles = cv.HoughCircles(img,cv.HOUGH_GRADIENT,1,20,
                                param1=50,param2=30,minRadius=0,maxRadius=0)
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        # draw the outer circle
        cv.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        cv.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
    cv.imshow('detected circles',cimg)
else:
    print("not captured image")
cv.waitKey(0)
cv.destroyAllWindows()