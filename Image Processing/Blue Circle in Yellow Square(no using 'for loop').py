# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 21:37:21 2020

@author: gaeeeemi
"""

import numpy as np
import matplotlib.pyplot as plt
import time

start = time.time() #for문을 사용하지 않았을 때 실행시간을 측정하기 위한 시작점

r = 200 #그려줄 원의 반지름
center_x = r #원의 중심의 x좌표
center_y = r #원의 중심의 y좌표

square_yellow = np.zeros((2*r, 2*r, 3)) # 이미지를 그려줄 값이 없는 그래프 설정
square_yellow[:, :, 0:2] = 1 # 그래프의 영역을 노란색으로 칠함

x_array = 2*r*[np.arange(0, 2*r)] # 0~999까지 1의 간격으로 차례로 갖는 행렬 1000개를 요소로 가지는 list를 생성
x_array = np.array(x_array) # list형태인 x_array를 ndarray 형태로 변환
y_array = x_array.T # x_array의 전치행렬(행과 열을 서로 교체한 행렬)을 생성

circle_x = (x_array - r)**2 # x_array행렬의 각 index마다 r을 빼주고난 후 제곱한 값들의 행렬 생성. (x-r)**2 값들의 행렬
circle_y = (y_array - r)**2 # y_array행렬도 마찬가지로 생성
circle_index = np.where(circle_x + circle_y < r**2)
""""원 안의 범위에 속한 index(circle_index[0], circle_index[1])를 찾아줌
    circle_index[0]이 x(행)좌표들을 나열한 ndarray, circle_index[1]이 y(열)좌표들을 나열한 ndarray"""
"""원 내부 좌표 (x - a)**2 + (y - b)**2 < r**2 식을 만족하는 (픽셀)좌표를 찾기 위해 해주는 작업"""

square_yellow_circle_blue = np.copy(square_yellow) # square_yellow와 같은 크기의 그래프를 복사하여 파란 원을 그릴 최종 그래프 생성
square_yellow_circle_blue[circle_index[0], circle_index[1], 0:2] = 0 # 원 안의 좌표에서 Red와 Green영역의 값을 모두 지워줌
square_yellow_circle_blue[circle_index[0], circle_index[1], 2] = 1 # 원 안의 좌표에서 Blue영역에 값을 채워줌

plt.imshow(square_yellow_circle_blue) # 그래프 출력
end = time.time() # 실행시간 측정 종료
print(end - start) # 실행시간 출력