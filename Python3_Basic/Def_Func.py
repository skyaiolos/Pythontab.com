__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/4/27
"""
    Description:
        4.6. 定义函数
"""


# 我们可以创建一个用来生成指定边界的斐波那契数列的函数:
def fib1(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


if __name__ == '__main__':
    fib1(2000)
    f_2000 = fib2(2000)
    print(f_2000)
