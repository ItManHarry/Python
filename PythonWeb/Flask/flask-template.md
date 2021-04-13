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
	<p ＞这是列表my_list 的第一个元素： ｛{ my_list[0] }}</p>
	<p ＞这是元组my_tuple 的第一个元素：｛{ my_tuple[0]  }}</p>
	<p ＞这是字典my_dict 的键为name 的值： {{ my_dict['name'] }}</p>
	<p ＞这是函数my_func 的返回值：｛{ my_func() }}</p>
	<p ＞这是对象my_object调用某方法的返回值:{{ my_object.name() }}</p>
```

## 上下文

- 传入变量&自定义变量

	模板上下文包含了很多变量，其中包括我们调用render_template（）函数时手动传入的变量
以及Flask 默认传入的变量。	除了渲染时传入变量，你也可以在模板中定义变量，使用set 标签：

```html
	｛	% set navigation ＝［('／'，'Home'),('about','About')］ %｝
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
	
	如果多个模板都需要使用同一变量，那么比起在多个视图函数中重复传人，更好的方法是能够设置一个模板全局变量。
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

	Jinja2 在模板中默认提供了一些全局函数，常用的三个函数如下：
	
| 变量 | 说 明 | 
| ------------- | ------------- | 
| range(\[start, ]stop\[, step]) | 和Python 中的range()用法相同 |
| lipsum(n=5, html=True, min=20, max=100) | 生成随机文本(lorem ipsum)，可以在测试时用来填充页面。默认生成5 段HTML 文本， 每段包含20 ~ 100 个单词 |
| dict(\*\*items) | 和Python中的diet()用法相同 |



| AAA | BBB |
| ---- | ---- |
| 1 | 2 |
| 1 | 2 |
| 1 | 2 |
| 1 | 2 |