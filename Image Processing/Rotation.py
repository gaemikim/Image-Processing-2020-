# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 14:37:20 2020

@author: gaeeeemi
"""

import numpy as np

import matplotlib.pyplot as plt

import matplotlib.image as img

import math

Lenna = img.imread('C:/Users/Gaeeeemi1/AnacondaProjects/Lenna.png')
Lenna_gray = Lenna[:,:,0]

rows = Lenna.shape[0]
cols = Lenna.shape[1]

angle = -50
angle_normal = angle / 180 * math.pi#Θ
angle_trans = (90 - angle) / 180 * math.pi#90 - Θ

Width = int(abs(rows * math.cos(angle_trans)) + abs(cols * math.cos(angle_normal)))#출력영상의 가로폭
Height = int(abs(rows * math.cos(angle_normal)) + abs(cols * math.cos(angle_trans)))#출력영상의 높이

rows_gap = Height#원본 영상의 높이와 출력영상의 높이의 차이
cols_gap = Width#원본 영상의 가로폭과 출력영상의 가로폭의 차이

Lenna_rot = np.empty([Height, Width])#출력영상을 담을 틀
Large_Lenna = np.empty([Height + rows, Width + cols])#입력으로 넣어 줄 영상 틀

Large_rows = Large_Lenna.shape[0]#입력영상의 높이
Large_cols = Large_Lenna.shape[1]#입력영상의 가로폭

for r in range(rows):
    for c in range(cols):
            Large_Lenna[r + math.ceil(rows_gap/2), c + math.ceil(cols_gap/2)] = Lenna_gray[r, c]#입력으로 넣어 줄 영상 틀의 가운데 부분에 원본 영상을 대입

rot_matrix = [[math.cos(angle_normal), -math.sin(angle_normal)], [math.sin(angle_normal), math.cos(angle_normal)]]
rot_matrix_inv = [[math.cos(angle_normal), math.sin(angle_normal)], [-math.sin(angle_normal), math.cos(angle_normal)]]

first_mid_x = math.ceil((Large_cols + 1)/ 2)#입력영상의 가로 중심점
first_mid_y = math.ceil((Large_rows + 1)/ 2)#입력영상의 세로 중심점

second_mid_x = math.ceil((Width + 1)/ 2)
second_mid_y = math.ceil((Height + 1)/ 2)

for r in range(Large_rows):#출력영상 높이만큼 반복
    for c in range(Large_cols):#출력영상 가로폭만큼 반복
            new_xy = np.array([c, Large_rows -1 -r])
            new_xy_shifted = new_xy - np.array([first_mid_x, first_mid_y])
            
            old_xy_shifted = np.matmul(rot_matrix_inv, new_xy_shifted)
            old_xy = old_xy_shifted + np.array([second_mid_x, second_mid_y])
            
            old_pxl_r = Height -1 -old_xy[1]
            old_pxl_c = old_xy[0]
            
            old_pxl_r = np.round(old_pxl_r).astype(int)
            old_pxl_c = np.round(old_pxl_c).astype(int)
            if (old_pxl_r >= 0 and old_pxl_r < Height) and (old_pxl_c >= 0 and old_pxl_c < Width):
                Lenna_rot[r, c] = Large_Lenna[old_pxl_r, old_pxl_c]

plt.imshow(Lenna_rot, cmap = 'gray')
plt.show()