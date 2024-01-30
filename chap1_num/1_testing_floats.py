#fraction 모듈 실습

from fractions import Fraction

def rounding_floats(number1, places):
  return round(number1, places) # round : 소숫점 맞춰 반올림 -> places 소숫점 자리까지 맞춰 반올림

def float_to_fractions(number):
  #소수를 분수로 반환
  return Fraction(*number.as_integer_ratio())
  #as_integer_ratio() : 메소드를 사용하여 주어진 부동 소수점 숫자의 분자와 분모를 얻는다
 # * 연산자가 튜플을 언패킹하여 인수로 전달
def get_denominator(number1, number2):
  # 분모 반환
  a = Fraction(number1, number2)
  # a가 num1/num2가 된다
  return a.denominator

def get_numerator(number1, number2):
  # 분자 반환
  a = Fraction(number1, number2)
  return a.numerator

num1 = 1.25
num2 = 1
num3 = -1
num4 = 5/4
num6 = 6

print(rounding_floats(num1, num2))
print(rounding_floats(num1*10, num3))
print(float_to_fractions(num4))
print(get_denominator(num2, num6))
print(get_numerator(num2, num6))
  
