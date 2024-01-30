#재귀함수를 이용하여 진법 변환
def convert_dec_to_any_base_rec(number, base):
  convertString = "0123456789ABCDEF"
  if number < base:
    return convertString[number]
  else:
    return convert_dec_to_any_base_rec(number // base, base) \ + convertString[number % base]


num = 9
base = 2
print(convert_dec_to_any_base_rec(num, base))