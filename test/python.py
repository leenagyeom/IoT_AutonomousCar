import cv2
import sys
import math
import numpy as np
import serial
import time

port = "/dev/ttyACM0"
serialFromArduino = serial.Serial(port,9600)
serialFromArduino.flushInput()

cap = cv2.VideoCapture(0)



flag_one = 0
flag_two = 0
flag_three = 0



def roi(img,vertices):
 mask=np.zeros_like(img)
 cv2.fillPoly(mask,vertices,255)
 masked=cv2.bitwise_and(img,mask)
 return masked

def angle(dy,dx):
    return math.atan2(dy,dx)*180/math.pi

def hough_lines(img):
    lines=cv2.HoughLinesP(img,1,math.pi/180.0,50,None,35,10)
    return lines

def initial(src):
    dst = cv2.GaussianBlur(src,(5,5),0)
    dst = cv2.Canny(src, 50, 200, None, 3)
    vertices=np.array([[0,260],[0,200],[140,150],[300,150],[440,200],[440,260]],dtype=np.int32) 
    ROI_dst=roi(dst,[vertices])
    lines=hough_lines(ROI_dst)
    return lines

def To_Arduino(src,lines):
    a,b,c = lines.shape
    (x1,y1,x2,y2) = (lines[0][0][0], lines[0][0][1], lines[0][0][2], lines[0][0][3])
                
    if angle(y2-y1,x2-x1)>0 and max(y1,y2)>130:
           
        print("Right Side Angle = ", angle(x2-x1,y2-y1))
        cv2.line(src,(x1,y1), (x2,y2), [0,0,255], 3)
        degree = angle(x2-x1,y2-y1)
        if degree >63:
            global flag_two
            flag_two = flag_two+1
            if flag_two==13:
                serialFromArduino.write(b'2')
                flag_two = 0
        elif degree <46.5:
            global flag_three
            flag_three = flag_three+1
            if flag_three==13:
                serialFromArduino.write(b'3')
                flag_three = 0
    else:
        global flag_one
        flag_one = flag_one+1
        if flag_one==13:
            serialFromArduino.write(b'1')
            flag_one = 0

while (True):
    ret, src = cap.read()
    src = cv2.resize(src, (440, 260))
    lines=initial(src)
    
    if lines is not None:
        To_Arduino(src,lines)

    cv2.imshow("detected lines", src)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()