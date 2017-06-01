__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/4/27
"""
    Description:
        
"""
a = ['Mary', 'had', 'a', 'little', 'lamb']

for i in range(len(a)):
    print(i, a[i])

print("enumerate".center(20, '~'))
for index, value in enumerate(a):
    print(index, value)

if __name__ == '__main__':
    pass
