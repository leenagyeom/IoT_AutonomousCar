import cv2
import numpy as np

  
cap = cv2.VideoCapture(0)
  
while True:

    ret, src = cap.read()
    hsv= cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) // ��Ȯ�ϰ� BGR
    lower_blue = np.array([0, 50, 50]) // �ּҰ� B G R ����
    upper_blue = np.array([20, 255, 255]) // �ִ밪
    mask = cv2.inRange(hsv, lower_blue, upper_blue) // �ν��� �� �ִ� �ּҹ����� �ִ����
    res = cv2.bitwise_and(src, src, mask=mask) // bitwize and �ϸ� ���� �͸� ã�� �������� ������.

  cv2.imshow('image', src)
  cv2.imshow('mask', mask)
  cv2.imshow('res', res)