import socket
import threading
def readFromServer(client):
    while True:
        content = client.recv(2048).decode('utf-8')
        if content:
            print(content)            
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 调用connect连接服务器
client.connect(('10.40.122.215',3000))
#将读取服务器端函数以多线程方式启动，这样的函数可与以下的死循环并发执行
threading.Thread(target=readFromServer,args=(client,)).start()
#通信
while True:
    line = input('Please Input(input exit to abord) : ')
    print('Your input is : ', line)
    if line and line != 'exit':
        client.send(line.encode('utf-8'))
    else:
        print('You have not input any data or input exit order, socket break')
        break
client.close()        