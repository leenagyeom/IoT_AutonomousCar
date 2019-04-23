# -*- coding: utf-8 -*-
import cv2 # opencv ���
import numpy as np

def region_of_interest(img, vertices, color3=(255,255,255), color1=255): # ROI ����

    mask = np.zeros_like(img) # mask = img�� ���� ũ���� �� �̹���
    
    if len(img.shape) > 2: # Color �̹���(3ä��)��� :
        color = color3
    else: # ��� �̹���(1ä��)��� :
        color = color1
        
    # vertices�� ���� ����� �̷��� �ٰ����κ�(ROI �����κ�)�� color�� ä�� 
    cv2.fillPoly(mask, vertices, color)
    
    # �̹����� color�� ä���� ROI�� ��ħ
    ROI_image = cv2.bitwise_and(img, mask)
    return ROI_image

def mark_img(img, blue_threshold=200, green_threshold=200, red_threshold=200): # ��� ���� ã��

    #  BGR ���� ��
    bgr_threshold = [blue_threshold, green_threshold, red_threshold]

    # BGR ���� ������ ������ ����������
    thresholds = (image[:,:,0] < bgr_threshold[0]) \
                | (image[:,:,1] < bgr_threshold[1]) \
                | (image[:,:,2] < bgr_threshold[2])
    mark[thresholds] = [0,0,0]
    return mark

cap = cv2.VideoCapture('solidWhiteRight.mp4') # ������ �ҷ�����

while(cap.isOpened()):
    ret, image = cap.read()
    height, width = image.shape[:2] # �̹��� ����, �ʺ�

    # ��ٸ��� ������ Points
    vertices = np.array([[(50,height),(width/2-45, height/2+60), (width/2+45, height/2+60), (width-50,height)]], dtype=np.int32)
    roi_img = region_of_interest(image, vertices, (0,0,255)) # vertices�� ���� ���� �������� ROI �̹��� ����

    mark = np.copy(roi_img) # roi_img ����
    mark = mark_img(roi_img) # ��� ���� ã��

    # ��� ���� ������ �κ��� ���� image�� overlap �ϱ�
    color_thresholds = (mark[:,:,0] == 0) & (mark[:,:,1] == 0) & (mark[:,:,2] > 200)
    image[color_thresholds] = [0,0,255]

    cv2.imshow('results',image) # �̹��� ���
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Release
cap.release()
cv2.destroyAllWindows()