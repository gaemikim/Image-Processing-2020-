# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 13:28:05 2020

@author: gaeeeemi
"""

import numpy as np
import matplotlib.image as img
import matplotlib.pyplot as plt
import time


def Runtime_Loop(r):
    start = time.time()
    center_x = r
    center_y = r
    x = np.arange(0, 2*r)
    y = np.arange(0, 2*r)
    square_yellow = np.zeros((2*r, 2*r, 3))
    square_yellow[:, :, 0:2] = 1
    for i in x:
        for j in y:
            if (i - center_x)**2 + (j - center_y)**2 < r**2:
                square_yellow[i, j, 0:2] = 0
                square_yellow[i, j, 2] = 1
    end = time.time()
    t = end - start
    return(t)
    
def Runtime_NoLoop(r):
    start = time.time()
        
    center_x = r
    center_y = r
    
    square_yellow = np.zeros((2*r, 2*r, 3))
    square_yellow[:, :, 0:2] = 1
    
    x_array = 2*r*[np.arange(0, 2*r)]
    x_array = np.array(x_array)
    y_array = x_array.T
    
    circle_x = (x_array - r)**2
    circle_y = (y_array - r)**2
    
    circle_index = np.where(circle_x + circle_y < r**2)
    
    square_yellow_circle_blue = np.copy(square_yellow)
    
    square_yellow_circle_blue[circle_index[0], circle_index[1], 0:2] = 0
    square_yellow_circle_blue[circle_index[0], circle_index[1], 2] = 1
    
    end = time.time()
    t = end - start
    return (t)

r_list = [100, 200, 300, 400, 500]
t_list_Loop = list()
t_list_NoLoop = list()

for i in r_list:
    t_list_Loop.append(Runtime_Loop(i))
    t_list_NoLoop.append(Runtime_NoLoop(i))
plt.plot(r_list, t_list_Loop, 'b', marker = 's', label = 'Runtime with Loop')
plt.plot(r_list, t_list_NoLoop, 'r', marker = 'o', label = 'Runtime without Loop')
plt.title('Runtime Comparison')
plt.xlabel('radius[pixel]')
plt.ylabel('Runtime[sec]')
plt.legend()