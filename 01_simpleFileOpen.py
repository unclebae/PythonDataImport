# _*_ coding: utf-8 _*_

# 파일을 오픈한다. 
file = open('doc.txt', mode='r')

# 파일내용 출력하기. 
print(file.read())

# 파일이 닫혔는지 검사한다. 
print(file.closed)

# 파일을 실제 닫는다. 
file.close()

# 파일이 최종적으로 닫혔는지 검사한다. 
print(file.close())
