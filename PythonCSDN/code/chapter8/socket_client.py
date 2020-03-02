import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 调用connect连接服务器
client.connect(('10.40.122.215',3000))
#通信
print(client.recv(2048).decode('utf-8'))