# coding:utf-8
"""
@author: Wonder
@file: client_v2.py
@time: 2020/03/04
"""
import socket


def conn_ser():
    # 连接地址设置
    # ip_port = ("127.0.0.1", 9999)
    ip_port = ("192.168.45.131", 9999)

    # 创建socket对象
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 连接服务器
    sk.connect(ip_port)
    sk.settimeout(5)

    recv_data = sk.recv(1024).decode('utf-8')
    print('服务器：', recv_data)

    while True:
        inp = input("你：").strip()
        # 防止输入空信息产生异常
        if not inp:
            continue
        # 发送数据
        sk.sendall(inp.encode('utf-8'))

        if inp == "exit":
            print("谢谢使用，再见！")
            break
        # 接收数据
        recv_data = sk.recv(1024).decode('utf-8')
        print("服务器：", recv_data)
    # 关闭socket
    sk.close()


if __name__ == "__main__":
    conn_ser()