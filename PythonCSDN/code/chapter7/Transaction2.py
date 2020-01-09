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