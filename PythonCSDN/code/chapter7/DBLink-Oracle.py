#连接Oracle数据库
import cx_Oracle as cxo
conn = cxo.connect('mi/mi@10.40.128.171:1521/orcl')
cursor = conn.cursor()
cursor.execute('''
	select 
		* 
	from mi_dealer
''')
print('Record size is : \t', cursor.rowcount)
data = cursor.fetchall()