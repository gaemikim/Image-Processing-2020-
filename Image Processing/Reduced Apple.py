# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 13:48:59 2020

@author: gaeeeemi
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img

file_name = "Apple.png"
Apple = img.imread(file_name)
rgb = Apple[:,:,0:3]

height = rgb.shpae[0]
width = rgb.shape[1]

ratio_height = 2;
ratio_width = 1.1

new_height = np.int(np.floor(height/ratio_height))
new_width = np.int(np.floor(width/ratio_width))

new_rgb = np.zeros((new_height,new_width,3))

for i in range(0, new_height):
    for j in range(0, new_width):
        new_rgb[i,j,0] = rgb[np.int(np.round(ratio_height*i)), np.int(np.round(ratio_width*j)),0]
        new_rgb[i,j,1] = rgb[np.int(np.round(ratio_height*i)), np.int(np.round(ratio_width*j)),1]
        new_rgb[i,j,2] = rgb[np.int(np.round(ratio_height*i)), np.int(np.round(ratio_width*j)),2]
plt.imshow(rgb)
plt.show()

plt.imshow(new_rgb)
plt.show()