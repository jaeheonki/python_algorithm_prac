#random 모듈 실습하기

import random


def testing_random():
  values = [1, 2, 3, 4, 5, 6]
  print(random.choice(values))
  print(random.choice(values))
  print(random.choice(values))
  print(random.sample(values, 2))
  print(random.sample(values, 3))

  #리스트 섞기
  random.shuffle(values)
  print(values)

  #랜덤 정수 생성
  print(random.randint(0, 10))
  print(random.randint(0, 1000))


testing_random()
