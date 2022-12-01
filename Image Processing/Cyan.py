# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 13:05:16 2020

@author: gaeeeemi
"""

import numpy as np
import matplotlib.image as img
import matplotlib.pyplot as plt

color_array = np.zeros((200,200,3)) #색상 그래프를 표현할 3차원 행렬 생성
Cyan = np.copy(color_array) #Cyan색 그래프를 그려줄 변수에 color_array와 같은 크기의 그래프 복사
Cyan[:,:,[1, 2]] = 1 #Cyan색은 RGB중 Grenn과 Blue가 겹쳤을 때 나타나는 색이므로 1(Green), 2(Blue)에 값을 채워넣음
plt.imshow(Cyan)