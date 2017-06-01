__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/4/18
"""
    Description:
divmod(a,b)函数
中文说明：
divmod(a,b)方法返回的是a//b（除法取整）以及a对b的余数

返回结果类型为tuple

参数：
a,b可以为数字（包括复数）

版本：
在python2.3版本之前不允许处理复数，这个大家要注意一下

英文说明：
Take two (non complex) numbers as arguments and
return a pair of numbers consisting of their quotient
and remainder when using long division. With mixed operand types,
the rules for binary arithmetic operators apply. For plain and long integers,
the result is the same as (a // b, a % b). For floating point numbers the result is (q, a % b),
 where q is usually math.floor(a / b) but may be 1 less than that.
 In any case q * b + a % b is very close to a, if a % b is non-zero it has the same sign as b,
 and 0 <= abs(a % b) < abs(b).
Changed in version 2.3: Using divmod() with complex numbers is deprecated.

"""
print("python代码实例：")
d1 = divmod(9, 2)
print(d1)
d2 = divmod(11, 3)
print(d2)
# d3 = divmod(1 + 2j, 1 + 0.5j)
# print(d3)

if __name__ == '__main__':
    pass
