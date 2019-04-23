# -*- coding: utf-8 -*- # �ѱ� �ּ������� �̰� �ؾ���
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

image = cv2.imread('solidWhiteCurve.jpg') # �̹��� �б�
height, width = image.shape[:2] # �̹��� ����, �ʺ�

# ��ٸ��� ������ Points
vertices = np.array([[(50,height),(width/2-45, height/2+60), (width/2+45, height/2+60), (width-50,height)]], dtype=np.int32)
roi_img = region_of_interest(image, vertices) # vertices�� ���� ���� �������� ROI �̹��� ����

mark = np.copy(roi_img) # roi_img ����
mark = mark_img(roi_img) # ��� ���� ã��

cv2.imshow('roi_white',mark) # ��� ���� ���� ��� ���
cv2.imshow('result',image) # �̹��� ���
cv2.waitKey(0)