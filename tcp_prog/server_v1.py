# coding:utf-8
"""
@author: Wonder
@file: server_v1.py
@time: 2020/03/04
"""
import socket
import threading


def conn_handler(conn, client):
    """
    该函数为线程需要执行的函数，负责具体的服务器和客户端之间的通信工作
    :param conn: 当前线程处理的连接
    :param client: 客户端ip和端口信息，一个二元元组
    :return: None
    """
    print("服务器开始接收来自[%s:%s]的数据！" % (client[0], client[1]))
    while True:
        recv_data = conn.recv(1024).decode("utf-8")
        if recv_data == "exit":
            print("结束与[%s:%s]的通讯连接！" % (client[0], client[1]))
            break
        print("来自[%s:%s]的客户端发来信息：%s" %(client[0], client[1], recv_data))
        conn.sendall("服务器已收到信息！")
    conn.close()


def main():
    # 设置监听地址
    ip_port = ("192.168.45.131", 9999)
    # 创建socket对象
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定该对象到监听地址
    sock.bind(ip_port)
    # 开始监听该地址
    sock.listen(5)
    print("启动socket，等待客户端连接")
    while True:
        # 定义无限循环接收客户端连接
        conn, addr = sock.accept()
        # 处理连接
        tch = threading.Thread(target=conn_handler, args=(conn, addr))
        tch.start()


if __name__ == '__main__':
    main()
