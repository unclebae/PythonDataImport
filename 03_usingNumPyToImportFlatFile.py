# _*_ coding: utf-8 _*_

# numpy 패키지 임포트하기. 
import numpy as np
import matplotlib.pyplot as mpl

# 파일 이름을 변수에 따로 저장하기. 
fileName = 'digit.csv'

# 파일 내용을 배열로 로드하기. 
# 구분자는 , 로 해서 로드한다. 
digits = np.loadtxt(fileName, delimiter=',')

# digit 타입 알아보기. 
print(type(digits))

# row선택해서 변수 할당하기,
# reshape 를 이용하여 행렬 만들기. 
im = digits[10, 1:]
im_sq = np.reshape(im, (28, 28))

# reshape데이터를 matplotlib 라이브러리로 그리기. 
mpl.imshow(im_sq, cmap='Greys', interpolation='nearest')
mpl.show()
