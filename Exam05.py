# coding:utf-8

import os
import sys


def get_curpath_files():
    try:
        for root, dirs, files in os.walk(os.curdir):
            print("\033[1;31m>"*7, "directory", "<%s>\033[0m" % root)
            for dirt in dirs:
                print("\033[1;34m<DIR>   %s\033[0m" % dirt)
            for file in files:
                print("\t\t%s" % file)
    except OSError as ex:
        print(ex)


def main():
    get_curpath_files()


if __name__ == '__main__':
    main()

