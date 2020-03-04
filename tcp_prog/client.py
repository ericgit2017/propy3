# coding:utf-8

import socket


def conn_ser():
    # 连接地址设置
    # ip_port = ("127.0.0.1", 9999)
    ip_port = ("192.168.45.131", 9999)

    # 创建socket对象
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 连接服务器
    sk.connect(ip_port)
    
    while True:
        inp = input("请输入发送内容：").strip()
        # 防止输入空信息产生异常
        if not inp:
            continue
        # 发送数据
        sk.sendall(inp.encode('utf-8'))

        if inp == "exit":
            print("通讯结束")
            break
        # 接收数据
        recv_data = sk.recv(1024).decode('utf-8')
        print(recv_data)
    # 关闭socket
    sk.close()


if __name__ == "__main__":
    conn_ser()

