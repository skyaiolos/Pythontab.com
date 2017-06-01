__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/4/13
"""
    Description:
        http://www.pythontab.com/html/2017/pythonjichu_0307/1121.html
         python中的struct主要是用来处理C结构数据的，读入时先转换为Python的字符串类型，然后再转换为Python的结构化类型，比如元组(tuple)啥的~。一般输入的渠道来源于文件或者网络的二进制流。

1.struct.pack()和struct.unpack()
    在转化过程中，主要用到了一个格式化字符串(format strings)，用来规定转化的方法和格式。
    下面来谈谈主要的方法：
1.1 struct.pack(fmt,v1,v2,.....)
　　将v1,v2等参数的值进行一层包装，包装的方法由fmt指定。被包装的参数必须严格符合fmt。最后返回一个包装后的字符串。
1.2 struct.unpack(fmt,string)
　　顾名思义，解包。比如pack打包，然后就可以用unpack解包了。返回一个由解包数据(string)得到的一个元组(tuple), 即使仅有一个数据也会被解包成元组。其中len(string) 必须等于 calcsize(fmt)，这里面涉及到了一个calcsize函数。struct.calcsize(fmt)：这个就是用来计算fmt格式所描述的结构的大小。

 　 格式字符串(format string)由一个或多个格式字符(format characters)组成，对于这些格式字符的描述参照Python manual如下:

Format  c Type      Python Note
x       pad byte    no value
c       char string of length 1
b       signedchar integer
B       unsignedchar integer
?       _Bool bool (1)
h       short integer
H       unsignedshort integer
i       int integer
I       unsignedint integer or long
l       long integer
L       unsignedlong long
q       longlong long (2)
Q       unsignedlonglong long (2)
f       float float
d       double float
s       char[] string
p       char[] string
P       void* long

"""
print('2.代码示例'.center(18, '-'))
import struct

# native byteorder
buffer = struct.pack('ihbb', 0, 4, 2, 6)
print(repr(buffer))
print(struct.unpack('ihbb', buffer))

# data from a sequence, network byteorder
data = [0, 4, 2, 6]
buffer = struct.pack("!ihbb", *data)
print(repr(buffer))
print(struct.unpack("!ihbb", buffer))

if __name__ == '__main__':
    pass
