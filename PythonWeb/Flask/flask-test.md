# Flask Framework 自动化测试

## 测试使用到的Python包

1. Selenium

2. Flake8

3. Coverage

## 自动化测试主要分为以下三种

- 单元测试（Unit Test）：对单独的代码块，比如函数进行测试。单元测试是自动化测试的主要形式，也是最基本的测试方式。

- 集成测试（Integration Test）：集成测试对代码单位之间的协同工作进行测试，比如测试Flask 和各个Flask 扩展的集成代码。
这部分的测试不容易编写，各个扩展通常会包含集成测试。在部署到云平台时， 集成测试可以确保程序和云平台的各个接口正常协作。

- 用户界面测试（User Interface Test）：也被称为端对端测试或全链路测试，因为需要启动服务器并调用浏览器来完成测试，所以
耗时比较长，适合用来测试复杂的页面交互，比如包含JavaScript 代码和AJAX 请求等实现的功能。

## Flask测试客户端

	Flask 通过app.test_client()方法提供了－个测试客户端，这会模拟一个Web 服务器环境。通过对程序实例app调用这个方法会返回
一个测试客户端对象，通过对这个对象调用get()和post()方法可以模拟客户端对服务器发送请求，我们可以从这两个方法返回的响应对
象获取响应数据。

- GET请求

```
	$flask shell 
	>>> client = app.test_client()
	<Response streamed [200 OK]>
	>>> response = client.get('/')
	>>> response.get_data()	＃获取字符字节串（ bytestring ）格式的响应主体
	'< 1DOCTYPE html>\n<html lang="en">\n ...
	>>> response.get_data(as_text=True)	＃获取解码为Unicode 字符串后的响应主体
	u'< 1DOCTYPE html>\n<html lang="en">\n ...
	>>>b'Say Hello' in response.get_data()
	True
	>>> response.status_code
	200
	>>> response.status_code
	'200 OK'
```

> get()方法模拟向服务器发送GET 请求，第一个参数是请求的URL 。对返回的Respons e 对
象调用get_data()方法默认返回字节字符串（ bytestring ，又被译为字节串）形式的响应主体。字
节字符串即Python2中的str 类型。在Python3 中字符串默认为unicode 类型，因此需要在字柯：
串前添加b 前缀，将字符串声明为bytes 类型。在上面为了兼容两者，我们统一添加了b 前缀：

```
	>>>b'Say Hello' in response.get_data()
	True
```

> 为了更方便处理，并支持使用中文字符进行判断，我们可以将as text 参数设为True 来获取
解码为Unicode 格式的响应主体，这时不必再添加b 前缀：

```
	>>>'Say Hello' in response.get_data(as_text=True)
	True
```

- POST请求

```
	$flask shell 
	>>> client = app.test_client()
	>>> response = client.post('/', data={'name': 'Harry', 'body': 'I am a test message'}, follow_redirects=True)
	>>> 'Your message have been sent to the world!' in response.get_data(as_text=True)
	True
	>>> ' I am a test message' in response.get_data(as_text=True)
	True
```

> 除了URL ，我们还将表单的数据以字典的形式通过data 参数传人，表单字段的name 值作为键，这里的name 和body 键
分别对应表单的name和body字段。因为表单提交后会跳转到首页，将follow_redirects参数设为True 可以跟随重定向，自
动向重定向后的页面发起GET 请求。通过判断返回的数据中是否包含通过flash()函数发送的提示消息和刚刚创建的消息内容，我们
就可以判断发表问候的功能是否正常。

## 使用unittest编写单元测试

> 自动化测试最常见的形式是单元测试。单元测试（ Unit Test ）指的是对程序代码中最小的单元进行测试， 比如Python 函数或方法。
Python 标准库内置了一个优秀的单元测试框架一－unittest 。本节我们将学习使用它来为程序编写单元测试。unittest 包含下面几个重要的概念：

1. 测试用例（Test Case）

	在unittest 中，最小的测试单元被称为测试用例，它由继承unittest. TestCas巳的类表示。每个测试用例中包含多个测试方法。
	
2. 测试固件（Test Fixtrue）

	测试固件指的是执行测试所需的前期准备工作和后期清理工作。比如创建临时的数据库，测试执行后清除数据库。测试用例可以
创建setUp()和tearDown()方法，它们会分别在每一个测试方法被执行的前后执行，这两个方法分别用来初始化测试环境、清除测试环境。
除了这两个方法，还有setUpClass()和tearDownClass()方法，这两个方法必须接收类本身作为唯一的参数，并且附加classmethod 装饰器，
它们会分别在整个测试用例执行的前后执行。

3. 测试集（Test Suite）

	测试集是测试用例的集合， 用来聚合所有测试以便执行。
	
4. 测试运行器（Test Runner）

	测试运行器用来运行测试，收集测试结果，并呈现给用户。
	
## Flask程序的测试固件

```python
	import unittest
	from chat import app, db
	class SayHelloTest(unittest.TestCase):
		def setUp(self):			
			app.config.update(
				TESTING=True,
				WTF_CSRF_ENABLED=False,
				SQLALCHEMY_DATABASE_URI='sqlite:///:memory'
			)
			self.client = app.test_client()
			db.create_all()
			
		def tearDown(self):
			db.session.remove()
			db.drop_all()
```

对程序实例调用test_client()会获得一个Werkzeug 提供的Client 类的实例，我们在setUp()方法中将其保存为类属性self.client ，
以便在测试方法中使用它来发送模拟请求。

测试时通常使用不同的配置。在上面的setUp()方法中，我们使用config 对象的update 方法一次更新多个配置。其中，我们将
TESTING 配置键设为True ， 这会开启测试模式。在测试模式下， F lask 会关闭在处理请求时的错误捕捉，从而获得更易读的错误报告。

Flask-WTF 默认开启CSRF保护，但是测试时并不需要验证CSRF，开启CSRF保护会让发送POST提交表单数据变得困难，我们
可以将配置变量WTF_CSRF_ENABLED 设为False来关闭CSRF保护。

