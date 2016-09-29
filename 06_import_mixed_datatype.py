# _*_ coding: utf-8 _*_
import numpy as np
import matplotlib.pyplot as plt

file = 'titanic.csv'

# 파일을 로드한다. 
# genfromtxt는 구조화된 파일을 로드할때 사용한다. 
# 구분자는 ','로 한다. 
# names 항목은 헤더가 존재함을 의미한다. (True인경우)
# dtype 는 로드할 데이터 타입을 의미한다. (구조적 배열이라 한다. structured array)
data = np.genfromtxt(file, delimiter=',', names=True, dtype=None)

print(type(data))

# 로드한 flat데이터를 쉐이프 처리한다. 
np.shape(data);
print(type(data))

# 필드 헤더를 이용하여 칼럼에 접근한다. 
print(data['Fare'])
