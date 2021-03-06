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