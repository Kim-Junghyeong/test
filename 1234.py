# 20251117_HomeWork_4

import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

data = {'분기': ['1분기', '2분기', '3분기', '4분기'],
        '서울 매출 (억원)': [300, 350, 420, 380],
        '부산 매출 (억원)': [250, 300, 380, 400]
        }
print("hello")

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