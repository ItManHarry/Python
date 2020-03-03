# 并发编程 + 网络编程

## Python的网络模块

	- socket
	
	- email
	
	- smtplib
	
	-poplib
	
	- urllib	

- 使用urllib.parse解析、恢复URL

	- urllib.parse：用于解析URL
	
	- 使用urlparse()函数来执行字符串解析
	
```python
	import urllib.parse
	url = "http://baidu.com/index.html;abc?name=aaa#myflags"
	r = urllib.parse.urlparse(url)
	print(r)
	print('协议 ：', r.scheme, r[0])
	print('位置 ：', r.netloc, r[1])
	print('路径 ：', r.path, r[2])
	print('参数 ： ', r.params, r[3])
	print('查询字符串 ：', r.query, r[4])
	print('片段 ：', r.fragment, r[5])
	print('*' * 120)
```

	- 使用urlunparse()函数来恢复成URL字符串
	
```python
	import urllib.parse
	e = ('https','www.baidu.com:8080','/index.html','haha','name=Harry','frag')
	print(urllib.parse.urlunparse(e))
```

- 使用urllib.parse解析、恢复查询字符串

	- parse_qs()和parse_qsl()(l代表list)两个函数都用于解析查询字符串，只不过返回值不同，前者返回字符串，后者返回list
	
```python
	import urllib.parse
	qs = "name=Harry&name=Jack&age=37&height=170"
	print(urllib.parse.parse_qs(qs))
	print(urllib.parse.parse_qsl(qs))
```
	
	- urlencode()则是他们的逆向函数
	
```python
	import urllib.parse
	l = [('name','Sam'),('name','Tom'),('age',36),('height', 170)]
	print(urllib.parse.urlencode(l))
	d = {'name':'Harry','age':36,'height':170,'name':'Henry'}
	print(urllib.parse.urlencode(d))
```

## 使用urllib模块读取网络资源及提交请求

- 打开URL对应的资源

	urllib.request子模块下的urllib.request.urlopen(url,data=None)方法，该方法用于打开URL指定的资源，并从中读取数据

- 发送请求参数

	1. 使用urlopen()函数时，可以使用data参数向被请求的URL发送数据
	
	2. 如果是GET请求，只要将请求参数追加到URL后面即可
	
```python
	params = {'y':2019,'m':12}
	with ur.urlopen('http://10.41.129.35/esb/scb/funnel/bonus/getData.do?%s' %up.urlencode(params)) as f:
		print(f.read().decode('UTF-8'))
```

- 发送不同的请求

```python
	#POST请求使用data传入产生
	print('-' * 190)
	params = {'p1':300,'p2':400}
	with ur.urlopen('http://localhost:8080/esb/test/rep/post.do',data=up.urlencode(params).encode('utf-8')) as f:
		print(f.read().decode('UTF-8'))
	params = {'p1':300,'p2':400}
	req = ur.Request(url='http://localhost:8080/esb/test/rep/post.do?%s' %up.urlencode(params) ,method='POST')
	with ur.urlopen(req) as f:
		print(f.read().decode('UTF-8'))
	print('-' * 190)  
	#如果需要发送PUT\PATCH\DELETE等请求，需要创建Request对象
	params = {'p1':100,'p2':200}
	req = ur.Request(url='http://localhost:8080/esb/test/rep/put.do?%s' %up.urlencode(params) ,method='PUT')
	#req = ur.Request(url='http://localhost:8080/esb/test/rep/put.do', data=up.urlencode(params).encode('utf-8')  ,method='PUT')
	with ur.urlopen(req) as f:
		print(f.read().decode('UTF-8'))
	print('-' * 190)   
```

- 读取受保护的资源

- TCP协议

	TCP协议被称作一种可靠的端对端协议。TCP协议让他们建立一个连接，用于发送接收数据的虚拟链路。TCP协议保证数据传输的准确性

