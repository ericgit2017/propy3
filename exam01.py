# coding:utf-8
import time
import urllib.request as urllib2
from functools import reduce
import os
import re


proxy_ip = []


def get_files(path):
    for dirs in os.walk(path):
        print("目录：%s 中文件如下：" % dirs[0], )
        for fi in dirs[2]:
            print("=======> ", fi)
        print()


def test_lambda(inlist):
    result = 0
    for i in inlist:
        result += i
        yield result


def lei_jia(my_list):
    sum_itr = test_lambda(my_list)
    res = [x for x in sum_itr]
    print(res)


def map_reduce_filter(my_list):
    print("==========================================================")
    print("输入列表my_list：                                      ", my_list)
    print("Map函数map(lambda x: x*x, my_list)测试结果：           ", [val for val in map(lambda x: x * x, my_list)])
    print("Reduce函数reduce(lambda x, y: x+y, my_list)测试结果：  ", reduce(lambda x, y: x + y, my_list))
    print("Filter函数filter(lambda x: x%2 != 0, my_list)测试结果：", [val for val in filter(lambda x: x % 2 != 0, my_list)])


def get_proxy_ip():
    rep = re.compile(r"""<tr>
                    <td data-title="IP">(.+?)</td>
                    <td data-title="PORT">(.+?)</td>
                    <td data-title="匿名度">.+?</td>
                    <td data-title="类型">(.+?)</td>
                    <td data-title="位置">(.+?)</td>
                    <td data-title="响应速度">.+?</td>
                    <td data-title="最后验证时间">.+?</td>
                </tr>""")
    for i in range(1, 3):
        source_url = r"https://www.kuaidaili.com/free/inha/%d/" %i
        req = urllib2.urlopen(source_url)
        htm = req.read().decode("utf-8")
        for row in rep.findall(htm):
            # print([x for x in res])
            ip_port = row[0]+":"+row[1]
            types = row[2]
            addr = row[3]
            rl = [ip_port, types, addr]
            proxy_ip.append(rl)
        time.sleep(0.8)

    for x in proxy_ip:
        print(x)


def test_fork():
    pid = os.fork()
    if pid == 0:
        print("this is the child id:%d  -- it's parent id:%d" % (pid, os.getppid()))
    else:
        print("this is the parent id:%d, --- it's parent id:%d" % (pid, os.getppid()))


def main():
    my_list = [1, 2, 3, 4, 5, 6, 7]
    # get_files("D:\\software\\PycharmProjects\\PythonExams")
    # 自定义lambda函数学习
    # lei_jia(my_list)
    # 学习map、reduce、filter函数使用
    # map_reduce_filter(my_list)
    # 学习简单网页爬虫
    # get_proxy_ip()
    # 学习并行，多进程和多线程
    test_fork()


if __name__ == "__main__":
    main()
