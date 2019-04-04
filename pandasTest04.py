import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc


#연습) scores.csv 파일을 읽어들여
#       학생의 이름을 index(키) 로설정하고
#           이름 칼럼은 삭제합니다.


df = pd.read_csv("Data/scores.csv")
df.index = df['name']
del df['name']


#연습) 모든 학생의 국어점수를 출력해 봅니다.
print(df['kor'])


#연습) 모든과목의 점수를 출력합니다.
subject = ['kor', 'eng', 'mat', 'bio']
print(df[subject])


rc("font",family=font_manager.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name())
#연습) ben학생의 과목별 점수를 막대그래프로 나타내 봅니다.
# plt.bar(range(len(subject)), df.loc['ben'][subject] )
# plt.title("ben의 과목별 점수")
# plt.xticks(range(len(subject)),subject)
# plt.show()

#연습) 모든학생의 국어점수를 막대그래프로 나타내 봅니다.
# plt.bar(range(len(df.index)) , df['kor'] )
# plt.xticks(range(len(df.index)), df.index, rotation=45)
# plt.title("학생별 국어점수")
# plt.show()
#연습)두개의 차트를 파티션을 나누어 하나의 화면에 표시하세요
plt.subplot(211)
# plt.subplot(2,1,1)
plt.bar(range(len(subject)), df.loc['ben'][subject] )
plt.title("ben의 과목별 점수")
plt.xticks(range(len(subject)),subject)

plt.subplot(212)
plt.bar(range(len(df.index)) , df['kor'] )
plt.xticks(range(len(df.index)), df.index, rotation=45)
plt.title("학생별 국어점수")
plt.savefig('student.png')
print('차트를 만들었어요')
# plt.show()

#학생의 이름을 입력받아
#그학생의 과목별 성적을 차트로 표현하는
#웹서비스를 구현해 봅니다.docker







