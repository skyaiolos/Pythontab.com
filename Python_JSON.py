__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/4/13
"""
    Description :
        http://www.pythontab.com/html/2017/pythonjichu_0413/1127.html
        使用 JSON 函数需要导入 json 库：import json。
        函数:            描述:
        json.dumps      将 Python 对象编码成 JSON 字符串
        json.loads      将已编码的 JSON 字符串解码为 Python 对象

# python 原始类型向 json 类型的转化对照表：

|Python        |JSON
 dict           object
 list,tuple     array
 str,unicode    string
 int,long,float number
 True           true
 False          false
 None           null

"""
# 实例1:
# 以下实例将数组编码为 JSON 格式数据：
import json

data = {'number': 6, 'name': 'Pythontab'}
print("实例1".center(10, '-'))
jsonData = json.dumps(data)
print(jsonData, '\n')

# 实例2:
# 使用参数让 JSON 数据排序并格式化输出：
print("实例2".center(10, '-'))
jsonData2 = json.dumps(data, sort_keys=True, indent=4, separators=(',', ':'))
print(jsonData2, '\n')

# 实例3:
# json.loads 用于解码 JSON 数据。该函数返回 Python 字段的数据类型。
"""
语法:
json.loads(s[, encoding[, cls[, object_hook[, parse_float[, parse_int[, parse_constant[, object_pairs_hook[, **kw]]]]]]]])

"""
print("实例3".center(10, '-'))
json_str = json.loads(jsonData)
print(json_str, '\n')

# 使用第三方库：Demjson

# Looping skill
for k, v in data.items():
    print("{}: {}".format(k, v))
print('enumerate Demo'.center(18, '-'))
for i, v in enumerate(['one', 'two', 'three']):
    print("{}: {}".format(i + 1, v))
if __name__ == '__main__':
    pass
