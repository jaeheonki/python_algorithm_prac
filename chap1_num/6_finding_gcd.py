#최대공약수 (GCD)를 구하는 함수)
def finding_gcd(a, b):
  while (b != 0):
    result = b
    a, b = b, a % b  #튜플 할당 -> a에는 b의 값을, b에는 a를 b로 나눈 나머지를 저장 -> b가 0될 때 까지 반복
  return result


num1 = 21
num2 = 12
print(finding_gcd(num1, num2))
