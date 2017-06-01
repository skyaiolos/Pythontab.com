__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

#!/usr/bin/python3 
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/5/10
"""
    Description:
      9、装饰器（Decorators）
一个decorator只是一个带有一个函数作为参数并返回一个替换函数的闭包。
我们将从简单的开始一直到写出有用的decorators。

"""
def outer(some_func):
    def inner():
        print("before some_func")
        ret = some_func()

