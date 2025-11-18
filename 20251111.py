'''
# 함수

# 실습1. 사칙연산 계산기 함수 만들기
# 문제1. 사칙연산 계산기 함수 만들기
def calculate(a, b, operator):
    if operator == "/":
        c = float(a / b)
        print(c)
    elif operator == "+":           # elif operator == "+":
        c = a + b                   # return a + b
        print(c)
    elif operator == "-":
        c = a - b
        print(c)
    elif operator == "*":
        c = a * b
        print(c)
    else:
        print("지원하지 않는 연산입니다.")
    
calculate(3, 4, "*")

# 실습2.가변인자 연습하기
# 문제1. 숫자 여러 개의 평균 구하기
def average(*args):
    return sum(args) / len(args)

print(average(2, 5, 5, 5))

################################
def average(*args):
    result = 0
    for arg in args
        result += arg
    return result    

# 문제2. 가장 긴 문자열 찾기
def longgest(*args):
    if len(args) == 0:
        return print("No arguments provided")
    maxString = ""
    for arg in args:
        if len(arg) > len(maxString):
            maxString = arg
    
    return maxString

####################
def longgest(*args):
    if len(args) == 0:
        return print("No arguments provided")
    return max(args, key=len)
    
# 문제3. (**kwargs 사용 연습)사용자 정보 출력 함수
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="ian", age=15, city="서울", job ="develooper")
print_info(name="ian2", age=20, city="서울", job ="develooper")
print_info(name="ian3", age=34, city="서울", job ="develooper")
print_info(name="ian4", age=14, city="서울", job ="develooper")

# 문제4. 할인 계산기
def discount_price(**kwagrs):
    for key, value in kwagrs.items():
        discounted = value * 0.9
        print(f"{key}: 할인가 {discounted} (원가 {value})")

discount_price(apple = 2000, watermelon=2500, cherry=3000)

# 실습3.전역 변수 연습하기
# 로그인/로그아웃 전역 상태 관리

current_user = ""

def login(name):
    global current_user
    
    if len(current_user) == 0:
        current_user = name
        print(f"{current_user}님 로그인 성공")

    else:
        print("이미 로그인되어 있습니다.")

    return current_user

def logout():
    global current_user
    current_user = ""
    print("로그아웃 되었습니다.")
    
login("jun")
login("jun2")
logout()
login("jun2")

# 실습5. 팩토리얼

n = int(input("정수를 입력하세요."))

result = 1
str_result = []

for i in range(n,0,-1):
    result *= i
    
print(result)

#########################

# 실습5. 팩토리얼
facts = 5
i = 1
for j in range(1,facts+1):
    i *= j
    
print(i)

####################

def factorial(n):
    i = 1
    for j in range(1,n+1):
        i *= j
    return i

print(factorial(5))

# 실습5. 팩토리얼(재귀함수)
x = 1

def factorial(n):
    global x
    if n == 1:
        return x
    else:
        return n * factorial(n-1)
    
print(factorial(5))


# 실습5. 팩토리얼(재귀함수)

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))

# Homework 1

def check_parentheses(s):
    if len(s) % 2 == 1:
        print("False")
    else:
        if s == ("(" * int(len(s)/2)) + (")" * int(len(s)/2)):
            print("True")
        else:
            print("False")


check_parentheses("()(()()))")
check_parentheses("((()))")
check_parentheses("())()")


'''
