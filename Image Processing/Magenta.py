# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 14:09:38 2020

@author: gaeeeemi
"""

import numpy as np
import matplotlib.image as img
import matplotlib.pyplot as plt

color_array = np.zeros((200,200,3)) #색상 그래프를 표현할 3차원 행렬 생성
Magenta = np.copy(color_array) #Magenta색 그래프를 그려줄 변수에 color_array와 같은 크기의 그래프 복사
Magenta[:,:,[0, 2]] = 1 #Magenta색은 RGB중 Red와 Blue가 겹쳤을 때 나타나는 색이므로 0(Red), 2(Blue)에 값을 채워넣음
plt.imshow(Magenta)