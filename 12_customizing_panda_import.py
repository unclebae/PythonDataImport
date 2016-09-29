# _*_ coding: utf-8 _*_
import pandas as pd
import matplotlib.pyplot as plt

file = 'titanic_corrupt.txt'

# 데이터를 임포트한다. 
# 구분자 sep='\t'로 
# 각 필드에 커맨트가 있다면 커맨트 필드를 확인하기 위해서 comment='#' 으로
# na_values=['Nothing'] 을 수행해서 리스트의 문자가 NA/NaN으로 인식된경우 처리. 
data = pd.read_csv(file, sep='\t', comment='#', na_values=['Nothing'])

# 데이터 프레임의 헤더를 출력한다. 
print(data.head())

pd.DataFrame.hist(data[['Age']])
plt.xlabel('Age (years)')
plt.ylabel('count')
plt.show()
