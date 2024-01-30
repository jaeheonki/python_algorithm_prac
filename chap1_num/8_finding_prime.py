#여러가지 방법을 이용하여 소수 찾아보기
import math
import random


def finding_prime(number):
  # 무차별 대입 -> 2~ num까지의 수를 모두 나누어봄
  num = abs(number)  #abs(num) -> num의 절대 값 반환
  if num < 4 : return True
  for x in range(2, num):
    if num % x == 0:
      return False  # num / 2 까지만 했어도 저장공간 단축 가능 했을 듯,,


def finding_prime_sqrt(number):
  #제곱근 활용
  num = abs(number)
  if num < 4: return True
  for x in range(2, int(math.sqrt(num)) + 1):
    if number % x == 0:
      return False
  return True


def finding_prime_fermat(number):
  if number <= 102:
    for a in range(2, number):
      if pow(a, number - 1, number) != 1:
        return False
      return True


num1, num2 = 17, 20
print(finding_prime(num1))
print(finding_prime(num2))
print(finding_prime_sqrt(num1))
print(finding_prime_sqrt(num2))
print(finding_prime_fermat(num1))
print(finding_prime_fermat(num2))
