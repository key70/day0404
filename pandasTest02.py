import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# df = pd.DataFrame([[1,2,3],[4,5,6]])
# print(df)
# print(type(df))


df  = pd.read_csv("Data/scores.csv")
# print(df)
# print(type(df))
# print(df.index)       #키(인덱스)를 확인
# print(df.columns)       #컬럼명들을 확인
# print(df.values)
# print(type(df.values))
# print(df['kor'])          #국어점수만 출력
# print(df[2])            #불가능          2번째행만 출력X   2번째열만 출력X


# Pandas의 DataFrame에서 행접근   loc이나 iloc함수를 이용하여 행에 접근합니다.
# 키값을 부여하지 않으면 행에 접근하려면 index접근합니다.
# 이때는 loc이나 iloc 차이가 없어요
# 그러나 키값을 부여했을때는
# 인덱스로 접근할때는 iloc을 쓰고 키로 접근할 때는 loc을 사용해요.
# loc
# iloc

# print(df)
print(df.loc[2].values)
print(df.iloc[2].values)