__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/4/13
"""
    Description:
        http://www.pythontab.com/html/2016/pythonjichu_1205/1108.html
    1.  单继承时super()和__init__()实现的功能是类似的
         * 区别是使用super()继承时不用显式引用基类。
"""
print("单继承时super()和__init__()实现的功能是类似的")


class Base:
    def __init__(self):
        print("Base create")


class childA(Base):
    def __init__(self):
        print("Create A")
        Base.__init__(self)


class childB(Base):
    def __init__(self):
        print("Create B")
        super(childB, self).__init__()


if __name__ == '__main__':
    base = Base()
    print()
    a = childA()
    print()
    b = childB()
    print("区别是使用super()继承时不用显式引用基类。")
