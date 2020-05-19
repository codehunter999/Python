# Section02-1
# 파이썬 기초 코딩
# Print 구문의 이해
# 참조 : http://www.python-course.eu/python3_formatted_output.php

# 기본출력
print('Hello Python!')
print("Hello Python!")
print("""Hello Python!""")
print('''Hello Python!''')

print()

# Separator 옵션 사용
print('T', 'E', 'S', 'T', sep='')
print('2019', '02', '19', sep='-')
print('niceman', 'google.com', sep='@')

# end 옵션 사용
print('Welcome To', end=' ')
print('the black parade', end=' ')
print('piano notes')

print()

# format 사용 [], {}, ()
print('{} and {}'.format('You','Me'))
print("{0} and {1} and {0}".format('You','Me'))
print("{a} arn {b}".format(a='You', b='Me'))

# %s: 문자, %d: 정수, %f: 실수
print("%s's favorate number is %d" % ('KDC', 7)) 

print("Test1: %5d, price: %4.2f" %(776, 6534.123))
print("Test1: {0: 5d}, price:{1: 4.2f}".format(776, 6534.123))
print("Test1: {a: 5d}, price:{b: 4.2f}".format(a=776, b=6534.123))


print("'You'")
print('\'you\'')
print('"You"')
print("""'you'""")
print('\\you\\\n\n\n\n')
print('\t\t\ttest')