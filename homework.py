class Asset:

    asset_list = []

    def __init__(self, name, cost):
        self.name = name
        self.__cost = cost

        Asset.asset_list.append(name)
        Asset.asset_list.append(cost)

        i = 0
        i += 1
        
        asset(i) = Asset.asset_list        
        print(asset(i))
        
        

        return asset(i)

    @property
    def cost(self):
        return self.__cost
    
    @cost.setter
    def cost(self,value):
        if value < 10000:
            raise ValueError("최소비용(10,000원) 미만입니다.")
        else:
            self.__cost = value

class Equipment(Asset):
    def __init__(self, name, cost, year_eq):
        super().__init__(name, cost)
        self.year_eq = year_eq
      
    def price(self):
        year_price = self.cost * (1 - self.year_eq)

        Asset.asset_list.append(year_price)

        return Asset.asset_list        
    
class Car(Asset):
    def __init__(self, name, cost, year_car):
        super().__init__(name, cost)
        self.year_car = year_car

    def price(self):
        
        year_price = self.cost - self.year_car

        Asset.asset_list.append(year_price)
        
        return Asset.asset_list 
          
 

server = Equipment("고성능 서버", 5000000, 0.15)
company_car = Car("업무용 세단", 300000000, 3000000)

server.price()
company_car.price()

asset_list = Asset.asset_list

for asset in asset_list:
    print(asset)
    # print(f"{asset[0]}의 연간 가치: ")

'''

# 실행 예시 
server = ???("고성능 서버", 5000000, 0.15)
company_car = ???("업무용 세단", 30000000, 3000000)


server.cost = 4500000
company_car.cost = 5000   # 10,000원 미만 → 거부 메시지 출력

asset_list = [server, company_car]

for asset in asset_list:
    print(asset)
    print(f"{asset._name}의 연간 가치: {asset.calculate_annual_value():,.0f}원")

'''