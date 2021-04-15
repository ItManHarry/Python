# Flask Framework Database

## 使用Flask-SQLAlchemy 管理数据库

- 安装扩展

```python
	pip install flask-sqlalchemy
```

- 连接数据库

	常用的数据库URI 格式
	
> SQLAlchemy indicates the source of an Engine as a URI combined with optional keyword arguments to specify options for the Engine. The form of the URI is:
>	dialect+driver://username:password@host:port/database
> Many of the parts in the string are optional. If no driver is specified the default one is selected (make sure to not include the + in that case).
	
| DBMS | URI |
| ---- | ---- |
| PostgreSQL | postgresql://username:password@host/databasename|
| MySQL | mysql://username:password@host/databasename |
| Oracle | oracle://://username:password@host/databasename |
| SQLite(UNIX) | sqIite :////absol ute/path/to/foo.db |
| SQLite(Windows) | sqlite:///absolutepath\\to\\foo.db 或r'sqIite:///absolute\path\to\foo.db' |
| SQLite(内存型) | sqlite:///或sqlite:///:memory: |

## 定义数据库模型

	用来映射到数据库表的Python 类通常被称为数据库模型（ model ），一个数据库模型类对应数据库中的一个表。
定义模型即使用Python 类定义表模式， 并声明映射关系。所有的模型类都需要继承Flask-SQLAlchemy 提供的db.Model基类

```python
	class Note(db.Model):
		id = db.Column(db.String(40), primary_key=True)
		body = db.Column(db.Text)
```

- SQLAlchemy 常用的字段类型

| 字段 | 说明 |
| ---- | ---- |
| Integer | 整型 |
| String | 字符串，可选参数length可以用来设置最大长度 |
| Text | 较长的Unicode 文本 |
| Date | 日期， 存储Python的datetime.date对象 |
| Time | 时间， 存储Python的datetime.datetime对象 |
| DateTime | 日期和时间， 存储Python的datetime对象 |
| Interval | 时间间隔，存储Python 的datetime.timedelta对象 |
| Float | 浮点数 |
| Boolean | 布尔值 |
| PickleType | 存储Pickle列化的Python对象 |
| LargeBinary | 存储任意二进制数据 |

	字段类型一般直接声明即可，如果需要传人参数，你也可以添加括号。对于类似String 的字符串列，有些数据库会要求限定长度，因此最好为其指定长度。
	
- 常用的SQLAlchemy字段参数

| 参数名 | 说明 |
| ---- | ---- |
| primary_key | 如果设为True ，该字段为主键 |
| unique | 如果设为True ，该字段不允许出现重复值 | 
| index | 如果设为True ，为该字段创建索引，以提高查询效率 |
| nullable | 确定字段值可否为空，值为True 或False ，默认值为True |
| default | 为字段设置默认值 |

- 创建数据库和表

	通过对我们的db对象调用create_all()方法实现：
	
```
	$ flask shell
	>>> from app import db
	>>> db.create_all()
```
	
	我们也可以自己实现一个自定义flask 命令完成这个工作:
	
```python
	import click
	from app import db,app
	@app.cli.command()
	def initdb():
		db.create_all()
		click.echo('Intitialized database finished!!!')
```
	在命令行下输入flask inintdb即可创建数据库和表：
	
```
	$ flask initdb
```
	
## 数据库操作

> SQLAJchemy使用数据库会话来管理数据库操作，这里的数据库会话也称为事务(transaction)。Flask-SQLAJchemy 自动帮我们创建会话，可以通过db.session 属性获取。
> 数据库中的会话代表一个临时存储区，你对数据库做出的改动都会存放在这里。你可以调用add() 方法将新创建的对象添加到数据库会话中，或是对会话中的对象进行更新。只有当你对
> 数据库会话对象调用commit()方法时，改动才被提交到数据库，这确保了数据提交的一致性。另外，数据库会话也支持回滚操作。当你对会话调用rollback()方法时，添加到会话中且未提交
> 的改动都将被撤销。

