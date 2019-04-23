import cv2
import numpy as np

  
cap = cv2.VideoCapture(0)
  
while True:

    ret, src = cap.read()
    hsv= cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) // 정확하게 BGR
    lower_blue = np.array([0, 50, 50]) // 최소값 B G R 순서
    upper_blue = np.array([20, 255, 255]) // 최대값
    mask = cv2.inRange(hsv, lower_blue, upper_blue) // 인식할 수 있는 최소범위와 최대범위
    res = cv2.bitwise_and(src, src, mask=mask) // bitwize and 하면 같은 것만 찾고 나머지는 버린다.

  cv2.imshow('image', src)
  cv2.imshow('mask', mask)
  cv2.imshow('res', res)