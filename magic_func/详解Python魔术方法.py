__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/4/13
"""
    Description:
       http://www.pythontab.com/html/2016/pythonjichu_1207/1109.html
    Python的魔术方法一般以__methodname__的形式命名，如：__init__（构造方法）, __getitem__、 __setitem__（subscriptable所需method）, __delitem__（del obj[key]所需method）, __len__（len(…)所需method）等。
    在Python中，如果我们想实现创建类似于序列和映射的类，可以通过重写魔法方法__getitem__、__setitem__、__delitem__、__len__方法去模拟。
魔术方法的作用：
__getitem__(self,key):返回键对应的值。
__setitem__(self,key,value)：设置给定键的值
__delitem__(self,key):删除给定键对应的元素。
__len__():返回元素的数量

这些魔术方法的原理就是：当我们对类的属性item进行下标的操作时，首先会被__getitem__()、__setitem__()、__delitem__()拦截，
从而进行我们在方法中设定的操作，如赋值，修改内容，删除内容等等。
"""
print('Demo'.center(15, "-"))
'''
    desc：尝试定义一种新的数据类型
          等差数列
    author
'''

class ArithemeticSequence(object):
    def __init__(self, start=0, step=1):
        print("Call func __init__")
        self.start = start
        self.step = step
        self.myData = {}

    # 定义获取值的方法
    def __getitem__(self, key):
        print("Call func __getitem__")
        try:
            return self.myData[key]
        except KeyError:
            return self.start + key * self.step

    # 定义赋值方法
    def __setitem__(self, key, value):
        print("Call func __setitem__")
        self.myData[key] = value

        # 定义获取长度的方法

    def __len__(self):
        print("Call func __len__")
        return len(self.myData) + 1

        # 定义删除元素的方法

    def __delitem__(self, key):
        print("Call func __delitem__")
        del self.myData[key]
        print(self.myData)


if __name__ == '__main__':
    s = ArithemeticSequence(1, 2)
    print(s[3])
    s[3] = 100
    print(s[3])
    print(len(s))
    del s[3]
    print(s[3])
