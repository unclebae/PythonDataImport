# _*_ coding: utf-8 _*_
import numpy as np
import matplotlib.pyplot as plt

file = 'seaslug.txt'

# 데이터를 로드한다. 
# 딜리미터는 탭으로
# 데이터 타입은 스트링으로 변환하여 로드 
data = np.loadtxt(file, delimiter='\t', dtype=str)

# 첫번째 엘리먼트를 출력한다. 
print(data[0])

# 데이터를 float타입으로 로드한다. 
# 첫번째 라인을 스킵한다. 
# 딜리미터는 탭으로 
data_float = np.loadtxt(file, delimiter='\t', dtype=float, skiprows=1)

# 10번째 elemment을 출력한다. 
print(data_float[9])

# 점 그림으로 출력한다. 
plt.scatter(data_float[:, 0], data_float[:, 1])
plt.xlabel('time (min.)')
plt.ylabel('percentage of larvae')
plt.show()
