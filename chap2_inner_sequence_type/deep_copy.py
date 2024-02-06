#리스트의 깊은 복사
mylist = [1, 2, 3, 4]  # 리스트 생성
newlist = mylist[:]
newlist2 = list(mylist)

print(id(mylist[0]))
print(id(newlist[0]))
print(id(newlist2[0]))

#딕셔너리의 깊은 복사
myDict = {"안녕": "세상"}
newDict = myDict.copy

print(id(myDict))
print(id(newDict))
