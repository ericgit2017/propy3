# coding:utf-8
"""
@author: Wonder
@file: eastmoney.py
@time: 2020/03/10
"""
import requests
from bs4 import BeautifulSoup
import time
import random
import multiprocessing

user_agent = ["Mozilla/5.0 (Windows NT 10.0; WOW64)", 'Mozilla/5.0 (Windows NT 6.3; WOW64)',
              'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
              'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
              'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.95 Safari/537.36',
              'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET '
              'CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; rv:11.0) like Gecko)',
              'Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1',
              'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3',
              'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12',
              'Opera/9.27 (Windows NT 5.2; U; zh-cn)',
              'Mozilla/5.0 (Macintosh; PPC Mac OS X; U; en) Opera 8.0',
              'Opera/8.0 (Macintosh; PPC Mac OS X; U; en)',
              'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.12) Gecko/20080219 Firefox/2.0.0.12 '
              'Navigator/9.0.0.6',
              'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Win64; x64; Trident/4.0)',
              'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)',
              'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; '
              '.NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E)',
              'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Maxthon/4.0.6.2000 '
              'Chrome/26.0.1410.43 Safari/537.1 ',
              'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; '
              '.NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E; '
              'QQBrowser/7.3.9825.400)',
              'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0 ',
              'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.92 '
              'Safari/537.1 LBBROWSER',
              'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; BIDUBrowser 2.x)',
              'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 '
              'TaoBrowser/3.0 Safari/536.11']


def get_proxy_ip(q, url, test_url):
    print("\033[1;34m="*30, "处理网页：", url, "="*30, "\033[0m")
    response = requests.get(url, headers={"User-Agent": random.choice(user_agent)})
    soup = BeautifulSoup(response.content.decode("gbk"), "lxml")
    trs = soup.find("table", attrs={"bordercolor": "#6699ff"}).find_all("tr")
    for tr in trs[1:]:
        ip = tr.find_all("td")[0].get_text()
        port = tr.find_all("td")[1].get_text()
        proxy = "http://" + ip + ":" + port
        # 验证代理是否可用，如果不可以则抛出异常
        try:
            proxies = {"http": proxy}
            response = requests.get(test_url, headers={"User-Agent": random.choice(user_agent)}, proxies=proxies,
                                    timeout=3)
            if response.status_code == 200:
                print(proxy)
                with open("ipList.txt", "a", encoding="utf-8") as f:
                    f.write(proxy + "\n")
                    f.close()
        except Exception as ex:
            # print(ex)
            continue
    time.sleep(random.randint(3, 5))


def agent_access():
    test_url = "http://blog.csdn.net"
    # 进程间通信队列
    q = multiprocessing.Manager().Queue()
    # 创建进程池
    po = multiprocessing.Pool(5)

    for i in range(1, 1912):
        url = "http://www.66ip.cn/" + str(i) + ".html"
        po.apply_async(get_proxy_ip, args=(q, url, test_url, ))

    po.close()
    po.join()


if __name__ == '__main__':
    agent_access()
