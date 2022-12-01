# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 13:38:27 2020

@author: gaeeeemi
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
color_array = img.imread('C:/Users/Gaemi/Desktop/Python Files/Image Processing/Images/Apple.png') #이미지 불러오기
plt.imshow(color_array)
plt.show() #이미지 원본 출력

color_array_R = np.copy(color_array)
color_array_R[:,:,[1,2]] = 0 #RGB중 Red영역만을 표현하기 위해 Green, Blue 영역을 0으로 환산
plt.imshow(color_array_R)
plt.show() #이미지의 Red영역 출력

color_array_G = np.copy(color_array)
color_array_G[:,:,[0,2]] = 0 #RGB중 Green영역만을 표현하기 위해 Red, Blue 영역을 0으로 환산
plt.imshow(color_array_G)
plt.show() #이미지의 Green영역 출력

color_array_B = np.copy(color_array)
color_array_B[:,:,[0,1]] = 0 #RGB중 Blue영역만을 표현하기 위해 Red, Green 영역을 0으로 환산
plt.imshow(color_array_B) #이미지의 Blue영역 출력