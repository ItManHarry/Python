# 数据库编程

## 数据库API与全局变量及核心类基本流程

- 数据库API

	Python需要操作不同数据库使用不同的模块，但是这些模块都需要遵守Python制定的DB API协议，目前最新版本为2.0 ： Python DB API 2.0

- 全局变量

	全局变量用于判断该数据库模块所支持的功能，通常有一下3个全局变量：
	
	1. apilevel：该全局变量显示数据库模块的API版本号
	
	2. threadsafety：该全局变量指定该数据库模块的线程安全等级
	
	3. paramstyle：该全局变量指定当SQL语句需要参数时，可以使用哪种风格的参数（qmark，numeric、named等）

- 核心API

	1. connect()函数：连接数据库，返回数据库连接
	
	2. 数据库连接：用于打开游标，开启或提交事务
	
	3. 游标：用于执行SQL语句，获取执行结果

- 操作数据库流程

	打开数据库连接：connection -> 获取游标：cursor -> 执行SQL（获取/处理数据）-> 关闭游标：cursor -> 关闭连接：connection -> 结束
	
## 动态创建数据表

- 导入sqlite3模块

- 执行DDL创建数据表

```python
	#connect SQLite3
	#1. 打开数据库连接
	# SQLite是一个没有后台进程的数据库，磁盘上一个文件就可以对应SQLite数据库
	import sqlite3
	connection = sqlite3.connect('test.db')
	#2. 打开游标
	cursor = connection.cursor()
	#3. 使用游标的execute方法执行任意的SQL语句（DDL）
	cursor.execute('''
		create table user_tb(
			id integer primary key autoincrement,
			name text,
			passed text,
			age integer
		)
	''')
	#4. 关闭游标
	cursor.close()
	#5. 关闭连接
	connection.close()
```

- SQLite数据库特性

	1. SQLite内部只支持NULL,INTEGER,REAL(浮点数),TEXT(文本),BLOB(大二进制文本)这5种数据类型
	
	2. SQLite允许存入数据时忽略底层数据列实际的数据类型，因此在编写建表语句时可以忽略数据列后面的类型声明
	
	
- 执行DML语句

	1. 单条操作

```python
	#connect SQLite3
	#1. 打开数据库连接
	# SQLite是一个没有后台进程的数据库，磁盘上一个文件就可以对应SQLite数据库
	import sqlite3
	connection = sqlite3.connect('test.db')
	#2. 打开游标
	cursor = connection.cursor()
	#3. 使用游标的execute方法执行任意的SQL语句（DDL）
	cursor.execute('''
		update user_tb set passed = '123456'
	''')
	print('data affected : ', cursor.rowcount)
	#提交事务
	connection.commit()
	#4. 关闭游标
	cursor.close()
	#5. 关闭连接
	connection.close()
	
	#connect SQLite3
	#1. 打开数据库连接
	# SQLite是一个没有后台进程的数据库，磁盘上一个文件就可以对应SQLite数据库
	import sqlite3
	connection = sqlite3.connect('test.db')
	#2. 打开游标
	cursor = connection.cursor()
	#3. 使用游标的execute方法执行任意的SQL语句（DDL）
	cursor.execute('''
		update user_tb set passed = '123456'
	''')
	print('data affected : ', cursor.rowcount)
	#提交事务
	connection.commit()
	#4. 关闭游标
	cursor.close()
	#5. 关闭连接
	connection.close()
```
	2. 多条操作
	
```python
	#connect SQLite3
	#1. 打开数据库连接
	# SQLite是一个没有后台进程的数据库，磁盘上一个文件就可以对应SQLite数据库
	import sqlite3
	connection = sqlite3.connect('test.db')
	#2. 打开游标
	cursor = connection.cursor()
	#3. 使用游标的execute方法执行任意的SQL语句（DDL）
	cursor.executemany('''
		insert into user_tb(name,passed,age)
		values(?,?,?)
	''', (
		('Harry1','12345678',36),
		('Harry2','12345678',37),
		('Harry3','12345678',38),
		('Harry4','12345678',39),
		('Harry5','12345678',40)
	))
	#提交事务
	connection.commit()
	#4. 关闭游标
	cursor.close()
	#5. 关闭连接
	connection.close()
```

