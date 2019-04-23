import cv2
import sys
import math
import numpy as np
import serial

port = "/dev/ttyACM0"
serialFromArduino = serial.Serial(port,9600)
serialFromArduino.flushInput()

def roi(img,vertices):
 mask=np.zeros_like(img)
 cv2.fillPoly(mask,vertices,255)
 masked=cv2.bitwise_and(img,mask)
 return masked

def angle(dy,dx):
    return math.atan2(dy,dx)*180/math.pi
    
cap = cv2.VideoCapture(0)

while (True):
    ret, src = cap.read()
    src = cv2.resize(src, (440, 260))
    dst = cv2.GaussianBlur(src,(5,5),0)
    dst = cv2.Canny(src, 50, 200, None, 3)
    row,col,ch=src.shape
    vertices=np.array([[0,260],[0,200],[140,150],[300,150],[440,200],[440,260]],dtype=np.int32) 
    ROI_dst=roi(dst,[vertices])
    lines = cv2.HoughLinesP(ROI_dst, 1, math.pi/180.0, 60, np.array([]), 35, 10)

    if lines is not None:
        a,b,c = lines.shape
        e=row/2    

        (x1,y1,x2,y2) = (lines[0][0][0], lines[0][0][1], lines[0][0][2], lines[0][0][3])
                
        if max(y1,y2)>row/2 and min(x1,x2)>col/2 and angle(y2-y1,x2-x1)>0 and max(y1,y2)>e:
            e = max(y1,y2)
            print("Right Side Angle = ", angle(x2-x1,y2-y1))
            degree = angle(x2-x1,y2-y1)
            cv2.line(src, (x1,y1), (x2,y2), (0, 0, 255), 3, cv2.LINE_AA) 
            if degree > 65:
                serialFromArduino.write(b'2')

    else:
        serialFromArduino.write(b'1')

    cv2.imshow("detected lines", src)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()