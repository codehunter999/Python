# Section09
# 파일 읽기, 쓰기
# 읽기모드 : r, 쓰기모드(기존 파일 삭제) : w, 추가모드(파일 생성 또는 추가) : a
# ..: 상대경로, . : 절대경로
# 기타 : https://docs.python.org/3.7/library/functions.html#open

# 파일 릭기
# 예제1
f = open('./resource/review.txt', 'r')
content = f.read()
print(content)
print(dir(f))
#반드시 close 리소스 반환
f.close()

print('------------------------------------------------')
print('------------------------------------------------')

# 예제2
with open('./resource/review.txt', 'r') as f:
    c = f.read()
    print(c)
    print(list(c))
    print(iter(c))

print('------------------------------------------------')
print('------------------------------------------------')

# 예제3
with open('./resource/review.txt', 'r') as f:
    for c in f:
        print(c.strip())

print('------------------------------------------------')
print('------------------------------------------------')

# 예제4
with open('./resource/review.txt', 'r') as f:
    content =  f.read()
    print(">", content)
    content =  f.read() # 내용 없음, 이미 한번 읽어와서 끝 부분에 커서가 존재하고 있기 때문에 다시 읽으면 내용이 안나옴
    print(">", content) 

print('------------------------------------------------')
print('------------------------------------------------')

# 예제5

with open('./resource/review.txt', 'r') as f:
    line = f.readline() # 한줄씩 읽는다.
    # print(line)
    while line:
        print(line, end=' ')
        line = f.readline()

print('------------------------------------------------')
print('------------------------------------------------')

# 예제6
with open('./resource/review.txt', 'r') as f:
    contents = f.readlines()
    print(contents)
    for c in contents:
        print(c, end='******')

print('------------------------------------------------')
print('------------------------------------------------')
print()

# 예제7
score = []
with open('./resource/score.txt', 'r') as f:    
    for line in f:
        score.append(int(line))
    print(score)

print('Average : {:6.3}'.format(sum(score)/len(score)))

print('------------------------------------------------')
print('------------------------------------------------')

# 파일 쓰기

# 예제1
with open('./resource/text1.txt', 'w') as f:
    f.write('Niceman!\n')

# 예제2
with open('./resource/text1.txt', 'w') as f:
    f.write('Goodman!\n')

# 예제3
from random import randint

with open('./resource/text2.txt', 'w') as f:
    for cnt in range(6):
        f.write(str(randint(0,50)))
        f.write('\n')
    

# 예제 4
#  writelines: 리스트 -> 파일로 저장
with open('./resource/text3.txt', 'w') as f:
    list = ['kim\n', 'park\n', 'cho\n']
    f.writelines(list)

# 예제 5
with open('./resource/text4.txt', 'w') as f:
    print('Test contest1', file=f)
    print('Test contest2', file=f)
