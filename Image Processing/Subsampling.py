# -*- coding: utf-8 -*-
"""
Created on Fri May 29 14:38:47 2020

@author: gaeeeemi
"""

import numpy as np

import matplotlib.pyplot as plt

import matplotlib.image as img

Airplane = img.imread('C:/Users/개미/AnacondaProjects/airplane.png')

Square = img.imread('C:/Users/개미/AnacondaProjects/sub_square.png')

#def subsampling(original_img, ratio):
#    sub_rows = int(original_img.shape[0] * ratio)
#    sub_cols = int(original_img.shape[1] * ratio)
#    sub_img = np.empty((sub_rows, sub_cols, 3))
#    rows = sub_img.shape[0]
#    cols = sub_img.shape[1]
#    for i in range(rows):
#        for j in range(cols):
#            for k in range(3):
#                sub_img[i, j, k] = original_img[int(1/ratio) * i, int(1/ratio) * j, k]
#    return sub_img

def enlarge(original_img, ratio):# enlarge라는 픽셀 확대 함수를 만듭니다.(parameter로 원본 이미지와 비율을 받습니다.)
    rows = original_img.shape[0]#원본 이미지 행렬의 행을 선언합니다.
    cols = original_img.shape[1]#원본 이미지 행렬의 열을 선업합니다.
    enl_rows = int(rows * ratio)
    enl_cols = int(cols * ratio)
    enl_img = np.empty((enl_rows, enl_cols, 3))#확대한 이미지를 받을 행렬을 생성합니다.
    divided_rows_idx = np.linspace(0, rows - 1, enl_rows)
    divided_rows_idx = divided_rows_idx.astype(int)
    divided_cols_idx = np.linspace(0, cols - 1, enl_cols)
    divided_cols_idx = divided_cols_idx.astype(int)
    for i in range(enl_rows):
        for j in range(enl_cols):
            for k in range(3):#R,G,B 3계층에 작업을 반복합니다.
                enl_img[i, j, k] = original_img[divided_rows_idx[i], divided_cols_idx[j], k]
    return enl_img

def blur_img(mask_size,original_img):#blurring 코드
    rows = original_img.shape[0]
    cols = original_img.shape[1]
    blurred_img = np.empty((rows, cols, 3))
    blurring_mask = np.ones((mask_size,mask_size), np.float32)/mask_size**2#blur마스크를 생성해줍니다.(각 인덱스값 = 1/mask_size**2)
    guard = int((mask_size - 1)/2)
    for i in range(guard, rows - guard):
        for j in range(guard, cols - guard):
            for k in range(3):
                blurred_img[i,j,k] = np.sum(blurring_mask * original_img[i - guard : i - guard + mask_size, j - guard : j - guard + mask_size, k])
            #맨 위에서 선언한 이미지 사이즈 배열에 연산한 인덱스 값을 넣어줍니다.
    return blurred_img

r = 0.25#축소 비율
#비행기 사진
plt.imshow(Airplane)
plt.title('Original')
plt.show()

plt.imshow(enlarge(Airplane, r))#축소
plt.title('Subsampling')
plt.show()

plt.imshow(blur_img(5, Airplane))#흐림 처리
plt.title('Blurred')
plt.show()

plt.imshow(enlarge(blur_img(5, Airplane), r))#흐림 처리 후 축소
plt.title('Blurred & Subsampling')
plt.show()

#사각형 이미지
plt.imshow(Square)
plt.title('Original')
plt.show()

plt.imshow(enlarge(Square, r))#축소
plt.title('Subsampling')
plt.show()

plt.imshow(blur_img(5, Square))#흐림 처리
plt.title('Blurred')
plt.show()

plt.imshow(enlarge(blur_img(5, Square), r))#흐림 처리 후 축소
plt.title('Blurred & Subsampling')
plt.show()