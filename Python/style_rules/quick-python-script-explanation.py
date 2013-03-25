#!/usr/bin/env python
#-*- coding: utf-8 -*-

# FileName: quick-python-script-explanation.py
# Date: Mon Mar 25 14:43:44 CST 2013
# Author: Dong Guo

# Quick Python Script Explanation for Programmers
# 给程序员的超快速Py脚本解说

import os  #模块名，其实导入了os.py

def main():  #函式名"main"在这儿并不是必须的，调用在这段脚本的最后部分
    print 'Hello World!'

    print "这是Alice\'的问候."  #声明单行字串，使用双/单引号都成，注意对字串中的引号进行逃逸处理
    print "这是Bob\'的问候."

    foo(5, 10)  #函式调用，声明在后述代码

    print '=' * 10  #字符可乘，等于:'=========='
    print '这将直接执行'+os.getcwd()  #调用了os模块中的函式，并连接字串

    counter = 0  #变量得先实例化才可进一步计算
    counter += 1

    food = ['苹果','杏子','李子','梨']  #内置的列表类型对象，其实可以包含不同类型数据，甚至可以包含其它列表对象
    for i in food:
        print '俺就爱整只：'+i

    print '数到10'
    for i in range(10):
        print i

def foo(param1, secondParam):  #函式声明，注意使用冒号结束声明
    res = param1+secondParam  #字串的格式化输出
    print '%s 加 %s 等于 %s' %(param1, secondParam, res)
    if res < 50:
        print '这个'
    elif (res>=50) and (param1==42) or (secondParam==24):
        print '那个'
    else:
        print '嗯...'
    return res  #这是单行注释
    '''这是多
行注释......'''

if __name__=='__main__':  
    '''一般在脚本最后调用主函数 main(); 而且使用内置的运行脚本名来判定；当且仅当我
    们直接运行当前脚本时，__name__ 才为 __name__ ，这样当脚本被当做模块进行 import
    导入时，并不运行 main() ，所以，一般这里是进行测试代码安置的...'''
    main()
