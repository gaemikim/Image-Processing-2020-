# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 18:19:04 2020

@author: gaeeeemi
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img

color_array = img.imread('apple.png')

rgb = color_array[:,:,0:3]

num_bin = 1000

x_values = np.linspace(0, 1, num_bin)

hist, x = np.histogram(rgb, bins = num_bin)

sum_hist = [np.sum(hist[:i]) for i in range(len(hist))]

n = np.array(sum_hist) / rgb.size

eq = np.copy(rgb)

for i in range(1, num_bin):
    idx = np.where((rgb > x_values[i-1])*(rgb < x_values[i]))
    eq[idx] = n[i]
    
hist_eq, x = np.histogram(eq, bins = num_bin)

plt.plot(x[1:], hist_eq, label = 'equalized rgb')
plt.legend(loc = 'upper right')
plt.show()

plt.imshow(eq)
plt.show()

plt.imshow(color_array)
plt.show()