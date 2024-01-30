def convert_to_decimal(number, base):
  # 'base' 진수 -> 10진수 변환
  multiplier, result = 1, 0
  while number > 0:
    result += number % 10 * multiplier # 나머지 * 10의 거듭제곱
    multiplier *= base # 다음 자릿수를 처리할 준비
    number = number // 10 #다음 자릿수로 이동
  return result

number, base = 1001001101, 2
print(convert_to_decimal(number, base))
