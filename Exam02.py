# coding:utf-8
import time


def build_conn_string(params):
    """Build a connection string from a dictionary of parameters.

    Return string."""
    return ";".join(["%s=%s" % (k, v) for k, v in params.items()])


def func1():
    while True:
        print("----------11----------")
        time.sleep(0.2)
        yield


def func2():
    while True:
        print("----------22----------")
        time.sleep(0.2)
        yield


def ass_exam():
    f1 = func1()
    f2 = func2()
    i = 100
    while i > 0:
        next(f1)
        next(f2)
        i -= 1


def decorator1(func):
    print("-----decorator1开始装饰-----")

    def td_func(*args, **kwargs):
        args = ("wangw", 55, 'dddd')
        return "<td>" + func(*args, **kwargs) + "</td>"

    return td_func


def decorator2(func):
    print("-----decorator2开始装饰-----")

    def tr_func(*args, **kwargs):
        args = ("mal", 66, 'sssssssss')
        ret = "<tr>" + func(*args, **kwargs) + "</tr>"
        return ret

    return tr_func


@decorator2
@decorator1
def dec_exam(name, aa, key="dbs"):
    key = 'jjjj'
    return "hello world %s %d %s" % (name, aa, key)


if __name__ == "__main__":
    dic_paras = {
        "server": "192.168.45.128",
        "database": "master",
        "uid": "root",
        "password": "root"
    }
    # print(build_conn_string(dic_paras))
    # ass_exam()
    print(dec_exam())
