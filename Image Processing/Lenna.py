# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 13:08:08 2020

@author: gaeeeemi
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img

Lenna = img.imread('Lenna.png')

num_bin = 100

x_values = np.linspace(0,1,num_bin)

red = Lenna[:,:,0]

num_pixels = [np.shape(np.where(red < x))[1] for x in x_values]

prob_cdf = np.array(num_pixels) / red.size

plt.plot(x_values, prob_cdf)

hist, x = np.histogram(red, num_bin)

plt.plot(x[1:], hist/red.size)

#hist2, x2 = np.histogram(red+0.2, num_bin)

#plt.plot(x[1:], hist/red.size)

#hist3, x3 = np.histogram(red * 1.2, num_bin)

#plt.plot(x[1:], hist/red.size)