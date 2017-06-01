__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/4/13
"""
    Description:
        http://www.pythontab.com/html/2016/pythonjichu_1213/1111.html
        enumerate函数用于遍历序列中的元素以及它们的下标,多用于在for循环中得到计数,
        enumerate参数为可遍历的变量，如 字符串，列表等
"""
print("一般情况下对一个列表或数组既要遍历索引又要遍历元素时，会这样写")
list = ["one", "two", "three"]

for i in range(len(list)):
    print(i + 1, list[i], )

print()
print("但是这种方法有些累赘，使用内置enumerrate函数会有更加直接，优美的做法，先看看enumerate的定义：")
for index, text in enumerate(list):
    print(index + 1, text)

print("代码实例1：".center(20, '-'))
i = 0
seq = ['one', 'two', 'three']
for element in seq:
    print(i + 1, seq[i])
    i += 1
print("代码实例2：".center(20, '-'))
for i, element in enumerate(seq):
    print(i + 1, seq[i])
print("代码实例3：".center(20, '-'))
for i, j in enumerate('abc'):
    print(i + 1, j)

if __name__ == '__main__':
    pass
