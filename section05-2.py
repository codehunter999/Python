# Section05-2
# 파이썬 흐름제어(반복문)
# 반복문 실습

# 코딩의 핵심 -> 조건 해결 중요

# 기본반복문 : for, while

v1 = 1
while v1 < 11:
    print("v1 is : ", v1)
    v1 += 1

print()

for v2 in range(10):
    print("v2 is : ", v2)

print()

for v3 in range(1, 100):
    print("v3 is : ", v3)

print()


# 1 ~ 100 합
sum1 = 0
cnt1 = 0

while cnt1 <= 100:
    sum1 += cnt1
    cnt1 += 1

print('1 ~ 100 : ', sum1)
print('1 ~ 100 : ', sum(range(1,101)))
print('1 ~ 100 : ', sum(range(1,101,2))) # 3번쨰 값을 증감 단위


# 시퀀스(순서가 있는) 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

names = ['kim', 'park', 'cho', 'choi', 'yoo']
for v in names:
    print('You are : ', v)

print()

word = 'dreams'
for s in word:
    print("Word : ", s)

print()

my_info = {
    "name": "kim",
    "age": 33,
    "city": "Seoul"
}

# 기본값은 키
for key in my_info:
    print("my_info", key)

print()

# 값
for key in my_info.values():
    print("my_info", key)

print()

# 키
for key in my_info.keys():
    print("my_info", key)

print()

# 키 and 값
for k, v in my_info.items():
    print("my_info", k, v)

print()

name = "KennRY"

for n in name:
    if n.isupper():
        print(n.lower())
    else:
        print(n.upper())



# break
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 37, 15, 34, 36, 38]

for num in numbers:
    if num == 33:
        print("found: 33!")
        break
    else:
        print("not found!!")

#for - else 구문(반복문이 정상적으로 수행 된 경우 else 블럭 수행)
for num in numbers:
    if num == 33:
        print("found: 33!")
        break
    else:
        print("not found!!")
else:
    print("Not found 33.....")



# continue
lt = ["1", 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is float:
        continue
    print("타입 : ", type(v))


print()

name = "Niceman"
print(reversed(name))
print(list(reversed(name)))
print(tuple(reversed(name)))