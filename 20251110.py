'''

# 반복문 
# 실습 1
#  1
#########답안####
numbers = [3, 6, 1, 8, 4]
doubled = []

for number in numbers:
    doubled.append(number*2)

print(doubled)

# 2

words = ["apple", "banana", "kiwi", "grape"]
new_list = []

for i in words:
    lens = len(i)
    new_list = new_list + [lens]

print(new_list)


##### 답안 ####
words = ["apple", "banana", "kiwi", "grape"]
lengths = []

for word in words:
    lengths.append(len(word))

print(lengths)

# 3

coordinates = [(1,2),(3,4),(5,6),(7,8)]

x_values = []
y_values = []

for x, y in coordinates:
    x_values.append(x)
    y_values.append(y)

print("x_values: ", x_values)
print("y_values: ", y_values)

# 실습 2

# 1

total = 0

for i in range(1, 10):
    total += i
print(total)    

###########################

num = int(input("숫자를 입력하세요: "))
sum = 0

for i in range(num + 1):
    sum += i

print(num, "까지의 합은", sum, "입니다.")

# 2

number = int(input("출력하고 싶은 단을 입력하세요. "))

for i in range (1,10):
    print(f"{number} X {i} = ",number*i)


######################
dan = int(input("생성할 단을 입력해주세요:"))

for i in range(1,10):
    print(f"{dan} X {i} = {dan * i}")
   
# 3

total = 0
i3 = 0 

for i in range(1,101):
    i2 = i * 3
   
    if i2 <= 100:
        i3 += i2
print(i3)       

###########################

num = int(input("숫자를 입력하세요."))
sum = 0

for i in range(num +1):
    if i % 3 == 0:
        sum += i

# 4

n = int(input("숫자를 입력해주세요. "))

for i in range(0,n):

#####################

n = int(input("숫자를 입력해주세요. "))

for i in range(1,n+1):
    if i % 2 ==0:        # if i % 2 ==0 and if i % 5 ==0:
        if i % 5 ==0:
            print(i)


# 실습3

# 1

for i in range(2,10):
    print(f"[ {i}단 ]")
    for j in range(1,10):
        print(f"{i} X {j} = {i*j}")
    print()



# 2
# 왼쪽 정렬

n = int(input("정수를 입력하세요. "))

for i in range(1,n+1):
    print("*"*i)

# 오른쪽 정렬
for i in range(1,n+1):
    for j in range(n+1,1,-1):
        print("*"*j)




############

n = int(input("정수를 입력하세요. "))

# 왼쪽 정렬

for i in range(1,n+1):
    for j in range(i):
        print("*", end="")
    print()


# 오른쪽 정렬

for i in range(1,n+1):
    for j in range(n-i):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()


# 실습4

# 1 반복문

num = []
for i in range(1,11):
    num.append(i**2)
print(num)

# 2
num = []

for i in range(1,51):
    if i % 3 == 0:
        num.append(i)
print(num)

# 3

fruits = ['apple', 'fig', 'banana', 'plum', 'cherry', 'pear', 'orange']
result = []
for i in fruits:
    if len(i) >= 5:
        result.append(i)
print(result)

# 1 컴프리헨션

num = [x**2 for x in range(1, 11)]
print(num)

# 2
num = [x for x in range(1, 51) if x % 3 ==0]
print(num)

# 3
fruits = ['apple', 'fig', 'banana', 'plum', 'cherry', 'pear', 'orange']
result = [x for x in fruits if len(x) >= 5]
print(result)


# While문 실습 1

# 1
secret_code = "enter"
i = ""

while i != secret_code:
    i = input("비밀 코드를 입력하세요: ")
    if i != secret_code:
        print("비밀코드가 틀렸습니다. 다시 시도하세요.")

print("입장 완료! 환영합니다.")

# 2

import random           # 랜덤 값 가져오기

temp = random.randint(1,10) # (시작값,마지막 값)
trial = 0

while True:
    num = int(input("1~100 사이 숫자를 입력하세요."))
    trial += 1
    if num > temp:
        print(f"{num}보다는 작아요.")
    elif num < temp:
        print(f"{num}보다는 커요.")
    else:
        print(f"{trial}번 만에 정답을 맞췄습니다.")
        break


# 구구단 while문

i = 2
j = 1

while True:
    print(f"[ {i}단 ]")
    while True:
        print(f"{i} X {j} = {i*j}")
        if j == 9:
            break
        j = j + 1
    print()
    j = 1
    if i == 9:
        break
    i = i+1

# While문 실습2
# 1

secret_code = "enter"
i = ""

while True:
    i = input("비밀 코드를 입력하세요: ")
    if i != secret_code:
        print("비밀코드가 틀렸습니다. 다시 시도하세요.")
    else:
        print("입장 완료! 환영합니다.")
        break    

# 2

sum_age = 0
times = 0

while True:
    ege = int(input("나이를 입력하세요: "))

    if ege > 0 and ege <= 120:
        sum_age += ege
        times += 1
        if times == 5:
            print(f"총 나이 합계는 {sum_age}, 평균은 {sum_age/5}입니다.")
            break

ID = "바보"
password = "바보"

while True:
    input_ID = input("ID를 입력하세요: ")

    if  ID == input_ID:
        input_Ps = input("비밀번호를 입력하세요: ")

        if password == input_Ps:
            print("로그인 성공!")
            break
        else:
            print("비밀번호가 틀렸습니다.")
    else:
        print("ID가 존재하지 않습니다.")            

'''