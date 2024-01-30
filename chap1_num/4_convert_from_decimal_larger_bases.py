#10보다 큰 진수도 변환할 수 있게 확장
def convert_from_decimal_larger_bases(number, base):
  strings = "0123456789ABCDEFGHIJ"
  result = ""
  while number > 0:
    digit = number % base
    result = strings[digit] + result
    number = number // base
  return result
num, base = 257, 16
print(convert_from_decimal_larger_bases(num, base))