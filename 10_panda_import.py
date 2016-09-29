# _*_ coding: utf-8 _*_
import pandas as pd

file = 'titanic.csv'

# 데이터 프레임으로 읽기
df = pd.read_csv(file)

# 헤더 출력하기. 
print(df.head())

