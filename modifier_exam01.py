# coding=utf-8

import os
import sys
import time
from prtfunc import prt_func as pf


def main():
    # test1(10000)
    # pass
    ret = test2(100, 200, 300, name='zhangs', age=32)
    print(ret)
    
# 测试utf8
def outfunc(func):
    print('-----------开始装饰------------')
    def call_func():
        bt = time.time()
        print('Begin run..... ', bt)
        func()
        et = time.time()
        print('End run..... ', et)
        print('程序运行时间：%f' %(et - bt))
    return call_func
    
def outfunc1(func):
    print('-----------开始装饰1------------')
    def call_func(num):
        bt = time.time()
        print('Begin run..... ', bt)
        func(num)
        et = time.time()
        print('End run..... ', et)
        print('程序运行时间：%f' %(et - bt))
    return call_func
    
def outfunc2(func):
    def call_func(*args, **kwargs):
        bt = time.time()
        print("Begin run......", bt)
        return func(*args, **kwargs)
        et = time.time()
        print("End run....", et)
        print("程序运行时间：%f" %(et - bt))
    return call_func
    
@outfunc
@pf
def test():
    print('hello world ')
    
@outfunc1
def test1(num):
    print('The para is: %d' %num)

@outfunc2
@pf
def test2(num, *args, **kwargs):
    print('First para: ', num)
    print('Second para: ', args)
    print('Third para: ', kwargs)
    return 'ok'
    

if __name__=="__main__":
    main()
    time.sleep(5)