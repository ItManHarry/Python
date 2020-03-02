#创建socket
import socket
import threading
clients = []
def server_target(server):
     while True:
        content = server.recv(2048).decode('utf-8')
        if content:
            #打印客户端传输的数据
            print(content)
            #将当个客户端发送的数据分发给各个客户端
            for c in clients:
                c.send(content.encode('utf-8'))
#第一个参数指定网络类型：AF_INET代表ipv4的网络，AF_INET6代表IPV6的网络，AF_UNIX代表UNIX的网络
#第二个参数指定Socket类型，SOCK_STREAM（TCP协议） SOCK_DGRAM(UDP协议)
#创建socket对象
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定到指定的IP地址和端口
s.bind(('10.40.122.215',3000))
#监听
s.listen()
#接收
while True:
    print('waiting for connect...')
    #该方法返回两个值，客户端socket及客户端的地址
    sc, address = s.accept()
    print('Address : ' , address)
    #将客户端对应的socket放到一个列表中
    clients.append(sc)
    #为客户端对应的socket启动对应的线程
    threading.Thread(target=server_target,args=(sc,)).start()