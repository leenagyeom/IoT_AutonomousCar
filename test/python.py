# Python 2/3 compatibility
from __future__ import print_function

import cv2
import numpy as np
import sys
import math
import serial
import time

port = "/dev/ttyACM0"
serialFromArduino = serial.Serial(port,9600)
serialFromArduino.flushInput()

def angle(dy,dx):
    return math.atan2(dy,dx)*180/math.pi

def roi(img, vertices):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(img, mask)
    return masked

#def line_detect(image):



if __name__ == '__main__':
    print(__doc__)

    cap = cv2.VideoCapture(0)

    while True:
        ret, src = cap.read()
        src = cv2.resize(src, (440,260))
        hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
        lower_blue = np.array([0, 0, 0])
        upper_blue = np.array([90, 90, 90])
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        res = cv2.bitwise_and(src, src, mask=mask)
        dst = cv2.GaussianBlur(src,(5,5),0)
        dst = cv2.Canny(src, 70, 210)
        #dst = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        row,col,ch=src.shape
        vertices = np.array([[0,260],[0,200],[140,150], [300,150],[440,200],[44$
        roi_img = roi(dst, [vertices])
        cdstP=np.copy(roi_img)
       # lines = cv2.HoughLinesP(cdstP, 1, math.pi/180.0, 100, np.array([]), 35$
        lines = cv2.HoughLinesP(hsv, 1, math.pi/180.0, 100, np.array([]), 35, 1$

        if lines is not None:
            a,b,c = lines.shape
            (d,e)=(row/2,row/2)
            (f,g)=(-1,-1)

            for i in range(a):
                (x1,y1,x2,y2) = (lines[i][0][0], lines[i][0][1], lines[i][0][2]$

                if max(y1,y2)>row/2 and min(x1,x2)<col/2 and angle(y2-y1,x2-x1)$
                    d = max(y1,y2)
                    f = i

                if max(y1,y2)>row/2 and min(x1,x2)>col/2 and angle(y2-y1,x2-x1)$
                    e = max(y1,y2)
                    g = i

            if f != -1:
                (x1,y1,x2,y2) = (lines[f][0][0], lines[f][0][1], lines[f][0][2]$
                print("left Side Angle = ", angle(x2-x1,y2-y1))
               # cv2.line(src, (x1,y1), (x2,y2), (0, 0, 255), 3, cv2.LINE_AA)
                cv2.line(hsv, (x1,y1), (x2,y2), (0, 0, 255), 3, cv2.LINE_AA)

                degree = angle(x2-x1,y2-y1)
                if degree > 130:
                    serialFromArduino.write(b'1')

            if g != -1:
                (x1,y1,x2,y2) = (lines[g][0][0], lines[g][0][1], lines[g][0][2]$
                print("Right Side Angle = ", angle(x2-x1,y2-y1))
                #cv2.line(src, (x1,y1), (x2,y2), (0, 0, 255), 3, cv2.LINE_AA)
                cv2.line(src, (x1,y1), (x2,y2), (0, 0, 255), 3, cv2.LINE_AA)
                degree = angle(x2-x1,y2-y1)

                if degree > 68:
                    serialFromArduino.write(b'2')
                    time.sleep(1)

        #cv2.imshow("detected lines", src)
        cv2.imshow("res", res)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()