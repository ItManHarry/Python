# Flask Framework HTTP

## Request对象

- 使用request的属性获取请求URL

	url: http://helloflask.com/hello?name=Grey	
	
| 属性 | 值 | 
| ------------- | ------------- | 
| path | '/hello' | 
| full_path | '/hello?name=Grey' |
| host | 'helloflask.com' | 
| host_url | 'http://helloflask.com/' |
| base_url | 'http://helloflask.com/hello' | 
| url | 'http://helloflask.com/hello?name=Grey' |
| url_root | 'http://helloflask.com/' | 

- request对象常用的属性和方法

| 属性/方法 | 说明 | 
| ------------- | ------------- | 
| args | Werkz eug 的ImmutableMultiDict 对象。存储解析后的查询字符串，可通过字典方式获取悦值。如果你想获取未解析的原生查询字符串，可以使用query_s tring属性 | 
| blueprint | 当前蓝本的名称 | 
| cookies | 一个包含所有随请求提交的cookies 的字典 | 
| data | 包含字符串形式的请求数据 | 
| endpoint | 与当前i苛求相匹配的端点值 | 
| files | Werkzeug的MultiDict 对象，包含所有上传文件，可以使用字典的形式获取文件。使用的键为文件input 标签中的name属性值，对应的值为Werkzeug的FileStorage 对象，可以调用save()方法并传入保存路径来保存文件 | 
| form | Werkz e ug 的ImmutableMultiDict 对象。与files 类似，包含解析后的表单数据。表单字段值通过input 标签的name 属性值作为键获取 | 
| values | Werkzeug 的CombinedMultiDict 对象，结合了args 和form 属性的值 | 
| get_data(cache=True, as_text=False,parse_from_data=False | 获取消求中的数据, 默认读取为字节字符串（ bytestring ）， 将as_text 设为True,则返回值将是解码后的unicode 字符串 | 
| get_json(self, force=False,silent=False,cache=True | 作为JSON解析并返回数据，如果MlME 类型不是JSON ，返回None(除非force 设为True ）；解析出错则抛出Werkzeug 提供的BadRequest 异常（ 如果未开silent= False, cache=True) 启调试模式，则返回400错误响应，后面会详细介绍）, 如果silent 设为True 则返回None; cache 设置是否缓存解析后的JSON 数据 | 
| headers | 一个Werkzeug 的EnvironHeaders 对象，包含首部字段， 可以以字典的形式操作 | 
| is_json | 通过MIME 类型判断是否为JSON 数据，返回布尔值 | 
| json |  包含解析后的JSON 数据，内部调用getjso n （），可通过字典的方式获取键值 | 
| method | 请求的HTTP 方法 |
| method | 请求发起的源URL ， 即referer |
| scheme | 请求的U RL 模式（ http 或https ) |
| user_agent | 用户代理（ UserAgent, UA ） ，包含了用户的客户端类型，操作系统类型等信息 |

- 在Flask处理请求

	1. 路由匹配
	
		使用 flask routes命令可以查看当前程序实例中定义的所有路由
		
	2. 设置监听的HTTP方法
	
		在app.route()装饰器使用methods参数传入HTTP方法的可迭代对象
	
	```
		@app.route('', methods=['GET','POST'])
		def hello():
			return  '<h1>Hello</h1>'
	```
	
	3. URL处理
	
	转换器通过特定的规则指定，即"<转换器：变量名>" 。＜int: year＞把year 的值转换为整数，因此我们可以在视图函数中直接对year变量进行数学计算

	Flask内置的URL变量转换器
	
| 转换器 | 说 明 | 
| ------------- | ------------- | 
| string | 不包含斜线的字符串（默认值） |
| int | 整型 |
| float | 浮点数 |
| path | 包含斜线的字符串。static 路由的URL 规则中的filename 变量就使用了这个转换器 |
| any | 匹配一系列给定值中的一个元素 |
| uuid | UUID字符串 |

```
	@app . route (’ goback/ <int :year > ’)
	def go back (year) :
		return '<p>Welcome to %d'</p ＞' %(2021 - year)
		
	@app.route ( '/ colors/<any (blue, white , red) : color>')
	def three colors (color):
	return '＜p>Love is patient and kind. Love is not jealous or boastful or proud or rude.< /p> ’
```

- 请求钩子

	每个钩子可以注册任意多个处理函数，函数名并不是必须和钩子名称相同

| 钩子 | 说 明 | 
| ------------- | ------------- | 
| before_first_request | 注册一个函数，在处理第一个请求前运行 |
| before_request | 注册一个函数，在处理每个请求前运行 |
| after_request | 注册一个函数，如果没有未处理的异常抛出，会在每个请求结束后运行 |
| teardown_requ est | 注册一个函数， 即使有未处理的异常抛出， 会在每个请求结束后运行。如果发生异常，会传入异常对象作为参数到注册的函数中 |
| after thi s_ request | 在视图函数内注册一个函数， 会在这个请求结束后运行 |

- 响应格式

```python
	'''
		相应格式
		1. 纯文本
		2. HTML(默认)
		3. XML
		4. JSON
	'''

	@app.route('/resp/plain')
	def plain():
		response = make_response('<h1>Hello Harry, this is plain text!</h1>')
		response.mimetype = 'text/plain'
		return response

	htmlstr = '''
		<!DOCTYPE html>
		<html>
		<head></head>
		<body>
			<hl >No te</ hl>
			<p>to : Peter</ p>
			<p>from : Jane</p>
			<p>heading : Rem 工n d er</ p >
			<p>body : <strong>Don ' t forget the party 1</strong></p>
		</body>
		</html>
	'''
	@app.route('/resp/html')
	def html():
		response = make_response(htmlstr)
		return response

	xmlstr = '''  
		<?xml version="1.0" encoding="UTF-8"?>
		<note>
			<to>Peter</to>
			<from>Jane</from>
			<heading>Reminder</heading>
			<body>Don’t forget the party </body>
		</note>
	'''
	@app.route('/resp/xml')
	def xml():
		response = make_response(xmlstr)
		response.mimetype = 'application/xml'
		return response

	jsonstr = '''
		{
			"note":{
				"to":"Peter",
				"from":"Jack",
				"heading":"Reminder",
				"body":"Don't forget the party!"
			}
		}
	'''
	@app.route('/resp/json')
	def json1():
		response = make_response(jsonstr)
		response.mimetype = 'application/json'
		return response

	'''
		1. 使用Python标准库中的json模块结合设置mime类型可将Python的字典、数组、元组序列化后返回json数据
		2. 使用Flask框架的jsonify()函数可以直接将Python数据返回json数据，而且不用设置mime类型,参数可以
		   传入普通参数、关键字参数、或者字典、数组、元组
	'''
	data = {'name':'Jack','age':38,'email':'xxx@xxx.com'}
	@app.route('/resp/json2')
	def json2():
		response = make_response(json.dumps(data))
		response.mimetype = 'application/json'
		return response

	@app.route('/resp/json3')
	def json3():
		return jsonify(name='Tom',age=38,email='tom@163.com')

	@app.route('/resp/json4')
	def json4():
		return jsonify([1,2,3,4,5])

```

- 设置Cookie

```python
	'''
		Response类属性方法
		1. headers：一个Werkzeug 的Headers 对象， 表示响应首部，可以像字典一样
		2. status：状态码，文本类型
		3. status_code：状态码，整型
		4. mimetype：MIME 类型（仅包括内容类型部分）
		5. set_cookie()：用来设置一个cookie，参数如下：
			5.1. key：键值
			5.2. value:cookie值
			5.3. max_age:有效时间，单位秒。默认是浏览器关闭即失效
			5.4. expires:具体的过期时间，一个datatime或者unix时间戳
			5.5. path:限定只在给定的路径内可用，默认整个域名
			5.6. domain:设置cookie可用的域名
			5.7. secure:如果设置True，只能通过https访问
			5.8. httponly:如果设置为True，客户端JavaScript获取cookie功能将被禁用        
	'''
	@app.route('/set/cookie/<name>')
	def setcookie(name):
		response = make_response(redirect(url_for('hello')))
		response.set_cookie(key='python_cookie_name', value=name)
		return response
```
- Response类常用属性和方法
| 方法/属性 | 说 明 | 
| ------------- | ------------- | 
| headers | 一个Werkzeug 的Headers 对象， 表示响应首部，可以像字典一样操作 |
| status | 状态码， 文本类型 |
| status code | 状态码， 整型 |
| mimetype | MIME 类型（仅包括内容类型部分） |
| set_cookie() | 用来设置一个cookie |

	set_cookie()方法的参数
	
| 属性 | 说 明 | 
| ------------- | ------------- | 
| key | cookie的键值 |
| value | cookie的值 |
| max_age | cookie 被保存的时间数， 单位为秒； 默认在用户会话结束（ 即关闭浏览器）时过期 |
| expires | 具体的过期时间，一个datetime 对象或UNIX 时间戳 |
| path | 限制cookie 只在给定的路径可用，默认为整个域名 |
| domain | 设置cooki e 可用的域名 |
| secure | 如果设为True ， 只有通过HTTPS 才可以使用 |
| httponly | 如果设为True ，禁止客户端JavaScript 获取cookie |

1. 设置cookie

```python
	from flask impor t Flask, make response
	@app.route ('/ set/<name >')
	def set cookie(name):
		response = make_response(redirect(url_for ( 'hello' )))
		response set_cookie('name'， name )
		return response
```

2. 读取cookie

```python
	from flask import Flask, r equest
	@app.route ('/')
	@app.route ('/hello')
	def hello( ):
		name= request.args.get ('name')
		if name is None :
			name = request . cookies . get ('name', 'Human') ＃从Cookie 中获取name 值
		return '<h1>Hello ， %s</h1> %name
```

- session ：安全的Cookie

	1. 设置秘钥
	
		app.secret_key = 'secret string'
		
## Flask上下文

	Flask 中有两种上下文，程序上下文（ application context ）和请求上下文（ request context ） 。
	
	1. 程序上下文中存储了程序运行所必须的信息
	
	2. 请求上下文里包含了请求的各种信息， 比如请求的URL ，请求的HTTP 方法等。
	
- 上下文全局变量

	Flask 提供了四个上下文全局变量
	
| 属性 | 上下文类别 | 说 明 |
| ------------- | ------------- | ------------- | 
| current_app |  程序上下文| 指向处理请求的当前程序实例 |
| g | 程序上下文 | 替代Python 的全局变量用法，确保仅在当前请求中可用。用于存储全局数据，每次请求都会重设 |
| request | 程序上下文 | 封装客户端发出的请求报文数据 |
| session | 程序上下文 | 用于记住请求之间的数据，通过签名的Cookie 实现 |

- 激活上下文

	在下面这些情况下， Flask 会自动帮我们激活程序上下文：
	
	1. 当我们使用flask run 命令启动程序时。
	
	2. 使用旧的app.run（）方法启动程序时。

	3. 执行使用＠app.cli . command（）装饰器注册的flask 命令时。

	4. 使用flask shell 命令启动Python Shell 时。
	
	当请求进入时， F lask 会自动激活请求上下文，这时我们可以使用request 和session 变量。另外，当请求上下文被激活
时，程序上下文也被自动激活。当请求处理完毕后，请求上下文和程序上下文也会自动销毁。也就是说，在请求处理时这
两者拥有相同的生命周期。

- 上下文钩子

	在前面我们学习了请求生命周期中可以使用的几种钩子， Flask 也为上下文提供了一个teardown_appcontext 钩子，使用它
注册的回调函数会在程序上下文被销毁时调用，而且通常也会在请求上下文被销毁时调用。比如， 你需要在每个请求处理结束后销毁数据库连接：

```python
	@app.teardown_appcontext
	def teardown_db(exception):
		...
		db.close()
```
	使用app.teardown_appcontext 装饰器注册的回调函数需要接收异常对象作为参数， 当请求被正常处理时这个参数值将是None ，这个函数的返回值将被忽略。