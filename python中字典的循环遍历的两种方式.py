__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/4/14
"""
    Description:
        开发中经常会用到对于字典、列表等数据的循环遍历，但是python中对于字典的遍历对于很多初学者来讲非常陌生，
        今天就来讲一下python中字典的循环遍历的两种方式。
;

"""
print("1. 只对键的遍历".center(15, '-'))
d = {'name1': 'pythontab', 'name2': '.', 'name3': 'com'}
for key in d:
    print(key, 'value : ', d[key])
print()
print("2. 对键和值都进行遍历 需要 ： items()".center(25, '-'))
for key, value in d.items():
    print(key, 'value : ', value)

if __name__ == '__main__':
    pass
