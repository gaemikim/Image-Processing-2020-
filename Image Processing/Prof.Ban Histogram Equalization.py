# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 14:21:32 2020

@author: gaeeeemi
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img

color_array = img.imread('apple.png')

plt.imshow(color_array)

rgb = color_array[:,:,0:3]

r = rgb[:,:,0]

num_bin = 1000

x_values = np.linspace(0, 1, num_bin)

hist, x = np.histogram(r, bins = num_bin)

plt.plot(x[1:], hist)

sum_hist = [np.sum(hist[:i]) for i in range(len(hist))]

np.array(sum_hist)

plt.plot(sum_hist)

num_pixels = rgb.shape[0] * rgb.shape[1]

n = np.array(sum_hist) / num_pixels

plt.plot(x_values, n)

eq = np.copy(r)

for i in range(1, num_bin):
    idx = np.where((r > x_values[i-1])*(r < x_values[i]))
    eq[idx] = n[i]
    
eq_color = np.repeat(eq[:,:,np.newaxis], 3, axis = 2)

hist_eq, x = np.histogram(eq, bins = num_bin)

plt.plot(x[1:], hist_eq)

