# _*_ coding: utf-8 _*_

with open('doc.txt') as file :
    print(file.readline())
    print(file.readline())
    print(file.readline())

    print ('----------------------')
    for line in file :
        print(line)