1. Create
	
	添加一条新记录到数据库主要分为三步：
	A）创建Python 对象（实例化模型类）作为一条记录。
	B）添加新创建的记录到数据库会话。
	C）提交数据库会话。
	下面的示例向数据库中添加三条留言：

```python
	from app import db , Note
	note1 = Note(body= 'remember Sammy Jankis ')
	note2 = Note(body= 'SHAVE'）
	note3 = Note(body= 'DON'T BELIEVE HIS LIES, HE IS THE ONE , KILL HIM ')
	db.session.add(note1)
	db.session.add(note2)
	db.session.add(note3)
	db.session.commit()
```

2. Read
	
> 我们已经知道了如何向数据库里添加记录，那么如何从数据库里取回数据呢？使用模型类提供的query 属性附加调用各种过滤方法及查询方法可以完成这个任务。
> 一般来说，一个完整的查询遵循下面的模式：
	
		<模型类>.query.<过滤方法>.<查询方法>
		
2.1. 常用的SQLAlchemy过滤方法
	
| 查询方法 | 说明 |
| ---- | ---- |	
| filter() | 使用指定的规则过滤记录，返回新产生的查询对象 |
| filter_by() | 使用指定规则过滤记录（ 以关键字表达式的形式），返回新产生的查询对 |
| order_by() | 根据指定条件对记录进行排序，返回新产生的查询对象 |
| limit(limit) | 使用指定的值限制原查询返回的记录数盐，返回新产生的查询对象 |
| group_by() | 根据指定条件对记录进行分组，返回新产生的查询对象 |
| offset( offset) | 使用指定的值偏移原查询的结果，返回新产生的查询对象 |
		
2.2. 常用的SQLAlchemy查询方法
	
| 查询方法 | 说明 |
| ---- | ---- |
| all() | 返回所有的记录 |
| first() | 返回查询的第一笔记录，如果未找到，则返回None |
| one() | 返回第一条记录，且仅允许有一条记录。如果记录数量大于1 或小于l ， 则抛出错误 |
| get(id) | 传入主键值作为参数，返回指定主级n值的记录，如果未找到， 则返回None |
| count() | 返回查询j结果的数量 |
| one_or_none() | 类似one()，如果结果数量不为1，返回None |
| first _ or_ 404() | 返回查询的第一条记录，如果未找到，则返回404 错误响应 |
| get_ or_ 404(id) | 传入主健值作为参数，返回指定主饱值的记录，如果未找到，则返回404 错误响应 |
| paginate() | 返回一个Pag inat i on 对象，可以对记录进行分页处理 |
| with_parent( instance) | 传人模型类实例作为参数， 返回和这个实例相关联的对象 |

2.3. 查询示例
	
```python
	#Equal
	Note.query.filter(Note.body='SHAVE').first()
	Note.query.filter_by(Note.body='SHAVE').all()
	#Like
	LIKE:
	filter(Note.body.like('%foo%'))
	IN:
	filter(Note.body.in_(['foo','bar','baz']))
	NOT IN:
	filter(~Note.body.in_(['foo','bar','baz']))
	AND:
	＃使用and ()
	from sqlalchemy import and_
	filter(and_(Note.body=='foo', Note.title == 'FooBar'))
	＃或在filter()中加入多个表达式，使用逗号分隔
	filter(Note.body=='foo' , Note.title=='FooBar')
	＃或叠加调用多个filter()/filter_by()方法
	filter(Note.body == 'foo').filter(Note.title =='FooBar')
	OR:
	from sqlalchemy import or_
	filter(or_(Note.body=='foo', Note.body=='bar'))
```

3. Update
	
		更新一条记录非常简单，直接赋值给模型类的字段属性就可以改变字段值，然后调用commit()方法提交会话即可
		
```python
	note = Note.query.get(2)
	note.body = 'Change the note'
	db.session.commit()
```

4. Delete
	
		删除记录和添加记录很相似， 不过要把add()方法换成delete()方法，最后都需要调用commit()方法提交修改
		
```python
	note = Note.query.get(2)
	db.session.delete(note)
	db.session.commit()
```