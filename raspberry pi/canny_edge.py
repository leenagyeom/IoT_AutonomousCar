# -*- coding: utf-8 -*- # �ѱ� �ּ������� �̰� �ؾ���
import cv2 # opencv ���
import numpy as np

def grayscale(img): # ����̹����� ��ȯ
    return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

def canny(img, low_threshold, high_threshold): # Canny �˰���
    return cv2.Canny(img, low_threshold, high_threshold)

def gaussian_blur(img, kernel_size): # ����þ� ����
    return cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)

image = cv2.imread('a1.jpg') # �̹��� �б�
height, width = image.shape[:2] # �̹��� ����, �ʺ�

gray_img = grayscale(image) # ����̹����� ��ȯ

blur_img = gaussian_blur(gray_img, 3) # Blur ȿ��

canny_img = canny(blur_img, 70, 210) # Canny edge �˰���

cv2.imshow('result',canny_img) # Canny �̹��� ���
cv2.waitKey(0) #�̹����� ��� ��� ���δ� ����