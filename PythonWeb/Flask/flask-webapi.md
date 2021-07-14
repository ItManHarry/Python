# Flask Framework Web API

## 使用URL定义资源

	Web API的根URL应该尽量简单明了。根URL模式主要有两种：

- 通过URL前缀指定：http://example.com/api

- 直接把api加到主机名中，作为子域名：http://api.example.com/api

> 在实际应用中，后一种方法更为简洁，也是普遍采用的方式。

	资源是Web API的核心，这里共有两种资源：

1. 单个资源

2. 集合资源

每个资源都使用一个独一无二的URL表示，URL的设计应遵循以下要求

- 尽量保持简短易懂

- 避免暴露服务器端架构

- 使用类似文件系统的层级结构

## 使用HTTP方法描述操作

	既然有资源，我们就需要对资源进行常见的操作，比如创建、读取、更新、删除（ CRUD ） 。
	
> 我们不需要为供资源实现所有的HTTP 方法。如果客户端使用了不受支持的方法，Flask 会自动处理并返回405 (Method Not Allow ）错误响应，表示不允许使用的方法。

	HTTP方法的响应内容
	
| HTTP方法 | 返回的响应 |	
| ---- | ---- |
| GET | 返回主体为目标资源的表现层， 200 (OK ）响应 |
| POST | 返回指向数据新地址的表现层，首部Location 字段为指向资源的URL, 201(Created ）响应 |
| PUT | 包含请求处理状态的表现层，返回200 响应；空数据，返回204 (No Content ）响应 |
| PATCH | 包含请求处理状态的表现层，返回200 响应；空数据，返回204 响应 |
| DELETE | 如果请求被接收，但删除操作还未执行，返回202 (Accepted ）响应；如果删除操作已经执行，返回204 响应；如果删除操作已经执行，且返回包含状态信息的表现层，返回200 响应 |

## 使用JSON交换数据

	JSON 已经取代XML 成为了API 的标准数据格式。大多数在线服务都使用JSON 作为数据格式。
	
## 设置API版本

> 	当打算对API 进行更新时，我们就不得不考虑还有大量的用户使用的客户端依赖于旧版本的API 。如果我们贸然更新，那么这些用户的客户端很可能会无法正常工作。为了解决这个问
题，我们需要保留旧版本的API ，创建一个新版本。

- 为了同时提供多个版本的API ，较为常见的做法是在API 的URL中指定版本：

	1. version 1: http: //api .example.com/v1
	
	2. version 2: http: //api .example.com/v2
	
- 更简洁的方法，直接在子域中指定：

	1. version 1: http: //api .example.com
	
	2. version 2: http: //api2 .example.com
	
## 使用Flask编写Web API

	API 相关的视图属于单独的程序子集，我们需要先创建一个蓝本来存放相关脚本。
	
- 创建API蓝本

	目录结构：
	
```
	-work
		-api
			-v1
				-__init__.py
				-resources.py
				-auth.py
				-errors.py
```	

初始版本的API 蓝本在v1子包的构造文件(__init__.py)中创建，如下所示：

```python
	from flask import Blueprint
	api_v1 = Blueprint('api_v1', __name__)
	from work.api.v1 import resources
```
	
程序包的构造文件中将这个蓝本注册到程序实例上

```python
	from work.api.v1 import api_v1
	
	def create_app():
		...
		register_app_views(app)
		
	def register_app_views(app):
		...
		app.register_blueprint(api_v1, url_prefix="/api/v1")
```

## 设置子域

> 使用Flask 设置子域非常简单。我们可以为程序设置子域，也可以为蓝本设置子域， 甚至可以为某个路由设置子域。
	
	有两种方式可以为蓝本指定子域： 
	
- 一种是在实例化Blueprint 类时使用subdomain 参数指定

- 另一种是在使用register_blueprint()函数注册蓝本时使用subdomain参数指定(一般采用此方式)。

	同时注册两次api_v1蓝本，分别支持通过子域或URL 前缀的形式访问Web API:

```python
	from work.api.v1 import api_v1
	
	def create_app():
		...
		register_app_views(app)
		
	def register_app_views(app):
		...
		app.register_blueprint(api_v1, url_prefix="/api/v1")
		app.register_blueprint(api_v1, url_prefix='/v1', subdomain='api')
```

> 需要注意的是，如果要在本地测试时使用子域，我们还需要修改操作系统的hosts 文件。在Windows 系统中，hosts 文件的
地址为C: \Windows\System32\drivers\etc\hosts （你可能需要根据Windows 系统的安装位置来修改盘符）；在Linux 和macOS 
系统中的地址为/etc/hosts 。

> hosts文件（又被称为域名映射文件）是一个没有扩展名的系统文件，它存储了主机名和相应IP 地址的映射关系。它通常作
为对DNS (Domain Name System ，域名系统）的补充，可以理解成一个本地的域名解析系统。正因为如此，我们可以自己管理映射关系。

	hosts文件添加以下内容：
	
```
	127.0.0.1 todolist.com
	127.0.0.1 api.todolist.com
```

	第一行的todolist.com作为程序的主机名，而第二行的api.todolist.com就是我们为API 蓝本分配的包含子域的主机名。
	
> 如果不知道主机名， Flask 就无法获取子域名称，也无法正确设置cookie 。为此我们需要在config文件中将SERVER NAME的值设为我们
在hosts 文件中设置的主机名和对应的端口号

```python
	'''
    系统配置
	'''
	import os
	#开发数据库
	dev_db = os.getenv('DEVELOP_DB')
	#生产数据库
	pro_db = os.getenv('PRODUCT_DB')
	#系统路径
	basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
	#全局配置
	class GlobalSetting():
		SECRET_KEY = os.getenv('SECRET_KEY', '123456789qwertyuio!@#$')  # 秘钥(session使用)
		BOOTSTRAP_SERVE_LOCAL = True                                    # Bootstrap本地化
		SYS_LOCALES = ['zh_Hans_CN', 'en_US']                           # 国际化区域设置
		BABEL_DEFAULT_LOCALE = SYS_LOCALES[0]                           # 默认语言区域
		SERVER_NAME = 'todolist.com:80'                                 # 主机名+端口号
	#开发配置
	class DevelopSetting(GlobalSetting):
		# 数据库配置
		SQLALCHEMY_TRACK_MODIFICATIONS = False
		SQLALCHEMY_DATABASE_URI = os.getenv('DEVELOP_DATABASE_URL', dev_db)
	#生产配置
	class ProductSetting(GlobalSetting):
		# 数据库配置
		SQLALCHEMY_TRACK_MODIFICATIONS = False
		SQLALCHEMY_DATABASE_URI = os.getenv('PRODUCT_DATABASE_URL', pro_db)
	#映射配置
	config = {
		'dev_config': DevelopSetting,
		'pro_config': ProductSetting
	}
```

> 	在Windows 下，设置包含"点"的主机名可能会导致AttributeError异常，这是因为Windows 下的socket 对象没有inet_pton 属性。如果
你使用Windows 系统，可以使用win_inet_pton 包来解决这个兼容问题，首先使用Pip安装$ pip install win_inet_pton 。然后在程序
中相关调用前导入import win_inet_pton 这个模块（比如在程序包的构造文件中） 。

## 添加CORS支持

	CORS(Cross Origin Resource Sharing:跨域资源共享)
	SOP(Same Origin Policy:同源策略)：出于安全考虑，浏览器会限制从脚本内发起的跨域请求
	
> 在CORS 流行之前， 大多数API 都通过支持JSONP (JSON with Padding）来支持跨域请求。和JSONP 相比， CORS 更加方便灵活，
支持更多的跨域请求方法，并且在2014年成为W3C的推荐标准，逐渐开始替代JSONP 。

	Flask添加跨域访问支持，首先安装flask-cors
	
```
	pip install flask-cors
```

	因为我们只需要对API 蓝本中的路由添加跨域请求支持，所以Flask-CORS 扩展只在蓝本中初始化，传人蓝本对象作为参数：
	
```python
	from flask import Blueprint
	from flask_cors import CORS
	api_v1 = Blueprint('api_v1', __name__)
	CORS(api_v1)
	from work.api.v1 import resources
```

> 默认情况下， Flask-CORS会为蓝本下的所有路由添加跨域请求支持，并且允许来自任意源的跨域请求。


## 设置资源端点

	在设计Web API 的资源端点时，我们首先要考虑的是通过Web API 开放程序的哪些功能。
	
## 创建资源类

> 在Flask 中，资源端点可以使用普通的视图函数来表示，通过为同一个URL 定义不同的方法实现，比如：

```python
	@api_v1.route('/items/<item_id>', methods=['GET'])
	def get_item(item_id):
		pass
	@api_v1.route('/items/<item_id>', methods=['POST'])
	def post_item(item_id):
		pass
```

	对于简单的程序，使用这种方式就足够了。不过，Flask 提供了使用Python 类来组织视图函数的支持，其中
的方法视图（ MethodView 类）可以让Web API 的编写更加方便， 并且让资源的表示更加直观。借助方法视
图，我们可以定义一个继承自MethodView 的资源类，整个类表示一个资源端点。我们使用资源端点支持的
HTTP 方法作为类方法名，它会处理对应类型的请求。比如，当客户端向／items/<int:id>发起一个GET 
请求时， 资源类中的get()方法将会被调用:

```python
	from flask.views import MethodView
	
	class ItemView(MethodView):
		def get(self, item_id):
			pass
			
		def delete(self, item_id):
			pass
```
在使用方法视图时，除了定义资源类，我们还需要使用add_url_rule()方法来注册路由：	

```python
	api_v1.add_url_rule('/items/<item_id>', view_func=ItemView.as_view('item_api'), methods=['GET', 'DELETE'])
```

## 使用OAuth认证

	OAuth ( Open Authorization ，开放授权）是一个2007 年发布的授权标准，它是现代Web API 中应用非常广泛的授权
机制， Google 、Facebook 、Twitter 、腾讯QQ 等各种在绒服务都提供了OAuth 认证支持。

- OAuth2.0认证模式

| 认证模式(Grant Type) | 说明 |
| ---- | ---- |
| Authorization Code | 最常用，也是最完善和安全的认证模式，大多数在线服务器都提供了这种认证类型支持 |
| Implicit | 同Authorization Code 使用场景类似，但简化了认证过程， 安全性也相应降低 |
| Resource Owner Password Credentials | 直接使用用户名和密码登录，适用于可信的程序，比如在线服务自己开发的官方客户端 | 
| Client Credentials | 不以用户为单位，而是通过客户端来认证， 通常用于访问公开信息 |

Resource Owner Password Credentials认证模式代码如下：

```python
	class AuthTokenAPI(MethodView):
		def post(self):
			 grant_type = request.form.get('grant_type')
			 username = request.form.get('username')
			 password = request.form.get('password')
			 if grant_type is None or grant_type.lower() != 'password':
				 return api_abort(400, message='The grant type must be password.')
			 user = User.query.filter_by(name=username).first()
			 if user is None or not user.validate_password(password):
				 return api_abort(400, message='User name or password is not right.')
			 token, expiration = generate_token(user)
			 response = jsonify({
				 'access_token': token,
				 'token_type': 'Bearer',
				 'expires_in': expiration
			 })
			 response.headers['Cache-Control'] = 'no-store'
			 response.headers['Pragma'] = 'no-cache'
			 return response
	api_v1.add_url_rule('/oauth/token', view_func=AuthTokenAPI.as_view('token'), methods=['POST'])
```

客户端提供的信息：
	
| 键(Key) | 值(Value) |
| ---- | ---- |
| grant_type | 必须为password |
| username | 账号(必填值) |
| password | 密码(必填值)|
| scope | 允许的权限范围(可选值) |

客户端示例代码：

```javascript
	$.ajax({
          type:'post',
          url:'/api/v1/oauth/token',
          data:{grant_type:'password',username:'xxx',password:'xxxxxx'},
          contentType:'application/x-www-form-urlencoded;charset=UTF-8',
          success:function(data){
            token = data.access_token
            $.alert({
               type:'green',
               title:'{{_('sys.info')}}',
               content: '令牌 : '+data.access_token ,
               onClose:function(){

               }
            })
          },
          error:function(e){
            $.alert({
               type:'red',
               //icon:'fa fa-info',
               title:'{{_('sys.error')}}',
               content: '{{_('system.common.error')}}, error code : '+e.status,
               onClose:function(){

               }
            })
          }
     })
```

## 验证access令牌

- 用户发送请求，账号密码验证通过后会获得类似如下的JSON响应：
	
```
	{
		"access_token":"eyJhbGciOiJIUzI1NiisimV4cCI6MTUyN] E3MTY1NiwiaWF0IjoxNTI2MTY4MDU2fQ . eyJpZCI6MX0.PJK4Ie07J x SAPNYcKEmfQogBzpiFEn 工cyzABOfmabYU"，
		"expires_in": 3600 ,
		"token_type": "Bearer "
	}
```

- 调用受资源保护的Web API时需要将access_token作为参数传递给API：

```javascript
	var token = 'eyJhbGciOiJIUzI1NiisimV4cCI6MTUyN] E3MTY1NiwiaWF0IjoxNTI2MTY4MDU2fQ . eyJpZCI6MX0.PJK4Ie07J x SAPNYcKEmfQogBzpiFEn 工cyzABOfmabYU'
	$.ajax({
		type:'post',
		url:'/api/v1/user/items/add',
		data:JSON.stringify({title:'add', body:'20210710added'}),
		contentType:'application/json;charset=UTF-8',
		headers:{'Authorization': 'Bearer '+token}, //传递Token给Web API
		success:function(data){
			if(data.code == 1){
				$.alert({
				   type:'green',
				   title:'{{_('sys.info')}}',
				   content: data.message,
				   onClose:function(){

				   }
				})
			}else{
			   $.alert({
				   type:'red',
				   title:'{{_('sys.info')}}',
				   content: data.message,
				   onClose:function(){

				   }
			   })
			}
		},
		error:function(e){
		   $.alert({
			   type:'red',
			   //icon:'fa fa-info',
			   title:'{{_('sys.error')}}',
			   content: '{{_('system.common.error')}}, error code : '+e.status,
			   onClose:function(){

			   }
		   })
		}
	})
```
- 后台资源保护

```python
	#获取Token
	def get_token():
		if 'Authorization' in request.headers:
			try:
				token_type, token = request.headers['Authorization'].split(None, 1)
			except ValueError:
				token_type = token = None
		else:
			token_type = token = None
		return token_type, token
	#登录保护装饰器
	def auth_required(f):
		@wraps(f)
		def decorated(*args, **kwargs):
			token_type, token = get_token() #获取Token
			if request.method != 'OPTIONS':
				if token_type is None or token_type.lower() != 'bearer':
					return api_abort(400, message='The token type must be bearer.')
				if token is None:
					return token_missing()
				if not validate_token(token):
					return invalid_token()
			return f(*args, **kwargs)
		return decorated
```

- Web API增加资源保护

```python
	class ItemView(MethodView):
		decorators = [auth_required]  #所有资源都增加了保护
		def get(self, item_id):
			#获取待办事项
			item = Item.query.get_or_404(item_id)
			if g.current_user != item.author:
				return jsonify(code=0, message='Wrong user!')
			return jsonify(item_schema(item))
		...
```

## 资源序列化

> 在传统Web 程序中，我们使用Jinja2 来把数据渲染到模板中，然后返回渲染后的HTML 数
据；而在Web API 中，我们则需要将数据按照设计好的模式封装为JSON 数据并返回。这个过
程被称为响应的格式化，或是响应封装，也被称为资源的序列化(Serialization)。

- 定义资源模式

	返回某个资漉时，我们要考虑如何设计响应数据的结构，这个结构被称为资源的模式。一
般来说，资源的模式遵循以下几个要点：

1. 响应数据并不需要完全反映数据库字段，仅需要包含必要的基本信息。

2. 包含自身的描述信息（比如kind），指向自身及相关资糠的URL 。

3. 为了便于使用，最好尽量使数据扁平化，以减少层级复杂度。当然，在使用层级结构更合适的情况下，也可以使用层级结构

	示例(待办资源序列化):
	
```python
	def item_schema(item):
		return {
			'id': item.id,
			#'self': url_for('.item', item_id=item.id, _external=True),
			'kind': 'Item',
			'title': item.title,
			'body': item.body,
			'done': item.done,
			'author': {
				'id': item.author.id,
				#'url': url_for('.user', _external=True),
				'name': item.author.name,
				'kind': 'User'
			}
		}
	#对应响应
	def get(self, item_id):
        #获取待办事项
        item = Item.query.get_or_404(item_id)
        if g.current_user != item.author:
            return jsonify(code=0, message='Wrong user!')
        return jsonify(item_schema(item))
```

## 资源的反序列化

> 在Web API 中，我们也需要获取POST 、PUT 、PATCH 等请求中包含的数据，然后验证这些数据的格式是否符合要求，最后存储于数据库中。这个过程被称为资源的反序列化（ Deserialization ）

- 反序列化处理

	在接收POST 方法的资源方法中，我们需要做相反的工作：从请求对象处获取客户端发来的JSON 数据，验证数据格式，并
将其对应的值存储到数据库字段中。在我们的Web API 中，需要接收的数据就是条目的title, body 值，为了避免重复，我们把
接收并验证条目title, body 字段的工作放到get_item_values()函数中完成，代码如下：

```python
	def get_item_values():
		data = request.get_json()
		title = data['title']
		body = data['body']
		if title is None or str(title).strip() == '':
			raise ValidationError('待办事项标题为空或者未传递!')
		if body is None or str(body).strip() == '':
			raise ValidationError('待办事项内容为空或者未传递!')
		return {
			'title': title,
			'body': body
		}
```
	在get_item_values()函数中，我们还需要对数据进行验证。如果title, body 值为None 或是空
白，我们需要返回400 响应。但因为get_item_values()由视图方法调用，我们并不能在这里使
用api_abort()函数，只能通过抛出异常的方式来处理错误。我们在errors.py 脚本中定义了一个
ValidationError 异常类，它继承Python 中的ValueError 类:

```python
	class ValidationError(ValueError):
		pass

	@api_v1.errorhandler(ValidationError)
	def validate_error(e):
		return api_abort(400, e.args[0])
```

- 使用Webargs解析请求

> 因为我们的程序非常简单，创建待办条目时只需要验证title, body 字段。但对于大型程序来说，
反序列化时通常需要处理多个资源， 每个资源又包含多个不同的字段，这时手动验证数据就会
非常繁琐，而且容易出锚，我们需要借助工具来简化工作。Webargs 是一个用于解析HTTP 请求
参数的Python 库，它主要基于Python 序列化/反序列化工具Marshmallow ( https://github.com/
mars hmallow-code/marshmallow／）实现，添加了HTTP 请求解析支持。

- 安装webargs

```
	 pip install -U webargs
```

- 编写资源模式字典脚本(args.py)

```python
	from webargs import fields, validate, ValidationError
	from work.models import User
	def check_user_code(code):
		user = User.query.filter_by(code=code.lower()).first()
		print('User is >>>>>>>>>>>>>>>>>>>>', user)
		if user is not None:
		   raise ValidationError('账号已存在!')
	user_args = {
		'code': fields.Str(required=True, validate=[check_user_code, validate.Length(min=1)]),
		'name': fields.Str(required=True, validate=validate.Length(min=1)),
		'password': fields.Str(validate=validate.Length(min=6))
	}
```

- 使用资源模式脚本

```python
	# 用户注册-传参方式一
	from webargs.flaskparser import parser
	from work.api.v1.args import user_args
	@api_v1.route('/user/register1', methods=['POST'])
	def register1():
		print('Do the user register action now...')
		args = parser.parse(user_args, request)
		user = User(
			id=uuid.uuid4().hex,
			code=args['code'].lower(),
			name=args['name']
		)
		user.set_password(args['password'])
		db.session.add(user)
		db.session.commit()
		return jsonify(code=1, message='用户注册成功!')
	# 传参方式二
	from webargs.flaskparser import use_args
	@api_v1.route('/user/register2', methods=['POST'])
	@use_args(user_args, location="json")
	def register2(args):
		user = User(
			id=uuid.uuid4().hex,
			code=args['code'].lower(),
			name=args['name']
		)
		user.set_password(args['password'])
		db.session.add(user)
		db.session.commit()
		return jsonify(code=1, message='用户注册成功!')
	# 传参方式三
	from webargs.flaskparser import use_kwargs
	@api_v1.route('/user/register3', methods=['POST'])
	@use_kwargs(user_args)
	def register3(code, name, password):
		u = User.query.filter_by(code=code.lower()).first()
		if u is None:
			print('User is not Exist!!!')
		else:
			print('User has been Exist!!!')
			return jsonify(code=0, message='用户代码已存在!')
		user = User(
			id=uuid.uuid4().hex,
			code=code.lower(),
			name=name
		)
		user.set_password(password)
		db.session.add(user)
		db.session.commit()
		return jsonify(code=1, message='用户注册成功!')
```

- 当验证出错时， Webargs 会返回422 响应(Unprocessable Entity ， 表示实体无法处理， 即语义错误)，我们可以注册一个对应的错误处理函数:

```python
	@app.errorhandler(422)
    def unprocessable_entity(e):
        exc = e.exc
        return jsonify({'code':0, 'errors': exc.messages}), 422
```