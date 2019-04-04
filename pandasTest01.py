# numpy         배열의 조작을 편리하게 해줘요
# pandas        데이터프레임의 조작을 편리하게 해줘요

#또, 머신러닝을 위한 많은 라이브러리들이
#상대하는 데이터형태가 numpy 이거나 pandas를 취급해요

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Pandas의 자료구조
#Series                 ==> 1차원배열
#DataFrame              ==> 2차원배열

#파이썬 기본배열을 Pandas의 1차원 배열로 만들어 봅시다.
# a = [1,2,3,4,5]
# arr = pd.Series(a)
# print(arr)
# print(a)
# print(type(a))
# print(type(arr))


#Pandas의 1차원 배열인 Series를 파이썬 배열을 변경
# arr = pd.Series(['홍길동','강감찬','이순신','유관순'])
# # print(arr)
# name = list(arr)
# print(type(name))
# print(type(arr))


# 설명서에는 Series는 Pandas에서 1차원 배열을 취급한다라고 되어 있었는데
# Series를 만들때 2차원배열을 매개변수로 주면 어떤일이 일어나는지 알아봅시다.

# arr = pd.Series([[1,2,3],[4,5,6]])
# print(arr)
# print(arr[0])
# print(type(arr[0]))
# print(arr[0][1])

#
# arr = pd.Series([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
# print(arr)



# arr = pd.Series([['홍길동','강감찬','이순신'],['서울','울산','광주']])
# arr = pd.Series([['홍길동','강감찬','이순신'],['홍길동','강감찬','이순신']])
# print(arr)
#

# Series는 마치 자바의 map과 같이 key value가 한쌍으로 이루어지는 자료구를
#표현하기에 적합합니다.
#key를 부여하지 않으면 차례대로 index가 부여됩니다.
#필요하다면 key를 부여할 수 있어요

# a = pd.Series([5,9,3,7,6])
# print(a)
# 0    5
# 1    9
# 2    3
# 3    7
# 4    6
# dtype: int64

# print(a.values)
# print(type(a.values))
#
# [5 9 3 7 6]
# <class 'numpy.ndarray'>

# print(a.index)

#각각의 값을 어떤값을 의미하는지 키를 부여할 수 있어요
#생략하면 차례대로 index가 부여되어요
#키값을 부여하면 키값으로 데이터에 접근할 수 있어요===> 직관적
#키값을 부여했다 하더라도 index로도 접근할 수 있어요.
# a = pd.Series([5,9,3,7,6], index=['김경민','오상훈','이성기','김도희','박민서'])
#
# keys = a.index              #Series의 키값으로 모두 뽑아와요
# for key in keys:            #key의 개수만큼 반복수행하여 각요소의 key의 value를 출력
#     print(key, a[key])

# print(a)

# print(a['김도희'])
# print(a[3])

# print(a[0])
# print(a[-1])
# print(a.index)


# Pandas의 Series는 파이썬 배열을 갖고 key값을 부여해
# 보다 직관적으로 접근할 수 있어요
# 그렇다면 파이썬 딕셔너리를 갖고도 Series를 만들수 있는지 실험

# a = {'김경민':5, '오상훈':9,'이성기':3, '김도희':10, '박민서':12}
# # print(a)
# # print(type(a))
# s = pd.Series(a)
# print(s)

















