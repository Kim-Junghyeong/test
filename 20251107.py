# 튜플 실습

'''
# 튜플 실습

# 1

# step 1
user = ("minji", 25, "Seoul")

l_user = list(user)
l_user[0] = "eunji"
restored_user = tuple(l_user)   # restored_user = ("eunju") + user[1:]
print(restored_user)

# step 2
name, age, city = restored_user
print(name)
print(age)
print(city)
'''

'''
user = ("minji", 25, "Seoul")

restored_user = ("eunji",) + user[1:]
print(restored_user)

name, age, city = restored_user
print(name)
print(age)
print(city)

if city == "Seoul":
    print("서울 지역 보안 정책 적용 대상입니다.")
else:
    print("일반 지역 보안 정책 적용 대상입니다.")

users = ("minji", "eunji", "soojin", "minji", "minji")
print(users.count("minji"))
print(users.index("soojin"))

list_user = list(users)
print(sorted(list_user))

'''
# SET

'''
# 1

submissions = ["kim", "lee", "kim", "park", "choi", "lee", "lee"]

s = set(submissions)
c = len(s)

print("제출한 학생 수 : ",c)
print("제출자 명단: ",s)

'''

# 딕셔너리
'''


# 1

user = {}

user["username"] = "skywalker"
user["email"] = "sky@example.com"
user["level"] = 5
print(user)

user = dict(username="skywalker",email="sky@example.com",level=5)
print(user)

email_value = user.get("email")     # email_value = user["email"]
print(email_value)

user.update(level=6)    # user["level"] = 6
print(user)

print(user.get("phone", "해당정보 없음"))

user.update(nickname="sky")
del user["email"]

user.setdefault("signup_date", "2025-07-07")    # user["signup_date"] = "2025-07-10"
# setdefault 는 value에 None을 추가할 수 있다. user.setdefault("test")
print(user)


'''

# 조건문
'''
# 1

weather = input("비 또는 맑음을 입력해주세요: ")

if weather == "비":
    print("우산을 챙기세요.")

if weather == "맑음":
    print("선크림을 바르세요.")

    
############################
weather = input("'비' or '맑음'을 입력하세요: ")

if weather == "비":
    print("우산을 챙기세요!")
elif weather == "맑음":
    print("선크림을 바르세요!")
else:
    print("'비' or '맑음'을 입력해주세요!")    

'''
# 2
'''
a = int(input("정수를 입력해 주세요. "))
if a % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")
'''

# 3
'''
a = int(input("나이를 입력하세요. "))

if a <= 12:
    print("전체 관람가")
elif a <= 15:
    print("12세 이상 관람가")
elif a <= 18:
    print("15세 이상 관람가")
else:
    print("청소년 관람불가")

'''

# 4
'''
time = int(input("정수를 입력해주세요. "))

hour = time // 3600
minute = time % 3600 // 60
second = time % 60

if time >= 3600:
    print(f"{hour}시간 {minute}분 {second}초")
elif time >= 60:
    print(f"{minute}분 {second}초")
else:
    print(f"{second}초")
'''

# 5
'''
price = int(input("가격을 입력해주세요. "))
menu = input("메뉴를 입력해주세요. ")

if menu == "김밥" :
    if price >= 2500:
        print("구매 성공")
    else:
        print("금액이 부족합니다.")

if menu == "삼각김밥" :
    if price >= 1500:
        print("구매 성공")
    else:
        print("금액이 부족합니다.")

if menu == "도시락" :
    if price >= 4000:
        print("구매 성공")
    else:
        print("금액이 부족합니다.")

'''


# 튜플
'''
user = ("minji", 25, "Seoul")

restored_user = ("eunji",) + user[1:]
print(restored_user)

name, age, city = restored_user
print(name)
print(age)
print(city)

if city == "Seoul":
    print("서울 지역 보안 정책 적용 대상입니다.")
else:
    print("일반 지역 보안 정책 적용 대상입니다.")

users = ("minji", "eunji", "soojin", "minji", "minji")
print(users.count("minji"))
print(users.index("soojin"))

list_user = list(users)
print(sorted(list_user))

'''