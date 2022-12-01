# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 13:04:27 2020

@author: gaeeeemi
"""

import matplotlib.pyplot as plt
import numpy as np
import time

r = 200



#With Loop
start_time = time.time()
sq_y = np.ones((2*r, 2*r, 3))
sq_y[:,:,2] = 0

center_x = r
center_y = r

x = np.arange(2*r)
y = np.arange(2*r)

for i in x:
    for j in y:
        if(i-center_x)**2 + (j-center_y)**2 < r**2:
            sq_y[i,j,0:2] = 0
            sq_y[i,j,2] = 1

plt.imshow(sq_y)
plt.show()
end_time = time.time()
t = end_time - start_time
print(f"Time W/ Loop:{t}")



#Without Loop
start_time = time.time()
sq_y = np.ones((2*r, 2*r, 3))
sq_y[:,:,2] = 0

center_x = r
center_y = r

x = np.arange(2*r).reshape(1, 2*r)
y = np.arange(2*r).reshape(2*r, 1)

x_sq = np.repeat(x, 2*r, axis = 0)
y_sq = np.repeat(y, 2*r, axis = 1)

dist = np.sqrt((x_sq - center_x)**2 + (y_sq - center_y)**2)

idx = np.where(dist <= r)
x_idx = x_sq[idx]
y_idx = y_sq[idx]

sq_y[x_idx,y_idx, 0:2] = 0
sq_y[x_idx,y_idx,2] = 1

plt.imshow(sq_y)
plt.show()
end_time = time.time()
t = end_time - start_time
print(f"Time WO/ Loop:{t}")