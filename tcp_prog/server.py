# coding:utf-8

import os
import sys
import socket


def create_conn():
    # ip_port = ('127.0.0.1', 9999)
    ip_port = ('192.168.45.131', 9999)

    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.bind(ip_port)
    sk.listen(5)
    print('启动socket服务，等待客户端连接...')
    conn, addr = sk.accept()
    while True:
        recv_data = conn.recv(1024).decode('utf-8')
        if recv_data == 'exit':
            exit("通信结束")
        print("来自%s的客户端向你发来信息：%s" % (addr, recv_data))
        conn.sendall("服务器已收到你的信息".encode('utf-8'))
    conn.close()


def main():
    create_conn()


if __name__ == '__main__':
    main()

