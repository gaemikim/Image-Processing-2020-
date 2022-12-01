# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 13:20:50 2020

@author: gaeeeemi
"""

import numpy as np

import matplotlib.pyplot as plt

import matplotlib.image as img

ant = img.imread('C:/Users/Gaeeeemi1/AnacondaProjects/ant.png')

Bolt = img.imread('C:/Users/Gaeeeemi1/AnacondaProjects/Bolt.png')

cell = img.imread('C:/Users/Gaeeeemi1/AnacondaProjects/cell.png')

def erode(mask_size, original_img):
    erd_img = np.copy(original_img)
    gray_img = np.copy(original_img)
    rows = gray_img.shape[0]
    cols = gray_img.shape[1]
    erd_mask = np.ones((mask_size,mask_size))
    guard = int((mask_size - 1)/2)
    for i in range(guard, rows - guard):
        for j in range(guard, cols - guard):#배경이 흰색이라 최대값 찾아서 픽셀값 바꿔줌(배경이 흰색 물체가 검은색일 경우에만)
            erd_img[i,j,0] = np.max(erd_mask * gray_img[i - guard : i - guard + mask_size, j - guard : j - guard + mask_size,0])
            erd_img[i,j,1] = np.max(erd_mask * gray_img[i - guard : i - guard + mask_size, j - guard : j - guard + mask_size,1])
            erd_img[i,j,2] = np.max(erd_mask * gray_img[i - guard : i - guard + mask_size, j - guard : j - guard + mask_size,2])
    return erd_img

def expansion(mask_size, original_img):
    exp_img = np.copy(original_img)
    gray_img = np.copy(original_img)
    rows = gray_img.shape[0]
    cols = gray_img.shape[1]
    exp_mask = np.ones((mask_size,mask_size))
    guard = int((mask_size - 1)/2)
    for i in range(guard, rows - guard):
        for j in range(guard, cols - guard):
            exp_img[i,j,0] = np.min(exp_mask * gray_img[i - guard : i - guard + mask_size, j - guard : j - guard + mask_size,0])
            exp_img[i,j,1] = np.min(exp_mask * gray_img[i - guard : i - guard + mask_size, j - guard : j - guard + mask_size,1])
            exp_img[i,j,2] = np.min(exp_mask * gray_img[i - guard : i - guard + mask_size, j - guard : j - guard + mask_size,2])
    return exp_img

def reduce_img(img, ratio):#ratio는 몇 배로 줄일건지에 대한 매개변수
    rows = img.shape[0]
    cols = img.shape[1]
    new_h = np.int(np.floor(rows / ratio))
    new_w = np.int(np.floor(cols / ratio))
    
    new_rgb = np.zeros((new_h, new_w, 3))
    for i in range(new_h):
        for j in range(new_w):
            new_rgb[i,j,0] = img[np.int(np.round(ratio * i)), np.int(np.round(ratio * j)), 0]
            new_rgb[i,j,1] = img[np.int(np.round(ratio * i)), np.int(np.round(ratio * j)), 1]
            new_rgb[i,j,2] = img[np.int(np.round(ratio * i)), np.int(np.round(ratio * j)), 2]
    return new_rgb

def img_bin(img, th):
    img_binaried = np.where(img > th, 1.0, 0.0)#th값보다 크면 1.0(백) 아니면 0.0(흑)
    return img_binaried

def mul_erode(mask_size, original_img, number):
    list = [original_img]
    for i in range(number):
        eroded_img = erode(mask_size, list[0])
        list[0] = eroded_img
    return list[0]


def mul_expansion(mask_size, original_img, number):
    list = [original_img]
    for i in range(number):
        expanded_img = expansion(mask_size, list[0])
        list[0] = expanded_img
    return list[0]

'''
plt.imshow(img_bin(ant[:,:,0], 0.5), cmap = 'gray')
plt.show()

A = erode(3,img_bin(reduce_img(ant, 2),0.5))
plt.imshow(A[:,:,0],cmap = 'gray')
plt.show()

B = mul_erode(3,img_bin(reduce_img(ant, 2),0.5),2)
plt.imshow(B[:,:,0],cmap = 'gray')
plt.show()

C = expansion(3,B)
plt.imshow(C, cmap = 'gray')
plt.show()

plt.imshow(img_bin(Bolt[:,:,0], 0.5), cmap = 'gray')
plt.show()

D = mul_expansion(3, img_bin(reduce_img(Bolt,2), 0.5), 2)
plt.imshow(D[:,:,0], cmap = 'gray')
plt.show()

E = mul_erode(3, D, 2)
plt.imshow(E, cmap = 'gray')
plt.show()
'''
#열림 연산
plt.imshow(img_bin(cell[:,:,0], 0.5), cmap = 'gray')
plt.show()

F = mul_expansion(3, mul_erode(3, img_bin(reduce_img(cell,2), 0.5), 2), 2)
plt.imshow(F[:,:,0], cmap = 'gray')
plt.show()