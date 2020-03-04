#!/usr/bin/env python
# coding:utf-8
"""
@author: Wonder
@file: server_v2.py
@time: 2020/03/04
"""
import socketserver


class MyServer(socketserver.BaseRequestHandler):
    """必需继承自socketserver.BaseRequestHandler类"""
    def handle(self):
        """
        必须实现这个方法
        :return:
        """
        conn = self.request
        conn.sendall("欢迎访问socketserver服务器！".encode("utf-8"))
        while True:
            recv_data = conn.recv(1024).decode("utf-8")
            if recv_data == "exit":
                print("断开与%s的连接！" % (self.client_address,))
                break
            print("来自于%s的数据：%s" % (self.client_address, recv_data))
            conn.sendall(("已收到你的消息<%s>" % recv_data).encode("utf-8"))


if __name__ == '__main__':
    # 创建一个多线程TCP服务器
    server = socketserver.ThreadingTCPServer(("192.168.45.131", 9999), MyServer)
    print("启动SocketServer服务器...")
    # 启动服务器并保持一直运行
    server.serve_forever()

