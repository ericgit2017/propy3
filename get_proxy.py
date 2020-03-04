# coding:utf-8

import re
import urllib.request as urllib2
import time
import threading
from functools import cmp_to_key

'''
https://www.kuaidaili.com/free/inha/1/
'''
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
proxylist = []

def get_proxy_from_kdli():
    global proxylist
    cp = re.compile(r'''<tr>
                    <td data-title="IP">(.*?)</td>
                    <td data-title="PORT">(.*?)</td>
                    <td data-title="匿名度">.*?</td>
                    <td data-title="类型">(.*?)</td>
                    <td data-title="位置">(.*?)</td>
                    <td data-title="响应速度">.*?</td>
                    <td data-title="最后验证时间">.*?</td>
                </tr>''')

    for i in range(1, 10):
        target = r"https://www.kuaidaili.com/free/inha/%d/" %i
        # print(target)
        # my_Request = urllib2.Request(target, headers=headers)
        req = urllib2.urlopen(target, timeout=10)
        htm = req.read().decode('utf-8')
        time.sleep(0.8)
        matchs = re.findall(cp, htm)
        # print(matchs)
        for row in matchs:
            ip = row[0]
            port = row[1]
            type = row[2]
            addr = row[3]
            pl = [ip, port, type, addr]
            # print(pl)
            proxylist.append(pl)
        
        # print(proxylist)
        
class ProxyCheck(threading.Thread):
    def __init__(self, proxylist, fname):
        threading.Thread.__init__(self)
        self.proxylist = proxylist
        self.fname = fname
        self.timeout = 5
        self.test_url = "http://www.baidu.com/"
        self.test_str = "030173"
        self.checked_proxy_list = []
        
    def checkProxy(self):
        #cookies = urllib2.HTTPCookieProcessor()
        for proxy in self.proxylist:
            #proxy_handler = urllib2.ProxyHandler({"http" : r"http:%s:%s" %(proxy[0], proxy[1])})
            #opener = urllib2.build_opener(cookies, proxy_handler)
            #urllib2.install_opener(opener)
            bt = time.time()
            try:
                req = urllib2.urlopen(self.test_url, timeout=self.timeout)
                htm = req.read().decode('utf-8')
                timeused = time.time() - bt
                pos = htm.find(self.test_str)
                if pos > -1:
                    #print(proxy[0], proxy[1], proxy[2], proxy[3], timeused)
                    self.checked_proxy_list.append((proxy[0], proxy[1], proxy[2], proxy[3], timeused))
                else:
                    continue
            except Exception as e:
                print(e)
                continue
    
    def sort(self):
        self.checked_proxy_list = sorted(self.checked_proxy_list, key=lambda x:(x[4], x[0]))
        
    def save(self):
        f = open(self.fname, "w+")
        for proxy in self.checked_proxy_list:
            f.write("%s:%s,%s,%s,%s\n" %(proxy[0], proxy[1],proxy[2],proxy[3],str(proxy[4])))
        f.close
        
    def run(self):
        self.checkProxy()
        self.sort()
        self.save()

        
if __name__=="__main__":
    get_proxy_from_kdli()
    t1 = ProxyCheck(proxylist, "t1.csv")
    t1.start()
