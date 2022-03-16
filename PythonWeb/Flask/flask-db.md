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

> 用来映射到数据库表的Python 类通常被称为数据库模型（ model ），一个数据库模型类对应数据库中的一个表。
> 定义模型即使用Python 类定义表模式， 并声明映射关系。所有的模型类都需要继承Flask-SQLAlchemy 提供的db.Model基类

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

> 字段类型一般直接声明即可，如果需要传人参数，你也可以添加括号。对于类似String 的字符串列，有些数据库会要求限定长度，因此最好为其指定长度。
	
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
| limit(limit) | 使用指定的值限制原查询返回的记录数量，返回新产生的查询对象 |
| group_by() | 根据指定条件对记录进行分组，返回新产生的查询对象 |
| offset( offset) | 使用指定的值偏移原查询的结果，返回新产生的查询对象 |
		
2.2. 常用的SQLAlchemy查询方法
	
| 查询方法 | 说明 |
| ---- | ---- |
| all() | 返回所有的记录 |
| first() | 返回查询的第一笔记录，如果未找到，则返回None |
| one() | 返回第一条记录，且仅允许有一条记录。如果记录数量大于1 或小于l ， 则抛出错误 |
| get(id) | 传入主键值作为参数，返回指定主键n值的记录，如果未找到， 则返回None |
| count() | 返回查询j结果的数量 |
| one_or_none() | 类似one()，如果结果数量不为1，返回None |
| first _ or_ 404() | 返回查询的第一条记录，如果未找到，则返回404 错误响应 |
| get_ or_ 404(id) | 传入主健值作为参数，返回指定主饱值的记录，如果未找到，则返回404 错误响应 |
| paginate() | 返回一个Pagination 对象，可以对记录进行分页处理(见下表) |
| with_parent( instance) | 传人模型类实例作为参数， 返回和这个实例相关联的对象 |

Pagination类属性

| 属性/方法 | 说 明 |
| ---- | ---- |
| items | 当前页丽的记录 |
| page | 当前页数|
| per_page | 每页的记录数数量 |
| pages | 总页数 |
| total | 总记录数 |
| next_num | 下一页的页数 |
| prev_num| 上一页的页数 |
| has_next | 有下一页返回True |
| has_prev | 有上一页返回True |
| query | 分页的源查询 |

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

## 定义关系

>	在关系型数据库中，我们可以通过关系让不同表之间的字段建立联系。一般来说，定义关系需要两步，分别是创建外键和定义
>关系属性。在更复杂的多对多关系中，我们还需要定义关联表来管理关系。

- 一对多

	以作者和文章为例，一个作者对应多篇文章，数据原始模型如下：
	
```python
	class Author(db.Model):
		id = db.Column(db.Integer, primary_key=True)
		name = db.Column(db.String(30), unique=True)
		phone = db.Column(db.String(20))		
		
	class Article(db.Model):
		id = db.Column(db.Integer, primary_key=True)
		title = db.Column(db.String(50), unique=True)
		body = db.Column(db.Text)
```
1. 定义外键

> 定义关系的第一步是创建外键。外键是(foreign key)用来在A 表存储B表的主键值以便和B表建立联系的关系字段。	

```python
	class Article(db.Model):
		id = db.Column(db.Integer, primary_key=True)
		title = db.Column(db.String(50), unique=True)
		body = db.Column(db.Text)
		#定义外键
		'''
			因为外键只能存储单一数据（标量）所以外键总是在“多”这一侧定义，多篇文章属于同一个作
			者，所以我们需要为每篇文章添加外键存储作者的主键值以指向对应的作者。在Article模型中，
			我们定义一个author_id 字段作为外键。
			这个字段使用db.ForeignKey 类定义为外键，传入关系另一侧的表名和主键字段名，即author.id
		'''
		author_id = db.Column(db.Integer, db.ForeignKey('author.id))
```

2. 定义关系属性

> 定义关系的第二步是使用关系函数定义关系属性。	

