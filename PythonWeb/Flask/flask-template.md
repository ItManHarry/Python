# Flask Framework Template

## 模板

- 模板示例：
	
```html
	< ! DOCTYPE html>
	<html lang="en">
	<head>
	<meta charset="utf- 8">
	<title>{{ user . username }} 's Watchlist</title>
	</head>
	<body>
		<a href="{{ url_for('index') }}">& larr; Return</a>
		<h2>{{ user.username }}</h2>
		{% if user.bio %｝
			<i>{{ user.bio}}＜/i>
		{% else %｝
			<i>This user has not provided a bio. </i>
		{% endif %}
		{＃下面是电影清单（这是注释） #}
		<h5>{{ user.username }} 's Watchlist ( {{movies|length }} ) : </h5>
		<ul>
			{% for movie in m ovies %｝
				<li>{{ movie.name }} - {{ movie.year }}</li>
			{% endfor %｝
		</ul >
</body>
</html>
```

	在模板中添加Python 语句和表达式时，我们需要使用特定的定界符把它们标示出来。
	
	三种定界符：
	
	1. 语句（比如if判断、for循环）
	
		{% ... %}
		
	2. 表达式（字符串、变量、函数调用等）
	
		{{ ... }}
		
	3. 注释
	
		{# ... #}
		
	另外，在模板中， Jinja2 支持使用“．”获取变量的属性，比如user 字典中的username 键值通过“．”获取，
	即user. username ，在效果上等同于user['name']
	
	Jinja2 允许你在模板中使用大部分Python 对象，比如字符串、列表、字典、元组、整型、浮点型、布尔值。它支持
基本的运算符号（＋、-、\*、／等）、比较符号（ 比如＝＝ 、！＝ 等） 、逻辑符号（ and 、or 、not 和括号）
以及in 、is 、None 和布尔值（ True 、False ） 。
	Jinja2 提供了多种控制结构来控制模板的输出，其中for 和if 是最常用的两种。在Jinja2里，语句使用｛%．．．%｝标识，
尤其需要注意的是，在语句结束的地方，我们必须添加结束标签。

```html
	{% if user.bio %}
		<i>{{user.bio}}</i>
	{% else %}
		<i>This user has not provided a bio.</i>
	{% endif %}	
```

	for循环，Jinja2提供多个特殊变量：
	
| 变量名 | 说 明 | 
| ------------- | ------------- | 
| loop.index | 当前迭代数（从l 开始计数） |
| loop.index() | 当前迭代数（从0 开始计数） |
| loop.revindex | 当前反向迭代数（从l 开始计数） |
| loop.revindex() | 当前反向迭代数（从0 开始计数） |
| loop.first | 如果是第一个元素， 则为True |
| loop.last | 如果是最后一个元素，则为True |
| loop.previtem | 上一个迭代的条目 |
| loop.next1tem | 下一个迭代的条目 |
| loop.length | 序列包含的元素数量 |

- 渲染模板

	在视图函数中渲染模板时，我们并不直接使用Jinja2提供的函数，而是使用Flask 提供的渲染函数render_template（）
	
```python
	from flask import Flask, render_template
	@app.route ( '/ watchlist ')
	def watchlist () :
		return render_template ( 'watchlist.html', user=user , movies=movies)
```

	传人Jinja2 中的变量值可以是字符串、列表和字典，也可以是函数、类和类实例，这完全取决于你在视图函数传入的值。下面是一些示例：
	
```html
	<p>这是列表my_list 的第一个元素： ｛{ my_list[0] }}</p>
	<p＞这是元组my_tuple 的第一个元素：｛{ my_tuple[0]  }}</p>
	<p＞这是字典my_dict 的键为name 的值： {{ my_dict['name'] }}</p>
	<p＞这是函数my_func 的返回值：｛{ my_func() }}</p>
	<p＞这是对象my_object调用某方法的返回值:{{ my_object.name() }}</p>
```

## 上下文

- 传入变量&自定义变量

	模板上下文包含了很多变量，其中包括我们调用render_template（）函数时手动传入的变量
以及Flask 默认传入的变量。	除了渲染时传入变量，你也可以在模板中定义变量，使用set 标签：

```html
	｛% set navigation ＝［('/','Home'),('about','About')］ %｝
```
	
	你也可以将一部分模板数据定义为变量，使用set 和endset 标签声明开始和结束：

```
	｛% set navigation %｝
		<li><a href= "/">Home</a>
		<li><a href="/about">About</a>
	｛% endset %｝
```	

- 内置上下文变量
	
		Flask 在模板上下文中提供了一些内置变量， 可以在模板中直接使用：
		
| 变量 | 说 明 | 
| ------------- | ------------- | 
| config | 当前的配置对象 |
| request | 当前的请求对象，在已激活的请求环境下可用 |
| session | 当前的会话对象，在己激活的请求环境下可用 |
| g | 与请求绑定的全局变革’，在已激活的请求环境下可用 |

- 自定义上下文
	
	如果多个模板都需要使用同一变量，那么比起在多个视图函数中重复传入，更好的方法是能够设置一个模板全局变量。
Flask 提供了一个app.context_processor 装饰器，可以用来注册模板上下文处理函数， 它可以帮我们完成统一传入
变量的工作。模板上下文处理函数需要返回一个包含变量键值对的字典：

```python
	@app.context_processor
	def inject_foo():
		foo = 'I am foo.'
		return dict(foo=foo)
```

## 全局对象

	全局对象是指在所有的模板中都可以直接使用的对象，包括在模板中导人的模板
	
- 内置全局对象

	1. Jinja2 在模板中默认提供了一些全局函数，常用的三个函数如下：
	
| 函数 | 说 明 | 
| ------------- | ------------- | 
| range(\[start, ]stop\[, step]) | 和Python 中的range()用法相同 |
| lipsum(n=5, html=True, min=20, max=100) | 生成随机文本(lorem ipsum)，可以在测试时用来填充页面。默认生成5 段HTML 文本， 每段包含20 ~ 100 个单词 |
| dict(\*\*items) | 和Python中的diet()用法相同 |

	2. Flask也在模板中内置了两个全局函数:

| 函数 | 说明 |
| ---- | ---- |
| url_for() | 用于生成U RL 的函数 |
| get_flashed_messages() | 用于获取flash 消息的函数 |

	3. 自定义全局函数
	
		除了使用app.context_processor 注册模板上下文处理函数来传入函数， 我们也可以使用app.template_global(仅能用于注册全局函数,注册全局变量需要用其他方法)装饰器
直接将函数注册为模板全局函数。以下代码清单把bar()函数注册为模板全局函数。
	
```python
	@app.template_global()
	def bar():
		return 'I am bar'
```

## 过滤器

	在Jinja2 中，过滤器（ filter ）是一些可以用来修改和过滤变量值的特殊函数，过滤器和变量
用一个竖线（管道符号）隔开，需要参数的过滤器可以像函数一样使用括号传递。下面是一个对
name 变量使用title过滤器的例子：

```html
	#这会将name变量的值标题化，相当于在Python里调用name.title()
	{{ name|title}}
	{{ movies|length}}		#相当于Python里调用len(movies)
```

	另一种用法是将过滤器作用于一部分模板数据，使用filter 标签和endfilter标签声明开始和结束。
比如，下面使用upper过滤器将一段文字转换为大写：

```html
	{% filter upper %}
		This text will becomes uppercase.
	{% endfilter%}
```

- 内置过滤器

Jinja2提供了许多内置过滤器，常用的过滤器如下表所示：

| 过滤器| 说明 |
| ---- | ---- |
| default(value, default_value='u',boolean=False) | 设置默认值，默认值做为参数传入，别名为d |
| escape(s) | 转义HTML 文本，别名为e |
| first (seq) | 返回序列的第一个元素 |
| last( seq) | 返回序列的最后一个元素 |
| Iength(object) | 返回变量的长度 |
| random( seq) | 返回序列中的随机元素 |
| safe( value) | 将变量值标记为安全，避免转义 |
| trim( value) | 清除变量值前后的空格 |
| max(value, case_ sensitive=False, attribute=None) | 返回序列中的最大值 |
| min(value, case sensitive=False, a忧ribute=None) | 返回序列中的最小值 |
| unique(value, case sensitive=False, attribute=None) | 返回序列中的不重复的值 |
| stri ptags(value) | 清除变量值内的HTML 标签 |
| urlize (value, trim_url_limit=None, nofollow=Flase,target=None,rel=None | 将URL 文本转换为可单击的HTML 链接 |
| wordcount (s) | 计算单词数量 |
| tojson(value, indent=None) | 将变量值转换为JSON 格式 |
| truncate(s, length=25 5, killwords=False,end='...',leeway=None | 截断字符串，常用于显示文章摘要， length 参数设置截断的长度，killwords参数设置是否截断单词，end参数设置结尾符号 |

- 自定义过滤器

	如果内置的过滤器不能满足你的需要，还可以添加自定义过滤器。使用app.template_filter()装饰器可以注册自定义过滤器
	
```python
	from flask import Markup
	@app.template_filter()
	def musical(s):
		return s + Markup('&#9835;')
```

## 测试器

	在Jinja2 中， 测试器（ Test ）是一些用来测试变量或表达式，返回布尔值（ True 或Fa l se ）的特殊函数。比如， number 测试器
	用来判断一个变量或表达式是否是数字，我们使用is连接变量和测试器：
	
```html
	{% if age is number %}
		{{ age * 365 }}
	{% else %}
		<h2>无效数字</h2>
	{% endif %}
```

- 内置测试器

| 测试器 | 说明 |
| ---- | ---- |
|callable(object) | 判断对象是否可被调用|
|defined(value)| 判断变量是否已定义|
|undefined(value)| 判断变量是否未定义|
|none(value) |判断变量是否为None|
|number(value) |判断变量是否是数字|
|string(value) |判断变量是否是字符串|
|sequence(value) |判断变量是否是序列， 比如字符串、列表、元组|
|iterable(value)| 判断变量是否可迭代|
|mapping(value) |判断变量是否是匹配对象，比如字典|
|sameas(value , other) |判断变量与other 是否指向相同的内存地址|

- 自定义测试器

	和过滤器类似，我们可以使用Flask提供的app. emplate_test()装饰器来注册一个自定义测试器：
	
```python
	@app.template_test()
	def baz(n):
		if n == 'baz':
			return True
		return False
```

## 模板环境对象

	在Jinja2 中，渲染行为由jinja2.Enviroment 类控制，所有的配置选项、上下文变量、全局函数、过滤器和
测试器都存储在Enviroment 实例上。当与Flask 结合后，我们并不单独创建Enviroment对象，而是使用Flask 
创建的Enviroment 对象,它存储在app.jinja_env 属性上。在程序中,我们可以使用app.jinja_env 更改Jinja2设置.

- 添加自定义全局函数/变量

	和app.template_global()装饰器不同，直接操作globals 字典允许我们传入任意Python 对象， 而不仅仅是函数，
类似于上下文处理函数的作用。下面的代码使用app.jinjia_env.globals 分别向模板中添加全局函数bar 和全局变量foo:

```python
	def bar():
		return 'I am bar'
	foo = 'I am foo'
	app.jinja_env.globals['bar'] = bar
	app.jinja_env.globals['foo'] = foo
```

- 添加自定义过滤器

```python
	def smiling(s):
		return s + ':)'
	app.jinja_env.filters['smiling'] = smiling
```

- 添加自定义测试器

```python
	def baz(n):
		if n == 'AAA':
			return True
		return False
		
	app.jinja_env.tests['baz'] = baz
```