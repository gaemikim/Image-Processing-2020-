# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 21:09:20 2020

@author: gaeeeemi
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img

color_array = img.imread('apple.png')# 이미지 불러오기

rgb = color_array[:,:,0:3]# 이미지 rgb값 불러오기

num_bin = 1000# bin 범위 생성

x_values = np.linspace(0, 1, num_bin)# x축 범위 생성

r = rgb[:,:,0]# red계열
g = rgb[:,:,1]# green계열
b = rgb[:,:,2]# blue 계열

hist_r, x_r = np.histogram(r, bins = num_bin)
hist_g, x_g = np.histogram(g, bins = num_bin)
hist_b, x_b = np.histogram(b, bins = num_bin)#히스토그램 생성

sum_hist_r = [np.sum(hist_r[:i]) for i in range(len(hist_r))]
sum_hist_g = [np.sum(hist_g[:i]) for i in range(len(hist_g))]
sum_hist_b = [np.sum(hist_b[:i]) for i in range(len(hist_b))]#누적 과정

n_r = np.array(sum_hist_r) / r.size
n_g = np.array(sum_hist_g) / g.size
n_b = np.array(sum_hist_b) / b.size#정규화 과정

plt.plot(x_values,n_r,'r',label = 'red cdf')
plt.plot(x_values,n_g,'g', label = 'green cdf')
plt.plot(x_values,n_b,'b', label = 'blue cdf')
plt.show()#cdf 출력

eq_r = np.copy(r)
eq_g = np.copy(g)
eq_b = np.copy(b)

for i in range(1, num_bin):
    idx = np.where((r > x_values[i-1])*(r < x_values[i]))
    eq_r[idx] = n_r[i]
    
for i in range(1, num_bin):
    idx = np.where((g > x_values[i-1])*(g < x_values[i]))
    eq_g[idx] = n_g[i]
    
for i in range(1, num_bin):
    idx = np.where((b > x_values[i-1])*(b < x_values[i]))
    eq_b[idx] = n_b[i]#픽셀 값 대체 과정
    
hist_eq_r, x_eq_r = np.histogram(eq_r, bins = num_bin)
hist_eq_g, x_eq_g = np.histogram(eq_g, bins = num_bin)
hist_eq_b, x_eq_b = np.histogram(eq_b, bins = num_bin)#평활화된 히스토그램 생성

eq = np.copy(rgb)

eq[:,:,0] = eq_r
eq[:,:,1] = eq_g
eq[:,:,2] = eq_b#평활화된 이미지 대입

hist_eq, x = np.histogram(eq, bins = num_bin)#통합 히스토그램 생성

plt.plot(x_r[1:], hist_r, 'k', label = 'original')
plt.plot(x_eq_r[1:], hist_eq_r, 'r', label = 'equalized red')
plt.legend(loc = 'upper right')
plt.show()

plt.plot(x_g[1:], hist_g, 'k', label = 'original')
plt.plot(x_eq_g[1:], hist_eq_g, 'g', label = 'equalized green')
plt.legend(loc = 'upper right')
plt.show()

plt.plot(x_b[1:], hist_b, 'k', label = 'original')
plt.plot(x_eq_b[1:], hist_eq_b, 'b', label = 'equalized blue')
plt.legend(loc = 'upper right')
plt.show()

plt.plot(x[1:], hist_eq, label = 'equalized')
plt.legend(loc = 'upper right')
plt.show()

plt.imshow(eq)
plt.show()

plt.imshow(color_array)
plt.show()