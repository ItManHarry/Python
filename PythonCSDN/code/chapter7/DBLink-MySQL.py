#连接操作MySQL数据库
import pymysql
print('-' * 80)
#获取数据库连接
conn = pymysql.connect(host='localhost',port=3306,user='root',passwd='root2019',db='sdb',charset='utf8')
print('database connect successfully...')
#获取游标
cursor = conn.cursor()
print('get cursor successfully...')
#查询数据
sql = '''
    select 
        *
    from tb_company
    where name like '%s'
    and delflag= %d
'''
cursor.execute(sql %('%北京%',0))
print('record size : ', cursor.rowcount)
for row in cursor.fetchall():
    print(row)
print('-' * 80)
#关闭游标
cursor.close()
#关闭连接
conn.close()