```python
	class Author(db.Model):
		id = db.Column(db.Integer, primary_key=True)
		name = db.Column(db.String(30), unique=True)
		phone = db.Column(db.String(20))	
		#定义关系属性
		'''
			关系属性在关系的出发侧定义，即一对多关系的“ 一”这一侧。一个作者拥有多篇文章，
			在Author 模型中，我们定义了一个articles属性来表示对应的多篇文章。
			注：relationship()函数的第一个参数为关系另一侧的模型名称
		'''
		articles= db.relationship('Article')
```

3. 建立关系

	方式一：为外键字段赋值
	
```python
	...
	apam.author_id = 1
	db.session.commit()
```

	方式二：操作关系属性
	
```python
	...
	foo.articles.append(spam)
	foo.articles.append(ham)
	db.session.commit()
```

注：一般采用第二种方式来建立管理

和append()相对，对关系属性调用remove()方法可以与对应的Aritcle对象解除关系：

```python
	...
	foo.articles.remove(spam)	
	db.session.commit()
```

	常用的SQLAlchemy 关系函数参数
	
| 参数名 | 说明 |
| ---- | ---- |
| back_populates | 定义反向引用，用于建立双向关系， 在关系的另一侧也必须显式定义关系属性 |
| backref | 添加反向引用，自动在另一侧建立关系属性，是back_populates 的简化版 |
| lazy | 指定如何加载相关记录，具体选项见下表 |
| uselist | 指定是否使用列表的形式加载记录，设为False则使用标量(scalar) |
| cascade | 设置级联操作 |
| order_by | 指定加载相关记录时的排序方式 |
| secondary | 在多对多关系中指定关联表 |
| primaryjoin | 指定多对多关系中的一级联结条件 |
| secondaryjo in | 指定多对多关系中的二级联结条件 |

	常用的SQLAlchemy 关系记录加载方式（ lazy 参数可选值）
	
| 关系加载方式 | 说明 |
| ---- | ---- |
| select | 在必要时一次性加载记录，返回包含记录的列表（默认值）， 等同于lazy=True |
| joined | 和父查询一样加载记录，但使用联结，等同于lazy=False | 
| immediate | 一旦父查询加载就加载 |
| subquery | 类似于join时，不过将使用子查询 |
| dynamic | 不直接加载记录，而是返回一个包含相关记录的query对象，以便再继续附加查询函数对结果进行过滤 |

4. 建立双向关系

> 我们在Author 类中定义了集合关系属性articles ，用来获取某个作者拥有的多篇文章记录。在某些情况下，你
也许希望能在Arti cle 类中定义一个类似的author 关系属性，当被调用时返回对应的作者记录，这类返回单个值
的关系属性被称为标量关系属性。而这种两侧都添加关系属性获取对方记录的关系我们称之为双向关系(bidirectional relationship)

	双向关系并不是必须的，但在某些情况下会非常方便。双向关系的建立很简单，通过在关系的另一侧也创建一个
relationship()函数，我们就可以在两个表之间建立双向关系。我们使用作家(Writer)和书(Book)的一对多关系来进行演示，
建立双向关系后的Writer 和Book 类如代码清单:

```python
	#back _populates 参数的值需要设为关系另一侧的关系属性名

	class Writer(db.Model):
		id = db.Column(db.String(40), primary_key=True)
		name = db.Column(db.String(50), unique=True)
		books = db.relationship('Book', back_populates='writer')
		
	class Book(db.Model):
		id = db.Column(db.String(40), primary_key=True)
		title = db.Column(db.String(20))
		writer_id = db.Column(db.String(40), db.ForeignKey('writer.id'))
		writer = db.relationship('Writer', back_populates='books')
```

	设置双向关系后，除了通过集合属性books 来操作关系，我们也可以使用标量属性writer来进行关系操作。比如，
将一个Writer 对象赋值给某个Book 对象的w riter 属性，就会和这个Book 对象建立关系。

	相对的，将某个Book 的writer属性设为None时， 就会解除与对应Writer对象的关系
	
