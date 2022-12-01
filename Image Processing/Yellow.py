# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 14:10:47 2020

@author: gaeeeemi
"""

import numpy as np
import matplotlib.image as img
import matplotlib.pyplot as plt

color_array = np.zeros((200,200,3)) #색상 그래프를 표현할 3차원 행렬 생성
Yellow = np.copy(color_array) #Yellow색 그래프를 그려줄 변수에 color_array와 같은 크기의 그래프 복사
Yellow[:,:,[0,1]] = 1 #Yellow색은 RGB중 Red와 Green가 겹쳤을 때 나타나는 색이므로 0(Red), 1(Green)에 값을 채워넣음
plt.imshow(Yellow)