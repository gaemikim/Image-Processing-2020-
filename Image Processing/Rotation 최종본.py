# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 16:45:53 2020

@author: Gaeeeemi1
"""

import numpy as np

import matplotlib.pyplot as plt

import matplotlib.image as img

import math

Image = img.imread('C:/Users/Gaeeeemi1/AnacondaProjects/seven.png')
Image_gray = Image[:,:,0]

rows = Image.shape[0]
cols = Image.shape[1]

angle = -150
angle_normal = angle / 180 * math.pi#Θ
angle_trans = (90 - angle) / 180 * math.pi#90 - Θ

Width = int(abs(rows * math.cos(angle_trans)) + abs(cols * math.cos(angle_normal)))#출력영상의 가로폭
Height = int(abs(rows * math.cos(angle_normal)) + abs(cols * math.cos(angle_trans)))#출력영상의 높이

Image_rot = np.empty([Height, Width])#최종 출력될 영상(패딩X)
Large_Image = np.empty([Height + rows, Width + cols])#입력으로 넣어 줄 영상 틀(패딩O)
Large_Image_rot = np.empty([Height + rows, Width + cols])#출력영상을 담을 틀(패딩O)

Large_rows = Large_Image.shape[0]#입력영상의 높이
Large_cols = Large_Image.shape[1]#입력영상의 가로폭

for r in range(rows):
    for c in range(cols):#입력으로 넣어 줄 영상 틀의 가운데 부분에 원본 영상을 대입(패딩 씌우기)
            Large_Image[r + math.ceil(Height/2), c + math.ceil(Width/2)] = Image_gray[r, c]

#영상을 주어진 각도에 따라 회전시켜 줄 식
rot_matrix = [[math.cos(angle_normal), -math.sin(angle_normal)], [math.sin(angle_normal), math.cos(angle_normal)]]
rot_matrix_inv = [[math.cos(angle_normal), math.sin(angle_normal)], [-math.sin(angle_normal), math.cos(angle_normal)]]

mid_x = math.ceil((Large_cols + 1)/ 2)#입력영상의 가로 중심점
mid_y = math.ceil((Large_rows + 1)/ 2)#입력영상의 세로 중심점

for r in range(Large_rows):#입력영상 높이만큼 반복
    for c in range(Large_cols):#입력영상 가로폭만큼 반복
            new_xy = np.array([c, Large_rows -1 -r])
            new_xy_shifted = new_xy - np.array([mid_x, mid_y])

            
            old_xy_shifted = np.matmul(rot_matrix_inv, new_xy_shifted)
            old_xy = old_xy_shifted + np.array([mid_x, mid_y])
            
            old_pxl_r = Large_rows -1 -old_xy[1]
            old_pxl_c = old_xy[0]
            
            old_pxl_r = np.round(old_pxl_r).astype(int)
            old_pxl_c = np.round(old_pxl_c).astype(int)
            if (old_pxl_r >= 0 and old_pxl_r < Height + rows) and (old_pxl_c >= 0 and old_pxl_c < Width + cols):
                    Large_Image_rot[r, c] = Large_Image[old_pxl_r, old_pxl_c]

for h in range(Height):
    for w in range(Width):#패딩을 씌운 영상에서 회전된 원본영상만 가져오기
        Image_rot[h, w] = Large_Image_rot[h + math.ceil(rows/2), w + math.ceil(cols/2)]
        
Image_rot = np.flip(Image_rot, axis = 1)#영상 반전

plt.imshow(Image_rot, cmap = 'gray')
plt.show()