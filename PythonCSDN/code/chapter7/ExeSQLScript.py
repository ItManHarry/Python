#connect SQLite3
#1. 打开数据库连接
# SQLite是一个没有后台进程的数据库，磁盘上一个文件就可以对应SQLite数据库
import sqlite3
connection = sqlite3.connect('test.db')
#2. 打开游标
cursor = connection.cursor()
#3. 使用游标的executescript方法执行SQL脚本
with open('add_user.sql','r') as f:
    sql = f.read()
    cursor.executescript(sql)	
#提交事务
connection.commit()
#4. 关闭游标
cursor.close()
#5. 关闭连接
connection.close()