# -*- coding: utf-8 -*-
"""
Created on Wed May 13 13:28:59 2020

@author: gaeeeemi
"""

import numpy as np

import matplotlib.pyplot as plt

import matplotlib.image as img

Lenna = img.imread('C:/Users/Gaeeeemi1/AnacondaProjects/Lenna.png')

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
    return enl_img#원본 이미지 픽셀을 기준으로 받은 비율에 비례하는 정사각행렬의 범위만큼 원본 이미지 픽셀값을 대입합니다.

# def interpolation(original_img, ratio):
#     rows = original_img.shape[0]
#     cols = original_img.shape[1]
#     enl_rows = int(rows * ratio)
#     enl_cols = int(cols * ratio)

plt.imshow(Lenna)#원본 영상
plt.title('original')
plt.show()
r = 0.25
plt.imshow(enlarge(Lenna, r))#확대 영상
plt.title('x{}'.format(r))
plt.show()
