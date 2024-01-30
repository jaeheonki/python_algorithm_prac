#10진수 -> 'base'진수 변환 2<= base <= 10

def convert_from_decimal(number, base):
  multiplier, result = 1, 0
  while number > 0: 
    result += (number % base) * multiplier
    multiplier *= 10
    number = number // base
  return result

num = 3024
base = 2
print(convert_from_decimal(num, base))