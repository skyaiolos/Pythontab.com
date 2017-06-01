__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/4/27
"""
    Description:
        http://docs.pythontab.com/python/python3.5/controlflow.html#range
        4.4. break 和 continue 语句, 以及循环中的 else 子句
"""
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n // x)
            break
    else:
        print(n, 'is a prime number')
if __name__ == '__main__':
    pass
