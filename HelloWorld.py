# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import keyword

def print_line():
    print('------------------------------')

print('Hello World!')
print_line()

# Python关键字集合
print(keyword.kwlist)
print_line()

if True:
    print('True')
else:
    print('False')
print_line()

str='Runoob'
 
print(str)                 # 输出字符串
print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
print(str[0])              # 输出字符串第一个字符
print(str[2:5])            # 输出从第三个开始到第五个的字符
print(str[2:])             # 输出从第三个开始后的所有字符
print(str * 2)             # 输出字符串两次
print(str + '你好')        # 连接字符串
print_line()
 
print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义
print_line()

#t = input("Pleasee Input:")
print_line()


import sys
print('================Python import mode==========================')
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)
print_line()

a, b, c = 1, 2.1, "runoob"
if isinstance(b, int):
    print('True')
else:
    print('False')
print_line()
