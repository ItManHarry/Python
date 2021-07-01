# Flask Framework Web API

## 使用URL定义资源

> Web API的根URL应该尽量简单明了。根URL模式主要有两种：

- 通过URL前缀指定：http://example.com/api

- 直接把api加到主机名中，作为子域名：http://api.example.com/api

> 在实际应用中，后一种方法更为简洁，也是普遍采用的方式。

> 资源是Web API的核心，这里共有两种资源：

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
| POST | 返回指向数据新地址的表现层，首部Lo cation 字段为指向资源的URL, 20 I (Crea ted ）响应 |
| PUT | 包含请求处理状态的表现层，返回200 响应；空数据，返回204 (No Content ）响应 |
| PATCH | 包含请求处理状态的表现层，返回200 响应；空数据，返回204 响应 |
| DELETE | 如果请求被接收，但删除操作还未执行，返回202 (Accepted ）响应；如果删除操作已经执行，返回204 响应；如果删除操作已经执行，且返回包含状态信息的表现层，返回200 响应 |

## 使用JSON交换数据

	JSON 已经取代XML 成为了API 的标准数据格式。大多数在线服务都使用JSON 作为数据格式。
	
## 设置API版本

> 	当打算对API 进行更新时，我们就不得不考虑还有大量的用户使用的客户端依赖于旧版本的API 。如果我们贸然更新，那么这些用户的客户端很可能会无法正常工作。为了解决这个问
题，我们需要保留旧版本的API ，创建一个新版本。

- 为了同时提供多个版本的API ，较为常见的做法是在API 的URL 中指定版本：

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