import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df  = pd.read_csv("Data/scores.csv")
df.index = df['name']       #학생의 이름을 key로 설정했어요
del df['name']              #데이터프레임에서 name컬럼은 삭제해요
# print(df)



# #연습) henry의 정보를 출력해 봅니다.
# print(df.loc['henry'])
# print(df.loc['henry'].values)
#
# #연습) 'andrew'부터 'paul'까지의 정보를 출력해봅니다.
# print(df.loc['andrew':'paul'])
# print(df.iloc[1:7])
# #  시작:끝
# #           loc은 끝이 포함이 되어요
# #           iloc은 끝이 포함이 되지 않아요
#
# #연습) 'adam', 'dan', 'walter'의 정보를 출력해봅니다.
# ps = ['adam', 'dan', 'walter']
# # print(df.loc[['adam','dan','walter']])
# print(df.loc[ps])
#
# #연습) 앞에서 5번째 학생들의 국어점수를 출력해봅니다.
# # print(df.iloc[:5]['kor'])
# # print(df.iloc[:5,'kor'])
# print(df.loc[:'dan','kor'])
#
# #연습) 앞에서 5번재 학생들의 국어,수학점수를 출력해 봅니다.
# print(df.iloc[:5][['kor','mat']])

#연습) 'adam', 'dan', 'walter'의 'bio'를 제외한 과목의 점수를 출력합니다.
# names = ['adam', 'dan', 'walter']
# subjects = ['kor','eng','mat']
# print(df.loc[names,subjects])
# print(df.loc[names][subjects])


names = [0,4,7]
print(df.iloc[names, 1:-1])





