# 실습5. 추상 클래스 연습문제

from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass
        

class CardPayment(Payment):
    def pay(self,amount):
        print(f"카드로 {amount}원을 결제합니다.")

class CashPayment(Payment):
    def pay(self,amount):
        print(f"현금으로 {amount}원을 결제합니다.")


card = CardPayment()
cash = CashPayment()

card.pay(2000)
cash.pay(30000)

# 상속된 Class에서 함수 이름을 pay 대신 pay1이나 다른 것을 사용하면 오류!

# 실습2. math 모듈 사용해보기

# 문제1.실제거리 계산

import math

x1, y1 = 4, 5
x2, y2 = 2, 3

print(math.sqrt(math.pow(x2-x1,2) + math.pow(y2-y1,2)))
