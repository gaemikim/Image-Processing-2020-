# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 13:25:44 2020

@author: gaeeeemi
"""

import numpy as np

import matplotlib.pyplot as plt

import matplotlib.image as img

rgb = img.imread('Lenna.png')

num_bin = 100

x_values = np.linspace(0,1, num_bin)

red = rgb[:,:,0]

num_pixels = [np.shape(np.where(red<x))[1] for x in x_values]

prob_cdf = np.array(num_pixels) / red.size

plt.plot(x_values, prob_cdf)

hist = np.histogram(rgb)

hist, x = np.histogram(red+0.2, bins = 100)

plt.plot(x[1:], hist/red.size)