#numpy speed testing

import numpy
import time

def trad_version():
  #numpy가 아닌 배열로 선언하였을 때 -> 약 9.3초
  t1 = time.time()
  X = range(10000000)
  Y = range(10000000)
  Z = []
  for i in range(len(X)):
    Z.append(X[i] + Y[i])
  return time.time() - t1

def numpy_version():
  #numpy 배열로 선언하였을 때 -> 약 0.5초
  t1 = time.time()
  X = numpy.arange(10000000)
  Y = numpy.arange(10000000)
  Z = X + Y
  return time.time() - t1

print(trad_version())
print(numpy_version())