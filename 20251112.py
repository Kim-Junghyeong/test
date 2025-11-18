'''

# 실습1
# 1
class Book:
    def __init__(self, title, author, total_pages, current_page):
        self.title = title
        self.author = author
        self.total_pages = total_pages
        self.current_page = current_page
    
    def read_page(self):
        if self.current_page > self.total_pages:
            print("총 페이지보다 적게 입력해주세요!")
        else:
            print(f"{self.current_page} 읽음")
    
    def progress(self):
        print(float(self.current_page/self.total_pages*100),"%")

book1 = Book("adada","sad",154,14)

book1.read_page()
book1.progress()

###### 모범답안 #####################

class Book:
    def __init__(self, title, author, total_pages, current_page):
        self.title = title
        self.author = author
        self.total_pages = total_pages
        self.current_page = current_page

    def read_page(self, pages):
        self.current_page += pages
        if self.current_page > self.total_pages:
            self.current_page = self.total_pages
            print("책을 끝까지 다 읽었어요.")

    def progress(self):
        percent = (self.current_page / self.total_pages) * 100
        print(f"현재 읽은 분량: {percent:.1f}%")
    
nexus = Book("넥서스","조정래",500, 0)

print(nexus.current_page)   # 함수 실행 전
print(nexus.read_page(100)) # return 값이 없으므로 None
print(nexus.current_page)   # 함수 실행 후
nexus.read_page(10)
print(nexus.current_page)

nexus.progress()


# 실습2
# 1

class User:

    total_users = 0         # Class 변수 선언

    def __init__(self, username, points):
        self.username = username
        self.points = points
        User.total_users += 1       # CLass 변수 증가

    def add_points(self, amount):
        self.points += amount

    def get_level(self):
        if self.points >= 0 and self.points < 100:
            print("Level: Bronze")      # reurn "Bronze"
        elif self.points >= 100 and self.points < 500:
            print("Level: Silver")      
        elif self.points >= 500:
            print("Level: Gold")
    
    @classmethod
    def get_total_users(cls):
        print(f"총 유저 수: {cls.total_users}")
    
user1 = User("kkk", 0)
user2 = User("jjj",0)

user1.add_points(500)
user2.add_points(56)

user1.get_level()
user2.get_level()

User.get_total_users()


# 게터 세터 예제
class User:

    def __init__(self, username, points):
        self.__username = username
        self.points = points
        
    def add_points(self, amount):
        self.points += amount
    
    def set_username(self,username):
        self.__username = username
    
    def get_username(self):
        return self.__username


user1 = User("kkk", 0)
user2 = User("jjj",0)

user1.set_username("k22")
print(user1.get_username())

# 실습 3
# 1
class UserAccount:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def change_password(self, old_pw, new_pw):
        if old_pw == self.__password:
            self.__password = new_pw
            print("비밀번호 변경 완료")
            return self.__password
                
        else:
            print("비밀번호 불일치")
    
    def check_password(self, password):
        if self.__password == password:
            print("True")
        else:
            print("False")
    
user1 = UserAccount("kkk",1234)

user1.change_password(1234,12345)
user1.check_password(12345)

# 2

class Student:
    def __init__(self, score):
        self.__score = score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if 0 <= value <= 100:
            self.__score = value
        else:
            raise ValueError("범위를 벗어난 길입니다.")
    
s1 = Student(85)
print(s1.score)

s1.score = 95
print(s1.score)

# 실습4
# 1

class Shape:
    def __init__(self, sides, base):
        self.sides = sides
        self.base = base
    
    def printinfo(self):
        print("변의 개수: ",self.sides)
        print("밑변의 길이: ",self.base)
    
    def area(self):
        print("넓이 계산이 정의되지 않았습니다.")

class Rectangle(Shape):
    def __init__(self, sides, base, height):
        super().__init__(sides, base)
        self.height = height

    def area(self):
        print(self.base * self.height)
    
class Triangle(Shape):
    def __init__(self, sides, base, height):
        super().__init__(sides, base)
        self.height = height
    
    def area(self):
        print(self.base * self.height / 2)

r = Rectangle(4,10,6)
t = Triangle(4,10,6)

r.printinfo()
t.printinfo()

r.area()
t.area()




'''
