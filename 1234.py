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
print(labels)
