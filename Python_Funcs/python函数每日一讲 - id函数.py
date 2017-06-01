__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/4/18
"""
    Description:
        http://www.pythontab.com/html/2016/hanshu_0808/1058.html
        python函数每日一讲 - id函数
id(object)

功能：返回的是对象的“身份证号”，唯一且不变，但在不重合的生命周期里，可能会出现相同的id值。此处所说的对象应该特指复合类型的对象(如类、list等)，对于字符串、整数等类型，变量的id是随值的改变而改变的。

Python版本： Python2.x Python3.x

Python英文官方文档解释：

Return the “identity” of an object. This is an integer (or long integer) which is guaranteed to be unique and constant for this object during its lifetime. Two objects with non-overlapping lifetimes may have the same id() value.

CPython implementation detail: This is the address of the object in memory.


注：一个对象的id值在CPython解释器里就代表它在内存中的地址（Python的c语言实现的解释器）。

用is判断两个对象是否相等时，依据就是这个id值

is与==的区别就是，is是内存中的比较，而==是值的比较


"""
print("代码实例：")


class Obj():
    def __init__(self, arg):
        self.x = arg


if __name__ == '__main__':
    obj = Obj(1)
    print(id(obj))
    obj.x = 2
    print(id(obj))

    s = 'abc'
    print(id(s))
    s = 'bcd'
    print(id(s))

    x = 1
    print(id(x))
    x = 2
    print(id(x))
