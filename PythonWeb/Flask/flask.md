# Flask Framework

## 搭建开发环境

- 安装pip

- 安装虚拟环境 ：virtualenv

- 创建虚拟环境

- 虚拟环境下安装flask

```
	pip install flask
```

	安装成功后，除了Flask包外，还有其他五个依赖包：
	
	1. Jinja2  ： 模板引擎
	
	2. MarkupSafe ： HTML字符转义工具
	
	3. Werkzeug ： WSGI工具集，处理请求与响应，内置WSGI开发服务器，调试器和重载器
	
	4. click ： 命令行工具
	
	5. itsdangerous ： 提供各种加密签名功能
	
## 创建程序实例

- 创建程序实例

```python
	from flask import Flask	
	app = Flask(__name__)	
```
	Flask表示一个Flask程序，实例化这个类，就得到了我们的程序实例app，传入Flask类构造方法的第一个参数时模块或者包名称，这里我们使用特殊变量"__name__",
Python会根据所处的模块来赋予__name__变量对应的值，同时也会在相应的文件夹里找的需要的资源，如模板和静态资源文件等。

- 注册路由
	
```python
	#使用app.route()装饰器即可完成路由注册
	@app.route('/')
	def index():
		return '<h1>Hello World!!!</h1>'	
	#绑定多个路由
	@app.route('/hi')
	@app.route('/hello')
	def say_hell():
		return '<h1>Hello World!!!</h1>'	
	#动态URL(赋予默认值)
	@app.route('/greet/<name>')
	def greet(name='Programmer'):
		return '<h1>Hello %s!</h1>' %name		
```

- 启动开发服务器

	1. Flask通过依赖包Click内置了一个CLI（Command Line Interface）系统，当我们安装Flask以后，会自动添加一个flask命令脚本，我们可以通过flask内置命令、扩展
	提供的命令或是我们自己定义的命令。启动开发服务器的命令：flask run； 使用flask --help可以查看所有的命令
	
	2. 自动发现程序实例
	
		一般来说，在执行flask run 命令运行程序前，我们需要提供程序实例所在模块的位置。我们在上面可以直接运行程序，是因为Flask 会自动探测程序实例，自动探测存在下面这些规则：
		
		a. 从当前目录寻找app . py 和wsgi.py 模块，并从中寻找名为app 或application 的程序实例。
		
		b. 从环境变量FLASK_APP 对应的值寻找名为app 或application 的程序实例。
		
			b.1. 	Linux 或mac OS 系统使用export 命令：
						$ export FLASK APP=hello
					在Windows 系统中使用se t 命令：
						set FLASK APP=hello
	3. 管理环境变量
	
		F lask 的自动发现程序实例机制还有第三条规则：如果安装了python-dotenv ，那么在使用flask run 或其他命令时会使用它自动从.flaskenv 文件和.env 文件中加载环境变量
		
		注：安装了python-dotenv时，Flask在加载环境变量的优先级是：手动设置的环境变量 > .env中的环境变量 > .flaskenv中的环境变量
		
		3.1. 使用python-dotenv管理项目的环境变量
		
				安装：pip install python-dotenv
				
		3.2. 在项目的跟目录下分别创建两个文件：.env和.flaskenv。.flaskenv用来存储和Flask相关的公开环境变量，比如FLASK_APP,而.env存放包含敏感信息的环境变量，比如邮箱服务器等信息
		环境变量使用键值对的形式定义，每行一个，#打头的为注释：
		
		```
			#邮箱服务器
			EMAIL_SERVER=email.163.com
		```

	4. 更多启动项
	
		4.1. 默认情况下我们启动的Web服务器对外是不可见的，在run命令后将--host选项设置为"0.0.0.0"使其对外可见
		
		```
			flask run --host 0.0.0.0
		```
		
		4.2. 设置访问端口
		
		```
			flask run --host 0.0.0.0 --port 80
		```
		
	5. 设置运行环境
	
		flask运行环境分为开发环境（development environment）和生产环境（production environment）。
		在.flaskenv文件配置FLASK_ENV变量为"development" / "production"进行环境切换
		
	6. 重载器
	
		默认使用Werkzeug内置的stat重载器，为了获得更优秀的体验，我们安装用于监测文件变化的Python库watchdog
		
		```
			pip install watchdog 
		```
		
	7. Flask shell 
	
		输入：flask shell即可进入flask交互解释器（执行前提和run一样，必须保证程序实例可以被正常找到）。
		
	8. 扩展
		
			扩展（ extension ） 即使用Flask 提供的API 接口编写的Python 库，可以为F lask 程序添加各种各样的功能。大部分Flask 扩展用来集成其他库，
		作为F l ask 和其他库之间的薄薄一层胶水。因为F l as k 扩展的编写有一些约定，所以初始化的过程大致相似。大部分扩展都会提供一个扩展类，
		实例化这个类，并传入我们创建的程序实例app作为参数，即可完成初始化过程。通常，扩展会在传入的程序实例上注册一些处理函数， 并加
		载一些配置。
			以某扩展实现了Foo 功能为例，这个扩展的名称将是Flask- Foo 或Foo-Flask ；程序包或模块的命名使用小写加下划线，即flask foo （ 即导人时的名称） ；
			用于初始化的类一般为Foo ，实例化的类实例一般使用小写，即foo 。初始化这个假想中的F lask-Foo 扩展的示例如下所示：		from f las k 工mport Flask
		```
			from flask foo import Foo
			app = Flask(__name__)
			foo = Foo (app)
		```
	9. 项目配置
	
		配置变量都通过Flask 对象的app. co nfig 属性作为统一的接口来设置和获取，它指向的Config 类实际上是字典的子类，所以你可以像操作其他字典一样操作它。
		可以把配置变量存储在单独的Python 脚本、JSON 格式的文件或是Python类中， config 对象提供了相应的方法来导人配置。
		和操作字典一样，读取一个配置就是从confi g 字典里通过将配置变量的名称作为链’读取对应的值：
		```
			value = app.config[ 'ADMIN_NAME ' ]
		```
		
	10. Flask命令
	
		除了Flask 内置的flask run 等命令，我们也可以自定义命令。在虚拟环境安装F lask 后，包含许多内置命令的flask 脚本就可以使用了。在前面我们已经接触了
		很多flask 命令，比如运行服务器的flask run ，启动shell 的flask shell 。
		通过创建任意一个函数，并为其添加app.cli.command（）装饰器，我们就可以注册一个flask命令：
		
		```
			@app. cli. command ()
			def hello () :		
				click .echo('Hello , Human !'）
		```
		函数的名称即为命令名称，这里注册的命令即hello ，你可以使用flask hello 命令来触发函数。作为替代，你也可以在app.cli.command(） 装饰器中传入参数
		来设置命令名称，比如app.cli.command （'say-hello'）会把命令名称设置为say-hello ，完整的命令即flask say-hello.
		借助cl ick 模块的echo(）函数，我们可以在命令行界面输出字符。命令函数的文档字符串则会作为帮助信息显示（ flask hello - -help ）