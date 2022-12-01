# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 21:28:55 2020

@author: gaeeeemi
"""

import numpy as np
import matplotlib.pyplot as plt
import time

start = time.time() #for문을 사용했을 때 실행시간을 측정하기 위한 시작점

r = 200 #그려줄 원의 반지름
center_x = r #원의 중심의 x좌표
center_y = r #원의 중심의 y좌표

x = np.arange(2*r) #for문에서 사용할 x축 범위 설정(0~999까지 1단위씩 arange)
y = np.arange(2*r) #for문에서 사용할 y축 범위 설정(0~999까지 1단위씩 arange)

square_yellow = np.zeros((2*r, 2*r, 3)) #이미지를 그려줄 값이 없는 그래프 설정
square_yellow[:, :, 0:2] = 1 #그래프의 영역을 노란색으로 칠함

for i in x: #x축의 값
    for j in y: #y축의 값
        if (i - center_x)**2 + (j - center_y)**2 <r**2:
            """원의 방정식에서 원 내부를 표현하는 (x - a)**2 + (y - b)**2 < r**2 식을 만족하는 
            (픽셀)좌표에만 파란색으로 표시"""
            square_yellow[i, j, 0:2] = 0 #노란색 지우기
            square_yellow[i, j, 2] = 1 #Blue영역 채우기
            
plt.imshow(square_yellow) #원하는 색으로 채워진 이미지 출력
end = time.time() #실행시간 측정 종료
print(end-start) #실행시간 출력