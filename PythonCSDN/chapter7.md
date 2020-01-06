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