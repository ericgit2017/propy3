# coding=utf-8

def prt_func(func):
    def call_func(*args, **kwargs):
        print("call func ", func)
        return func(*args, **kwargs)
    return call_func
