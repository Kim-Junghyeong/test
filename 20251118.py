# Pandas(2) 
# 실습.1


import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

df = pd.DataFrame({
    '이름': ['민준', '서연', '지후', '서준', '지민'],
    '점수': [78,92,85,60,88],
    '반': [1,2,1,2,1]
})

# 5

df1 = df[(df['점수'] < 80) | (df['반'] == 2)]
print(df1)

# 6

df2 = df1[df1['점수'] >= 70]
df2.reset_index(drop=True)
print(df2)

# 실습.4
# 4

import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

df = pd.DataFrame({
    'team': ['A','A','B','B','A','B'],
    'position':['FW','DF','FW','DF','DF','FW'],
    'score': [3,2,None,1,4,2]
})

result = df.groupby(['team','position'])['score'].mean()
print(result)

# Folium 실행(지도시각화)

import folium

m = folium.Map(location=[37.61119807384533, 126.91731049700418],zoom_start=18)
# 기본 마커
folium.Marker(
    [37.61119807384533, 126.91731049700418],
    popup="Subway",
    tooltip="구산역",
    icon=folium.Icon(color="black", icon="fa-solid fa-bus", prefix="fa-solid")
).add_to(m)

# 원형 마커
folium.CircleMarker(
  [37.61020411781574, 126.9133136519163],
  radius=100,
  color="#adcdff",
  fill_color ="#1c73ff",
  popup="CircleMarker",
  tooltip="tooltip"
).add_to(m)

m.add_child(folium.ClickForMarker(popup="내가 클릭한 곳"))

# 클릭한 곳의 위도와 경도 표시
m.add_child(folium.LatLngPopup())

m.save("map.html")

# 확장 : Live Server 설치
# map.html 오른쪽 클릭 후, Open with Live Server 실행


# Github

# 터미널 
# git init                                                                  # git 설정
# git remote add origin https://github.com/Kim-Junghyeong/test.git          # 등록 위치
# git status
# git add .                                                                 # 모든 파일 등록
# git status

# git config --global user.name Kim-Junghyeong
# git config --global user.email cxop2002@naver.com
# git config user.name
# git config user.email

# git commit -m "첫번째 git hub"                                             # 저장 포인트
# git push -f origin master                                                 # 파일 올리기
# 소스제어 사용하여 Git 올리기 가능 

# git clone https://github.com/Kim-Junghyeong/test.git ./                   # 코드 복사 해당 폴더
# git remote -v
# git pull origin master