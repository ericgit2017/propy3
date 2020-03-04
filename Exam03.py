# coding:utf-8
"""
@author: Wonder
@file: Exam03.py
@time: 2020/03/03
"""
import os
import sys


def get_files():
    try:
        for root, dirs, files in os.walk(r"D:\software\PycharmProjects\PythonExams"):
            print("\033[1;31m>"*7, "directory", "<%s>\033[0m" % root)
            for dirt in dirs:
                print("\033[1;34m<DIR>   %s\033[0m" % dirt)
            for file in files:
                print("\t\t%s" % file)

    except OSError as ex:
        print(ex)
    for index, arg in enumerate(sys.argv):
        print("第 %d 个参数是： %s" % (index, arg))


def get_sys_modules():
    for key, val in sys.modules.items():
        if key not in sys.builtin_module_names:
            # val = val[]
            print("%-24s\t %s" % (key, val))


if __name__ == "__main__":
    # get_files()
    get_sys_modules()