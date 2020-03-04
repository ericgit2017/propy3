# coding:utf-8
"""
@author: Wonder
@file: Exam04.py
@time: 2020/03/03
"""
import sys
import time

# 从控制台重定向到文件
# f_handler = open('out.log', 'w')
# sys.stdout = f_handler
# print('hello')
# # 你无法在屏幕上看到“hello”
# # 因为它被写到out.log文件里了


def bar(num, total):
    rate = num / total
    rate_num = int(rate * 100)
    r = '\r[%s%s]%d%%' % ("="*num, " "*(100-num), rate_num, )
    # sys.stdout.write(r)
    # sys.stdout.flush()
    print(r, end="")


if __name__ == '__main__':
    for i in range(0, 101):
        time.sleep(0.3)
        bar(i, 100)