- 创建socket - 服务端

	1. 创建socket对象
	
	2. socket.socket(family=AF_INEF,type=SOCK_STREAM,proto=0,fileno=None)
	
	3. 绑定IP地址、端口，并在该IP、端口监听，用于监听来自客户端的连接
	
	4. socket.bind(address):绑定指定的address，该address参数可以是一个元组，包含IP地址和端口
	
	5. socket.accept():接收来自客户端的连接
	
```python
	#创建socket
	import socket
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
		#通过sc与客户端进行通信
		sc.send('Hello, I am the server.')
		sc.close()
```

- 创建socket - 客户端

```python
	import socket
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# 调用connect连接服务器
	client.connect(('10.40.122.215',3000))
	#通信
	print(client.recv(2048).decode('utf-8'))
```

- 加入多线程

	1. 通过threading.Thread创建线程
	
	2. 服务端为每个客户端启动一条进程，保证客户端互不干扰
	
	3. 客户端为网络IO启动一线程，为用户交互启动一条线程
	
服务端：

```python
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
```

客户端：

```python
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
```

- 发送邮件（smtplib）

	1. 连接SMTP服务器，并使用账户密码登录服务器
	
	2. 创建EmailMessage对象，该对象代表了邮件本身
	
	3. 调用代表与SMTP服务器的连接对象的sendmail()方法发送邮件
	
- 普通发送

```python
	import smtplib
	import email.message as em
	#邮箱账户
	account = '280688074@qq.com'
	#安全码
	code = 'fzbifrurnhhwcajd'
	#连接SMTP服务器
	# smtplib.SMTP()          #普通的SMTP连接
	#server = smtplib.SMTP_SSL('smtp.qq.com',, 21)
	# smtplib.SMTP_SSL()  #基于SSL的SMTP连接
	server = smtplib.SMTP_SSL('smtp.qq.com', 465)
	server.set_debuglevel(1)
	#登录邮箱服务器
	server.login(account, code)
	#创建邮件对象
	message = em.EmailMessage()
	#设置邮件内容	
	message.set_content('The mail from python application.')
	#执行邮件发送
	server.sendmail(account, ['guoqian.cheng@doosan.com'], message.as_string())
	#断开连接
	server.quit()
```

- 附件发送

```python
	import smtplib
	import email.message as em
	import email.utils as eu
	#邮箱账户
	account = '280688074@qq.com'
	#安全码
	code = 'fzbifrurnhhwcajd'
	#连接SMTP服务器
	# smtplib.SMTP()          #普通的SMTP连接
	#server = smtplib.SMTP_SSL('smtp.qq.com',, 21)
	# smtplib.SMTP_SSL()  #基于SSL的SMTP连接
	server = smtplib.SMTP_SSL('smtp.qq.com', 465)
	server.set_debuglevel(1)
	#登录邮箱服务器
	server.login(account, code)
	#创建邮件对象
	message = em.EmailMessage()
	#设置邮件内容 - 普通邮件
	#message.set_content('The mail from python application.')
	#设置邮件内容 - HTML邮件
	att_id1 = eu.make_msgid()
	message.set_content("""
		<h2>The mail from python application.</h2>
		<div style = 'border:1px solid red'>HTML邮件内容</div>
		<img src = 'cid:%s'/>
	""" %att_id1[1:-1], 'html', 'utf-8')
	#设置邮件标题
	message['subject']='HTML邮件测试-带有附件'
	#设置发件人
	message['from']='Harry <%s>' %account
	#设置收件人
	message['to']='ChengGuoqian <%s>' %'guoqian.cheng@doosan.com'
	#添加附件 - 二进制读取
	with open('e:/th.jpg', 'rb') as f:
		message.add_attachment(f.read(), maintype='image',subtype='jpeg',filename='picture.jpg',cid=att_id1)
	with open('e:/harry.jpg', 'rb') as f:
		message.add_attachment(f.read(), maintype='image',subtype='jpeg',filename='me.jpg')    
	with open('e:/test.xlsx', 'rb') as f:
		message.add_attachment(f.read(), maintype='file',subtype='excel',filename='test.xlsx')     
	#执行邮件发送
	server.sendmail(account, ['guoqian.cheng@doosan.com'], message.as_string())
	#断开连接
	server.quit()
```

- 接收邮件