- 执行查询

 1. 执行语句变为select，由于select语句执行完后可以得到查询结果，可以通过游标的fetchone()/fetchmany()/fetchall()来获取查询结果
 
 2. 也可直接将游标当成可迭代对象来获取查询结果
 
 3. 使用execute()方法执行完select语句之后，程序可通过游标的description属性（返回值为游标）获取查询的列信息，也可以通过游标来获取查询结果
 
 ```python
	#执行查询 - 获取列信息
	#connect SQLite3
	#1. 打开数据库连接
	# SQLite是一个没有后台进程的数据库，磁盘上一个文件就可以对应SQLite数据库
	import sqlite3
	connection = sqlite3.connect('test.db')
	#2. 打开游标
	cursor = connection.cursor()
	#3. 使用游标的execute方法执行任意的SQL查询语句
	cursor.execute('''
		select * from user_tb
		where age > ?
	''', (36,))
	#获取列信息
	for columns in cursor.description:
		print(columns[0])
	#4. 关闭游标
	cursor.close()
	#5. 关闭连接
	connection.close()
	
	#执行查询
	#connect SQLite3
	#1. 打开数据库连接
	# SQLite是一个没有后台进程的数据库，磁盘上一个文件就可以对应SQLite数据库
	import sqlite3
	connection = sqlite3.connect('test.db')
	#2. 打开游标
	cursor = connection.cursor()
	#3. 使用游标的execute方法执行任意的SQL查询语句
	cursor.execute('''
		select * from user_tb
		where age > ?
	''', (36,))
	#获取列信息
	for columns in cursor.description:
		print(columns[0], end="\t")
	print('-' * 80)
	while True:
		row = cursor.fetchone()
		if not row:
			break
		else:
			for data in row:
				print(data, end='\n')
	#4. 关闭游标
	cursor.close()
	#5. 关闭连接
	connection.close()
	
	#执行查询
	#connect SQLite3
	#1. 打开数据库连接
	# SQLite是一个没有后台进程的数据库，磁盘上一个文件就可以对应SQLite数据库
	import sqlite3
	connection = sqlite3.connect('test.db')
	#2. 打开游标
	cursor = connection.cursor()
	#3. 使用游标的execute方法执行任意的SQL查询语句
	cursor.execute('''
		select * from user_tb
		where age > ?
	''', (36,))
	#使用游标输出
	for row in cursor:
		for data in row:
			print(data, end='\t')
		print()
	#4. 关闭游标
	cursor.close()
	#5. 关闭连接
	connection.close()	
 ```
 
 - 使用事务控制数据库操作
 
	1. 事务
	
		事务是由一步或者几步数据操作序列组成的逻辑执行单元，事务的特性：原子性（Atomicity）、一致性（Consistency）、隔离性（Isolation）、持续性（Durability）
 
	2. 提交事务	
	
```python
	#事务 - 提交
	#connect SQLite3
	#1. 打开数据库连接
	# SQLite是一个没有后台进程的数据库，磁盘上一个文件就可以对应SQLite数据库
	import sqlite3
	connection = sqlite3.connect('test.db')
	#2. 打开游标
	cursor = connection.cursor()
	#3. 使用游标的execute方法执行任意的SQL查询语句
	#如果游标执行是DDL语句，程序不需要显示提交事务，程序会自动提交事务
	#执行DML语句 - 事务默认开启，该游标后面所执行的DDL语句也不会自动生效，必须手动执行事务提交
	cursor.execute('''
		insert into user_tb(name,passed,age)
		values(?,?,?)
	''', ('Sam','12345678',25))
	cursor.execute('create table tb_emp(id integer primary key autoincrement, name text)')
	#提交事务
	connection.commit()
	#4. 关闭游标
	cursor.close()
	#5. 关闭连接
	connection.close()	
```
	
	3. 回滚事务
	
		回滚方式分为显示回滚和自动回滚
		
```python
	#事务 - 回滚
	#connect SQLite3
	#1. 打开数据库连接
	# SQLite是一个没有后台进程的数据库，磁盘上一个文件就可以对应SQLite数据库
	import sqlite3
	connection = sqlite3.connect('test.db')
	#2. 打开游标
	cursor = connection.cursor()
	#3. 使用游标的execute方法执行任意的SQL查询语句
	#如果游标执行是DDL语句，程序不需要显示提交事务，程序会自动提交事务
	#执行DML语句 - 事务默认开启，该游标后面所执行的DDL语句也不会自动生效，必须手动执行事务提交
	cursor.execute('''
		insert into user_tb(name,passed,age)
		values(?,?,?)
	''', ('Sam2','12345678',22))
	cursor.execute('create table tb_emp2(id integer primary key autoincrement, name text)')
	#回滚事务
	connection.rollback()
	#4. 关闭游标
	cursor.close()
	#5. 关闭连接
	connection.close()
```