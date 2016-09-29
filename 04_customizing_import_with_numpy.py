# _*_ coding: utf-8 _*_
import numpy as np

# 파일 이름을 설정한다. 
file = 'digits_header.txt'

# Load the data: data
# 딜리미터는 탭으로한다. 
# skiprows 를 통해서 필요없는 라인을 스킵한다. 
# 로드할 칼럼을 지정한다. 0 : 첫번째 칼럼, 2 : 세번째 칼럼 
data = np.loadtxt(file, delimiter='\t', skiprows=1, usecols=[0,2])

# 데이터 출력하기. 
print(data)
