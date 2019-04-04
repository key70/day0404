# 숙제)
# 2016_GDP.txt 파일을 읽어 들여 상위 10개의 나라를 막대그래프로 그려주세요


import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager, rc, colors
import csv

f = open("Data/2016_GDP.txt","r",encoding="UTF-8")
f.readline()

names, money = [],[]
list = csv.reader(f, delimiter=":")
for row in list:
    names.append(row[1])
    money.append(int(row[2].replace(",","")))

f.close()

# money = np.array(money, dtype="int32")


#한글글꼴 설정
rc('font',family=font_manager.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name())

# plt.bar(range(10), money[:10])
# plt.bar(range(10), money[:10], color="b")
plt.bar(range(10), money[:10], color=colors.TABLEAU_COLORS)
plt.title("GDP 상위 10개의 나라")
plt.xticks(range(10), names[:10],rotation="90")
plt.show()











