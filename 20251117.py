# Pandas(1)

# 실습1 Series 연습

# 3. 딕셔너리를 이용해 series를 만들고, 인천 값 출력
import pandas as pd

s = {'서울': 950, '부산':340, '인천':520}
s1 = pd.Series(s)

print(s1.index,s1.values)
print(s1["인천"])

# 5 아래 두 Series의 합을 구하세요.
import pandas as pd
s1 = pd.Series([3,5,7], index=['a','b','c'])
s2 = pd.Series([10,20,30],index=['b','c','d'])

print(s1+s2)


# 실습1 DataFrame 연습(1)

# 1. DataFrame 생성, 컬럼명 '이름','나이','도시' 지정

import pandas as pd

data = {
    '이름': ["홍길동", "김철수", "이영희"],
    '나이': [28, 33, 25],
    '도시': ["서울","부산","대구"]
}

df = pd.DataFrame(data)
print(df)

# 2. 딕셔너리로 생성

import pandas as pd

data = [
    {'A':[1, 2, 3]}, 
    {'B': [4, 5, 6]}
]

df = pd.DataFrame(data)
print(df)

#3. DataFrame 만들기
import pandas as pd

data = [{'과목': '수학','점수': 90},
        {'과목': '영어', '점수': 85},
        {'과목': '과학', '점수': 95}
        ]

df = pd.DataFrame(data)

print(df)

#4. DataFrame 만들기, 인덱스 ['학생1','학생2','학생3'] 지정
import pandas as pd

data = {'이름': ['민수', '영희', '철수'],
        '점수': [80, 92, 77]
        }

df = pd.DataFrame(data,
    index=['학생1','학생2','학생3']
)

print(df)

#5. Series 객제 2개로 DataFrame 만들기
import pandas as pd

kor = pd.Series([90, 85, 80], index=['a','b','c'])
eng = pd.Series([95, 88, 82], index=['a','b','c'])

df = pd.DataFrame({1: kor,2: eng})
print(df)


# 실습4. 통계함수, 결측값 처리 연습(1)

import pandas as pd
import numpy as np

data = {
    "도시": ["서울", "부산", "광주", "대구", np.nan, "춘천"],
    "미세먼지": [45, 51, np.nan, 38, 49, np.nan],
    "초미세먼지": [20, np.nan, 17, 18, 22, 19],
    "강수량": [0.0, 2.5, 1.0, np.nan, 3.1, 0.0]
}
df = pd.DataFrame(data)
print(df)

# 1. '미세먼지' 컬럼의 평균과 중앙값 구하기
print("미세먼지 평균: ", df["미세먼지"].mean())
print("미세먼지 중앙값: ", df["미세먼지"].median())

# 2. '초미세먼지' 컬럼의 최대값과 최솟값 구하기
print("초미세먼지 최댓값: ", df["초미세먼지"].max())
print("초미세먼지 최솟값: ", df["초미세먼지"].min())

# 3. 각 컬러멸 결측값 개수 구하기
print(df.isnull().sum())

# 4. 결측값 1개라도 있으면 삭제 한 뒤, 
# 남은 데이터의 '초미세먼지 평균'
df2 = df.dropna()
print("초미세먼지 평균: ",df2["초미세먼지"].mean())

# 5. 결측값 모두 0으로 채운 뒤, 
# '미세먼지'와 '초미세먼지'의 합계
df3 = df.fillna(0)
print("미세먼지 합계: ", df3["미세먼지"].sum())
print("초미세먼지 합계: ",df3["초미세먼지"].sum())

df4 = df.fillna(df.mean(numeric_only=True))
print("미세먼지 표준편차: ", df4["미세먼지"].std())

# 매트랩

# 실습1. 선 그래프 그리기
import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales_2019 = [100,120,140,110,130,150,160,170,180,200,190,210]
sales_2020 = [90,110,130,120,140,160,170,160,150,180,200,190]

plt.plot(months,sales_2019, label=2019)
plt.plot(months, sales_2020, label=2020)
plt.legend()
plt.title("Monthly Sales Comparison (2019-2020)")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()

# 실습2. 막대 그래프 그리기
import matplotlib.pyplot as plt

categories = ['Categroy 1','Categroy 2','Categroy 3','Categroy 4','Categroy 5']
data = [20, 35, 15, 27, 45]

plt.bar(categories,data)
plt.grid()
plt.title("Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show() 


# 20251117_HomeWork_1

import pandas as pd

data = {'Seoul': 5.3, 'Busan': 8.1, 'Jeju': 9.5, 'Daejeon': 4.8}

temperature = pd.Series(data)

print(temperature)
print('---')
print(temperature.dtype)
print('---')
print(temperature.size)
print('---')
print(temperature * 2)

# 20251117_HomeWork_2

import pandas as pd

data = {'지역': ['Seoul', 'Busan', 'Jeju', 'Daejeon'],
        '강수량': [120.5, 88.0, 150.2, 105.7],
        '미세먼지': [45, 35, 28, 50]
        }

df_weather = pd.DataFrame(data)

print(df_weather)
print("------")
print(df_weather.columns)
print("------")
print(df_weather.info())
print("------")
print(df_weather.head(2))

# 20251117_HomeWork_3

import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

data = {'부서': ['영업', '기획', '개발', '마케팅'],
        '예산(만원)': [1500, 800, 2200, 1000],
        }

df= pd.DataFrame(data)

df1 = df.sort_values(by='예산(만원)',ascending=False)
print(df1)

labels = df1['부서'].tolist()
values = df1['예산(만원)'].tolist()

plt.bar(labels,values)
plt.grid()
plt.title("부서별 예산 테이블")
plt.xlabel("부서")
plt.ylabel("예산(만원)")
plt.show()

# 20251117_HomeWork_4

import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

data = {'분기': ['1분기', '2분기', '3분기', '4분기'],
        '서울 매출 (억원)': [300, 350, 420, 380],
        '부산 매출 (억원)': [250, 300, 380, 400]
        }

df = pd.DataFrame(data)

x_values = df['분기'].tolist()
y_values1 = df['서울 매출 (억원)'].tolist()
y_values2 = df['부산 매출 (억원)'].tolist()

plt.plot(x_values,y_values1, label='서울 매출')
plt.plot(x_values,y_values2, label = '부산매출')
plt.legend()
plt.grid()
plt.title("지역별 분기 매출 테이블")
plt.xlabel("분기")
plt.ylabel("매출 (억원)")
plt.show()
