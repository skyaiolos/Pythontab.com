__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/5/10
"""
    Description:
        http://www.pythontab.com/html/2013/pythonjichu_0219/236.html
         Python和c++一样，可以定义类，可以继承，类中又包含了类变量、实例变量
        （私有变量和公有变量）、方法（包括静态方法staticmethod、类方法classmethod和实例方法instancemethod）。
         这里只着重介绍类的成员。
"""


class Myclass:
    '''I simple example class'''
    val1 = 'Value 1'  # 类变量
    val4 = 1

    def __init__(self):
        self.val2 = 'Value 2'  # 公有实例变量
        self.__val3 = 'Value 3'  # 公有实例变量

    def __func():
        print('val1 : ', Myclass.val1)
        print("static method cannot access val2")
        print("static method cannot access __val3")
        print("val4 : ", Myclass.val4)
        Myclass.val4 = ((Myclass.val4 + 1))

    smd = staticmethod(__func)

    def __func2(cls):
        print('val1 : ', cls.val1)
        print('class method cannot access val2')
        print('class method cannot access __val3')
        print('val4 : ', Myclass.val4)
        cls.val4 = ((cls.val4 + 1))

    cmd = classmethod(__func2)

    def func3(self):
        print('val1 : ', self.val1)
        print('val2 : ', self.val2)
        print('instance method cannot access __val3')
        print('val4 : ', self.val4)
        self.val4 = ((self.val4 + 1))


if __name__ == '__main__':
    print('--------------------MyClass.smd()-------------------')
    Myclass.smd()  # 类调用静态方法
    print('--------------------MyClass.cmd()-------------------')
    Myclass.cmd()  # 类调用类方法
    # MyClass.func3()       # 类无法直接调用实例方法

    x = Myclass()
    print('--------------------x.smd()-------------------')
    x.smd()  # 实例调用静态方法
    print('--------------------x.cmd()-------------------')
    x.cmd()  # 实例调用类方法
    print('--------------------x.func3()-------------------')
    x.func3()  # 实例调用实例方法
    # 结果
