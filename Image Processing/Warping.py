# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 13:11:17 2020

@author: gaeeeemi
"""

import numpy as np

import matplotlib.pyplot as plt

import matplotlib.image as img

import math

Lenna = img.imread('C:/Users/Gaeeeemi1/AnacondaProjects/Lenna.png')
Lenna_gray = Lenna[:, :, 0]

rows = Lenna_gray.shape[0]
cols = Lenna_gray.shape[1]

Warped_Lenna = np.empty([rows, cols])#와핑될 레나 영상

amp = 73#진폭
frq = 1/45#주파수

x = np.linspace(0, cols -1, cols)
out_graph = math.ceil(np.max(amp*np.sin(frq*x)))#영상 범위 밖으로 나가는 부분

Large_Lenna = np.empty([rows + (2*out_graph), cols])#영상 범위 밖으로 나가는 부분까지 받아줄 클 영상

Large_rows = Large_Lenna.shape[0]
Large_cols = Large_Lenna.shape[1]

for c in range(cols):
    upper_graph = amp*math.sin(frq*c)#영상 위쪽의 그래프
    under_graph = rows - upper_graph#영상 아래쪽의 그래프
    warp_rows = int(under_graph - upper_graph)#와핑 된 rows길이
    rows_gap = Large_rows - warp_rows#와핑 된 rows길이와 원본 영상rows길이의 차이
    divided_rows_idx = np.linspace(0, rows - 1, warp_rows)#원본 영상 길이를 와핑된rows길이 만큼 축소or확장 
    divided_rows_idx = divided_rows_idx.astype(int)#정수화
    for r in range(warp_rows):#축소or확장된 와핑된 영상 index를 큰 영상에 대입
        Large_Lenna[r + int(rows_gap/2), c] = Lenna_gray[divided_rows_idx[r], c]

for r in range(rows):
    for c in range(cols):#큰 영상에서 원본 영상 크기 사이즈 바깥으로 나가는 부분을 잘라내고 대입
        Warped_Lenna[r, c] = Large_Lenna[r + int((Large_rows - rows)/2), c]
        
plt.imshow(Warped_Lenna, cmap = 'gray')