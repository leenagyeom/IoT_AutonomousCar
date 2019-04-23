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



def draw_lines(img,lines,color=[0,0,255]):
    cv2.line(img,(x1,y1), (x2,y2), color, 3)



while (True):
    ret, src = cap.read()
    src = cv2.resize(src, (440, 260))
    dst = cv2.GaussianBlur(src,(5,5),0)
    dst = cv2.Canny(src, 50, 200, None, 3)
    row,col,ch=src.shape
    vertices=np.array([[0,260],[0,200],[140,150],[300,150],[440,200],[440,260]],dtype=np.int32) 
    ROI_dst=roi(dst,[vertices])
    lines=hough_lines(ROI_dst)



    if lines is not None:
        a,b,c = lines.shape
        e=row/2  
        (x1,y1,x2,y2) = (lines[0][0][0], lines[0][0][1], lines[0][0][2], lines[0][0][3])
                
        if angle(y2-y1,x2-x1)>0 and max(y1,y2)>e:
        #    print("Right Side Angle = ", angle(x2-x1,y2-y1))
            draw_lines(src,lines)
            degree = angle(x2-x1,y2-y1)
            if degree >63:
                serialFromArduino.write(b'2')
            elif degree <46.5:
                serialFromArduino.write(b'3')
        else:
            serialFromArduino.write(b'1')



    cv2.imshow("detected lines", src)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()