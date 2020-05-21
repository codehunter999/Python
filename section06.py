# Section06
# 파이썬 함수식 및 람다(lambda)

# 함수 정의 방법
# def 함수명(parameter):
#     code

# 함수 호출 
# 함수명(parameter)

# 함수 선언 위치 중요

# 예제1
def hello(world):
    print("Hello", world)

hello("Python!")
hello(7777)


# 예제2
def hello_return(world):
    val = "Hello " + str(world)
    return val

str = hello_return("Python!!!!!")
print(str)


# 예제3(다중리턴)
def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return y1, y2, y3

val1, val2, val3 = func_mul(100)
print(val1, val2, val3)
print(type(val1), val2, val3)


# 예제3(데이터 타입 반환)
def func_mul2(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]

lt = func_mul2(100)
print(lt, type(lt))

# 예제4
# args, kwargs

# *args
# 가변
# tuple 자료형으로 받는다.
# 매개변수의 수량을 정확하게 파악할수 없을때
# enumerate : index를 붙여준다.
def args_func(*args):  # 매개변수명 자유롭게 변경 가능
    for i, v in enumerate(args):
        print(type(args),'{}'.format(i), v, end=' ')


args_func('Kim')
args_func('Kim', 'Park')
args_func('Kim', 'Park', 'Lee')

print()

# kwargs
# dictionaty 자료형으로 받는다.
# 가변 
def kwargs_func(**kwargs):  # 매개변수명 자유롭게 변경 가능
    for v in kwargs.keys():
        print(type(kwargs),'{}'.format(v), kwargs[v], end=' ')


kwargs_func(name1='Kim')
kwargs_func(name1='Kim', name2='Park')
kwargs_func(name1='Kim', name2='Park', name3='Lee')

print()
print()


# 전체 혼합
def example(arg_1, arg_2, *args, **kwargs):
    print(arg_1, arg_2, args, kwargs)


example(10, 20, 'park', 'kim', 'lee', age1=33, age2=34, age3=44)

# 예제5
# 중첩 함수
def nested_func(num):
    def func_in_func(num):
        print('>>>>', num)

    print("In func")
    func_in_func(num + 100)

nested_func(1)

# python decorator 실습
import datetime

def datetime_decorator(func):
    def decorated():
        print (datetime.datetime.now())
        func()
        print (datetime.datetime.now())        
    return decorated

@datetime_decorator
def main_function():
    print("Main function start")

main_function()


# 예제 6
# Hint
# x는 int형 반환은 list로 된다는 힌트
def func_mul3(x : int) -> list:
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]

print(func_mul3(5))


# 람다식 예제
# 메모리 절약, 가독성 향상, 코드 간결화
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행(Heap 초기화) -> 메모리 초기화

# 일반적 함수 -> 변수 할당
def mul_10(num : int) -> int:
    return num*10

var_func = mul_10
print(var_func)
print(type(var_func))

print(var_func(130))

# 람다식 전환
lambda_mul_10 = lambda num: num*10

print('>>>>',lambda_mul_10(10))

def func_final(x, y, func):
    print(x * y * func(10))

func_final(10, 10, lambda_mul_10)

# 함수를 즉시 만들어서 실행 가능
print(func_final(10,10,lambda x: x*1000))