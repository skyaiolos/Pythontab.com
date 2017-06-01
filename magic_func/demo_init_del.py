__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/5/22
"""
    Description:
        http://www.cnblogs.com/zhepama/p/3536016.html
        这里是一个 __init__ 和 __del__ 实际使用的例子。
"""
from os.path import join


class FileObject:
    '''给文件对象进行包装从而确认在删除时文件流关闭'''

    def __init__(self, file_path='~', file_name='sample.txt'):
        self.file = open(join(file_path, file_name), 'r+')

    def __del__(self):
        self.file.close()
        del self.file


data_file = FileObject(file_path="D:\Demo_python\Pythontab\magic_func", file_name='data.txt')

