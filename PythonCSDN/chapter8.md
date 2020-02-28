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

- 发送不同的请求

- 读取受保护的资源
