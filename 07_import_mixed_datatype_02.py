# _*_ coding: utf-8 _*_
import numpy as np

file = 'titanic.csv'

# genfromtxt 와 유사하게 파일을 읽어들인다. 
# 기본적으로 dtype는 None로 설정된다. 
# 기본적인 delimiter는 ','이다. 
# 기본적인 names=True로 설정된다. 
d = np.recfromcsv(file)

#  첫번째 3개의 엔트리를 출력한다. 
print(d[:3])

np.shape(d)
# Servived 필드를 출력한다. 
print(d[1])

# 아래코드와 같이 사용이 안되네...
# print(d['Fare'])
