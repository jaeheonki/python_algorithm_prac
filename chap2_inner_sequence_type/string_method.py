#문자열 메소드 실습

# join method -> A.join(B) : 리스트 B에 있는 모든 문자열을 하나의 단일 문자열 A로 결합(+를 쓸 수도 있지만 리스트에 많은 문자열이 있을 때 사용)
slayer = ["버피", "앤", "아스틴"]
print(slayer)
a = "-<>-".join(slayer)
print(a)

#ljust(), rjust()
#ljust : 문자열 맨 처음부터, rjust : 문자열 맨 끝부터
#사용법 : l/rjust(width, fillchar))

name = "스칼렛"
b = name.ljust(50, '-')
c = name.rjust(50, '-')
print(b)
print(c)

#format()
#A.format() : 문자열 A에 변수를 추가
print("{0} {1}".format("안녕", "파이썬!"))
print("이름 : {who}, 나이 : {age}".format(who="김재헌", age=24))
print("이름 : {who}, 나이 : {0}".format(12, who="김재헌"))
#필드 이름/인덱스 생략도 가능
print("{} {} {}".format(10, "김재헌", True))

#splitlines()
#A.splitlines() : 문자열 A를 줄(\n) 단위로 나누어 리스트로 반환
slayers = "로미오\n줄리엣"
list_slayers = slayers.splitlines()
print(slayers, list_slayers)

#split method
#A.split(t, n) : 문자열 A에서 문자열 t를 기준으로 정수 n번만큼 분리한 문자열 리스트를 반환
# n 미지정시 : 대상 문자열을 t로 최대한 분리
# t도 미지정시 : 공백 문자로 구분한 문자열 리스트를 반환

string_list = "healthy*presentation*beautiful*sorry"
print(string_list.split("*", 1))
print(string_list.split("*"))

#strip()
