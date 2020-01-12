#connect SQLite3
#1. 打开数据库连接
# SQLite是一个没有后台进程的数据库，磁盘上一个文件就可以对应SQLite数据库
import sqlite3
connection = sqlite3.connect('test.db')
#2. 使用数据库连接对象的executescript方法执行SQL脚本
with open('add_user.sql','r',1,'utf-8') as f:
    sql = f.read()
    connection.executescript(sql)	
#3. 提交事务
connection.commit()
#4. 关闭连接
connection.close()