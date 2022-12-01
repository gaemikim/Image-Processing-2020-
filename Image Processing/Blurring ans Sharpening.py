# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 14:04:51 2020

@author: gaeeeemi
"""

import numpy as np

import matplotlib.pyplot as plt

import matplotlib.image as img

Lenna = img.imread('C:/Users/개미/AnacondaProjects/Lenna.png')
#일반화하지 않은 코드
'''
blurred_img = Lenna[:,:,0]

rows, cols = blurred_img.shape
mask_size = 5

mask_center = int(mask_size/2 - 0.5)

blurring_mask = np.ones((mask_size,mask_size),dtype = np.float32)/mask_size**2

guard = int((mask_size - 1)/2)
#blurred_img = np.copy(Lenna)

for i in range(guard, rows - guard):
    for j in range(guard, cols - guard):
        blurred_img[i,j] = np.sum(blurring_mask * blurred_img[i - guard : i - guard + mask_size,j - guard : j - guard + mask_size])

sharpening_mask = np.ones((mask_size,mask_size),dtype = np.float32)*-1
sharpening_mask[mask_center,mask_center] = mask_size**2
sharped_img = np.copy(Lenna)

for i in range(guard, rows - guard):
    for j in range(guard, cols - guard):
        sharped_img[i,j] = np.sum(sharpening_mask * blurred_img[i - guard : i - guard + mask_size,j - guard : j - guard + mask_size])
'''
#일반화 코드
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

def sharpen_img(mask_size,original_img, blurred_img):#sharpening 코드
    sharped_img = np.copy(original_img)#연산한 인덱스값을 넣어줄 원본 이미지 사이즈를 불러옵니다.
    rows = blurred_img.shape[0]#3차원 배열의 행을 지정해줍니다.
    cols = blurred_img.shape[1]#3차원 배열의 열을 지정해줍니다.
    mask_center = int(mask_size/2 - 0.5)#마스크의 중간값의 위치를 찾아줍니다.
    sharpening_mask = np.ones((mask_size,mask_size), np.float32)*-1#모든 인덱스가 -1인 마스크를 만듭니다.
    sharpening_mask[mask_center,mask_center] = mask_size**2#중간값만 mask_size의 제곱으로 바꿔줍니다.
    guard = int((mask_size - 1)/2)
    for i in range(guard, rows - guard):
        for j in range(guard, cols - guard):
            sharped_img[i,j] = np.sum(sharpening_mask * blurred_img[i - guard : i - guard + mask_size,j - guard : j - guard + mask_size])
            #맨 위에서 선언한 이미지 사이즈 배열에 연산한 인덱스 값을 넣어줍니다.
    return sharped_img

plt.imshow(Lenna)
plt.title('original')
plt.show()
plt.imshow(blur_img(5,Lenna),cmap='gray')
plt.title('blurred')
plt.show()
plt.imshow(sharpen_img(5,Lenna,blur_img(5,Lenna)),cmap='gray')
plt.title('sharpened')
plt.show()

