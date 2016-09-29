# _*_ coding: utf-8 _*_
import pandas as pd

file = 'digit.csv'

# 첫번째 5개의 row를 읽어들인다. 
# 읽어들인 dataframe를 data에 세팅
data = pd.read_csv(file, nrows=5, header=None)

# DataFrame를 Numpy로 빌드한다. 
data_array = data.values

# data 타입을 출력한다. 
print(type(data))
print(type(data_array))
