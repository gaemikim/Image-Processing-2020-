#%%
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 13:27:22 2020

@author: gaeeeemi
"""

import numpy as np

import matplotlib.pyplot as plt

import matplotlib.image as img

import math

Lenna = img.imread('C:/Users/Gaemi/Desktop/Python Files/Lenna.png')# 로컬에서 Lenna이미지 파일을 불러옵니다

mask_Prewitt = np.array([[[-1,-1,-1],[0,0,0],[1,1,1]],[[1,0,-1],[1,0,-1],[1,0,-1]]])#Prewitt 마스크 구현
mask_Roberts = np.array([[[-1,0,0],[0,1,0],[0,0,0]],[[0,0,-1],[0,1,0],[0,0,0]]])#Roberts 마스크 구현

def find_bnd(mask_size,original_img,mask_style):#경계선을 찾는 함수 구현
    bnd_img = np.copy(original_img)#함수의 매개변수로 입력된 이미지의 픽셀값들을 그대로 복사한 이미지 변수를 만듭니다
    bnd_img = bnd_img[:,:,0]#이미지 파일의 픽셀값은 r,g,b 3개의 레이어로 표현돼 있기 때문에 연산의 편의를 위해 하나의 레이어만 불러옵니다
    gray_img = original_img[:,:,0]#원본 이미지도 계산의 편의를 위해 하나의 레이어만 불러옵니다
    rows, cols = gray_img.shape#원본 이미지 픽셀의 행 수와 열 수를 불러옵니다
    bnd_mask_horizon = mask_style[0,:,:]#수평 경계선을 찾을 마스크 구현
    bnd_mask_vertical = mask_style[1,:,:]#수직 경계선을 찾을 마스크 구현
    guard = int((mask_size - 1)/2)#마스크 사이즈를 고려하여 Convolution연산을 할 때 필요한 연산 시작 좌표 확보를 위한 guard를 만듭니다
    for i in range(guard, rows - guard):#행 연산
        for j in range(guard, cols - guard):#열 연산
            bnd_horizon = np.sum(bnd_mask_horizon * gray_img[i - guard : i - guard + mask_size,j - guard : j - guard + mask_size])
            #수평 경계선 마스크와 이미지 픽셀을 각각 곱한 후 행렬 요소를 합해줍니다
            bnd_vertical = np.sum(bnd_mask_vertical * gray_img[i - guard : i - guard + mask_size,j - guard : j - guard + mask_size])
            #수직 경계선 마스크와 이미지 픽셀을 각각 곱한 후 행렬 요소를 합해줍니다
            bnd_img[i,j] = math.sqrt(bnd_horizon**2 + bnd_vertical**2)#수평 값과 수직 값을 제곱한 후 더하여 제곱근을 구해 해당 픽셀에 대입합니다
    return bnd_img#대입한 픽셀로 이루어진 이미지를 함수 리턴 값으로 받아옵니다

th = 0.12#경계선을 검출할 임계값을 설정합니다
img_bnd_th = np.where(find_bnd(3,Lenna,mask_Roberts) > th, 1, 0)#임계값보다 크다면 흰색(1), 그렇지 않은 경우엔 검은색(0)으로 표시합니다

plt.imshow(Lenna)#원본 이미지 출력
plt.show()

plt.imshow(img_bnd_th,cmap = 'gray')#경계선 검출 후 이미지 출력
plt.show()
'''
#교수님 코드
img = Lenna[:,:,0]

rows, cols = img.shape

mask_size = 3

guard = int((mask_size -1)/2)
            
mask_h = np.array([[-1,-1,-1],[0,0,0],[1,1,1]])
mask_v = np.array([[1,0,-1],[1,0,-1],[1,0,-1]])
img_boundary = np.zeros(img.shape, img.dtype)
for i in range(guard, rows - guard):
        for j in range(guard, cols - guard):
            img_sel = img[i - guard : i - guard + mask_size, j - guard : j - guard + mask_size]
            masked_h = np.sum(img_sel * mask_h)
            masked_v = np.sum(img_sel * mask_v)
            img_boundary[i,j] = np.sqrt(masked_h**2 + masked_v**2)
            
plt.imshow(img, cmap = 'gray')
plt.show()

th = 0.2
img_boundary_th = np.where(img_boundary < th, 1, 0)

plt.imshow(img_boundary_th, cmap = 'gray')
plt.show()
'''
# %%
