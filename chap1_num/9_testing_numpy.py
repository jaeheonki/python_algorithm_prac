import numpy as np
#numpy package testing/practice


def testing_numpy():
  ax = np.array([1, 2, 3])  #np.array(list) -> 1차원 배열
  ay = np.array([3, 4, 5])
  print(ax)
  print(ax * 2)  #배열의 원소에 2를 곱함
  print(ax + 10)
  print(np.sqrt(ax))  #배열의 원소에 루트를 씌우기
  print(np.cos(ax))  #배열의 원소에 cos를 취함
  print(ax - ay)
  print(np.where(ax < 2, ax, 10))  #ax<2가 참이면 ax, 거짓이면 10으로 array를 바꾼다.

  m = np.matrix([ax, ay, ax])  #1차원 배열 3개로 2차원 배열을 만듬
  print(m.ndim)  #차원의 개수
  print(m)
  print(m.T)  #m의 전치행렬을 구해줌

  grid1 = np.zeros(
      shape=(10, 10),
      dtype=float)  #shape가 10, 10인 0으로 가득찼으며, type은 float인 행렬을 만들어줌
  grid2 = np.ones(
      shape=(10, 10),
      dtype=float)  #shape가 10, 10인 1 으로 가득찼으며, type은 float인 행렬을 만들어줌
  print(grid1)
  print(grid2)
  print(grid1[1] + 10)
  print(grid2[:, 2] * 2)  #배열 슬라이싱


testing_numpy()