> 需要注意的是，我们只需要在关系的一侧操作关系。当为Book 对象的writer 属性赋值后，对应Writer 对象的books 
属性的返回值也会自动包含这个Book 对象。反之，当某个Writer 对象被删除时，对应的Book 对象的writer 属性被调
用时的返回值也会被置为空(即NULL,会返回None)

- 一对一

> 一对一关系实际上是通过建立双向关系的一对多关系的基础上转化而来。我们要确保关系两侧的关系属性都是标量属
性，都只返回单个值，所以要在定义集合属性的关系函数中将**uselist参数设为False** ，这时一对多关系将被转换为一对
一关系。代码清单基于建立双向关系的一对多关系实现了一对一关系:

```python
	class Country(db.Model):
		id = db.Column(db.String(40), primary_key=True)
		name = db.Column(db.String(50), unique=True)
		capital = db.relationship('Capital', uselist=False)
		
	class Capital(db.Model):
		id = db.Column(db.String(40), primary_key=True)
		name = db.Column(db.String(50) unique=True)
		country_id = db.Column(db.String(40), db.ForeignKey('country.id'))
		country = db.relationship('Country')
```

- 多对多

>	在一对多关系中，我们可以在“多”这一侧添加外键指向“一”这一侧，外键只能存储一个记录，但是在多对多关系中，
每一个记录都可以与关系另一侧的多个记录建立关系，关系两侧的模型都需要存储一组外键。在SQLAlchemy 中， 要想
表示多对多关系， 除了关系两侧的图模型外，我们还需要创建一个关联表(associationtable)。关联表不存储数据，只用
来存储关系两侧模型的外键对应关系，如代码清单如下所示：

```python
	
	association_table = db.Table('association', 
		db.Column('student_id', db.String(40), db.ForeignKey('student.id')),
		db.Column('teacher_id', db.String(40), db.ForeignKey('teacher.id'))
	)
	
	class Student(db.Model):
		id = db.Column(db.String(40), primary_key=True)
		name = db.Column(db.String(50), unique=True)
		grade = db.Column(db.String(10))
		clazz = db.Column(db.String(10))
		teachers = db.relationship('Teacher', secondary=association_table, back_populates='students')
		
	class Teacher(db.Model):
		id = db.Column(db.String(40), primary_key=True)
		name = db.Column(db.String(50), unique=True)
		subject = db.Column(db.String(10))
		students = db.relationship('Student', secondary=association_table, back_populates='teachers')
```

## Data Migration

- 安装Flask-Migrate及其依赖

```
	pip install flask-migrate
```

- 实例化

```
	migrate = Migrate()
	migrate.init_app(app, db) #传入app和db两个参数
```

- 创建迁移环境(只做一次即可)

```
	'''
	Flask-Migrate 提供了一个命令集，使用db 作为命名集名称，它提供的命令都以flask db开头
	'''
	flask db init
```
命令执行完成后会在项目根目录下创建一个migrations 文件夹，其中包含了自动生成的配置文件和迁移版本文件夹。

- 生成迁移脚本

使用migrate 子命令可以自动生成迁移脚本：

```
	flask db migrate -m "add note timestamp”
```
这条命令可以简单理解为在flask 里对数据库（ db ）进行迁移（ migrate ） 。－m 选项用来添加迁移备注信息。

- 更新数据库

生成了迁移脚本后，使用upgrade 子命令即可更新数据库：

```
	flask db upgrade
```
如果还没有创建数据库和表，这个命令会自动创建；如果已经创建， 则会在不损坏数据的前提下执行更新。
Tip：如果你想回滚迁移， 那么可以使用downgrade（降级），它会撤销最后一次迁移数据库中的改动，这在开发时非常有用。
比如，当你执行upgrade 命令后发现某些地方出错了，这时就可以执行flask db downgrade 命令进行回滚，删除对应的迁移脚本，重新
生成迁移脚本后再进行更新（ upgrade ） 。
