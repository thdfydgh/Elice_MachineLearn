import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from PIL import Image



# #한글을 지원하는 나눔바른고딕 폰트로 바꾼 코드
# fname='./NanumBarunGothic.ttf'
# font = fm.FontProperties(fname = fname).get_name()
# plt.rcParams["font.family"] = font
# Data set
#---------------------------------------------------------------------------------------------------------------------------#
x = np.array(["Soccer", "Baseball", "Basketball", "Badmintan", "Tabletenis"])
y = np.array([13, 10, 17, 8, 7])
z = np.random.randn(1000)

fig, axes = plt.subplots(1, 2, figsize=(8, 4))

# Bar 그래프
axes[0].bar(x, y)
# 히스토그램
axes[1].hist(z, bins = 200)
fig.savefig("SportHist.png")
#---------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------#
df = pd.read_csv("data_pokemon.csv")

# 공격 타입 Type 1, Type 2 중에 Fire 속성이 존재하는 데이터들만 추출
fire = df[(df['Type 1'] == "Fire") | (df['Type 2'] == "Fire")]     
# 공격 타입 Type 1, Type 2 중에 Water 속성이 존재하는 데이터들만 추출
water = df[(df['Type 1'] == "Water") | (df['Type 2'] == "Water")]

fig, ax = plt.subplots()

ax.scatter(fire['Attack'], fire['Defense'],
    marker='*', color='red', label="Fire", s=50)
ax.scatter(water['Attack'], water['Defense'],
    marker='.', color='blue', label="Water", s=25)

ax.set_xlabel("Attack")
ax.set_ylabel("Defense")
ax.legend(loc="upper right")

fig.savefig("pokemon.png")

#---------------------------------------------------------------------------------------------------------------------------#
