# Pandas

## Pandas的价值

- 事实上的Python数据分析底层标准架构

- 为后续的数据分析与挖掘提供了大一统的数据基础框架

- 为Python和数据、R等外部工具进行互通提供了简单易用的接口

- 使用Pandas还可以：
	
	1. 清洗数据，整理数据
	
	2. 用统计图和统计表探索数据特征
	
	3. 为后续分析做好数据准备（数据变换、格式转换）
	
	4. 初步数据分析（更专业的要交给scikit-learn、statsmodels等）
	
## 数据读取

- 读取csv文件

```python
	passengers = pd.read_csv('D:\\Github\\Python\\PythonData\\code\\data\\titanic.csv',encoding='utf-8')
	print(passengers)
```

- 读取Excel文件

```python
	customers = pd.read_excel('D:\\Github\\Python\\PythonData\\code\\data\\customers.xls',sheet_name='All')
	print(customers)
```

- 读取统计软件的数据文件(SAS/STATA/SPSS)

```python
	pd.read_sas() 	#必要时添加encoding参数
	pd.read_spas() #0..25版本之后新增
	pd.read_stata()
```

- 读取数据库数据

	1. 配置对应的数据库驱动	
	
		所需程序包：
	
		1.1. SQL Alchemy engine : 几乎可以使用任何常见的DB格式和操作命令（https://docs.sqlalchemy.org/en/14/dialects/index.html）
		
		1.2. DBAPI2 connection : 只对SQLite3有较为完整的支持
	
	2. 读取数据表
	
```python
	#MySQL数据库
	import pandas as pd
	from sqlalchemy import create_engine
	engine = create_engine('mysql+pymysql://root:root2019@localhost:3306/sdb?charset=gbk')
	print(type(engine))
	users = pd.read_sql('select * from sys_user',con=engine)
	print(users)
	uc = pd.read_sql('select count(*) from sys_user', con=engine)
	print(type(uc))
	print(uc)
	ud = users.to_dict()
	print(type(ud))
	for k,v in ud.items():
		print('Key is : ', k, ' value type is : ', type(v), ' the 12th data is : ', v.get(11))
		for kk,vv in v.items():
			print('Key is :', kk, ' value is : ', vv)
	#Oracle数据库	
	import cx_Oracle as cxoc
	#首先要初始化Oracle client library
	cxoc.init_oracle_client(lib_dir=r"D:\Development\Python\db-drivers\instantclient_19_8")
	engine = create_engine('oracle+cx_oracle://dcstest0801:Tsv33db#2016@10.40.128.171:1521/orcl?encoding=UTF-8&nencoding=UTF-8')
	users = pd.read_sql('select * from gp_operator', con=engine)
	print(users)
	uc = pd.read_sql('select count(*) from gp_operator', con=engine)
	print('User count is : ', uc)
```

### 数据读入/保存命令总结

| 数据格式 | 读入命令 | 保存命令 | 
| ------------- | ------------- | ------------- | 
| 剪贴板 | read_clipboard | to_clipboard | 
| General delimited File | read_table | | 
| Fixed-width File | read_table | | 
| csv | read_csv | to_csv | 
| MS Excel | read_excel | to_excel | 
| OpenDocument | read_excel | | 
| JSON | read_json | to_json | 
| html | read_html | to_html | 
| Stata | read_stata | to_stata | 
| SAS | read_sas|  | 
| SPSS | read_spss | pyreadstat.write_sav | 
| SQL | read_sql,read_sql_query,read_sql_table | to_sql | 
| Google BigQuery | read_gbq | to_gbq | 
| HDF5 Format | read_hdf | to_hdf | 
| Feather Format | read_feather | to_feather | 
| Parquet Format | read_parquet | to_parquet | 
| ORC Format | read_orc |  | 
| Msgpack | read_msgpack | to_msgpack | 
| Python Pickle Format | read_pickle | to_pickle | 

### Pandas将DataFrame转换为其他数据格式的命令

| 数据格式 | 转换命令 |
| ------------- | ------------- |
| dict格式 | to_dict | 
| Markdown-friendly 表格格式 | to_markdown |
| Console-friendly tabularoutput | to_string |
| Numpy array | to_numpy |
| Numpy record array | to_records |
| Latex格式 | to_latex |
| Parquet | to_parquet |
| xarray object | to_xarray |

```python
	#写入CSV	
	print('-' * 80)
	users = pd.DataFrame(columns=['Name','Email','Address','Mobile','age'],
		data=[
			['Harry','jack1@163.com','SD JN','13780924007',20],
			['Jack','jack2@163.com','SD JN','13780924007',26],
			['Tom','jack3@163.com','SD JN','13780924007',27],
			['Will','jack4@163.com','SD JN','13780924007',28],
			['Bill','jack5@163.com','SD JN','13780924007',24],
			['Alex','jack6@163.com','SD JN','13780924007',29],
			['Max','jack7@163.com','SD JN','13780924007',31],
			['Jane','jack8@163.com','SD JN','13780924007',30],
			['Jon','jack9@163.com','SD JN','13780924007',23],
			['Dany','jack10@163.com','SD JN','13780924007',22]
		]
	)
	print(users)
	'''
		to_csv(
			filepath_or_buffer:''   #文件路径,
			sep=','                 #分隔符,
			columns=[...],          #导出的变量列表 
			header=True,            #重置变量名，也可提供新的列表
			index=True,             #是否导出索引
			mode='',                #导出模式：r,r+,w,w+,a,a+
			encoding='utf-8'        #编码集       
		)
	'''
	users.to_csv('C:\\Users\\20112004\\Desktop\\tmp\\users.txt',index=False,header=['姓名','邮箱','地址'],columns=['Name','Email','Address'],mode='a+')
	print('-' * 80)
	#写入Excel
	 import pandas as pd
	print('-' * 80)
	users = pd.DataFrame(columns=['Name','Email','Address','Mobile','age'],
		data=[
			['Harry','jack1@163.com','SD JN','13780924007',20],
			['Jack','jack2@163.com','SD JN','13780924007',26],
			['Tom','jack3@163.com','SD JN','13780924007',27],
			['Will','jack4@163.com','SD JN','13780924007',28],
			['Bill','jack5@163.com','SD JN','13780924007',24],
			['Alex','jack6@163.com','SD JN','13780924007',29],
			['Max','jack7@163.com','SD JN','13780924007',31],
			['Jane','jack8@163.com','SD JN','13780924007',30],
			['Jon','jack9@163.com','SD JN','13780924007',23],
			['Dany','jack10@163.com','SD JN','13780924007',22]
		]
	)
	print(users)
	'''
		to_excel(
			filepath_or_buffer:''   #文件路径,
			columns=[...],          #导出的变量列表 
			header=True,            #重置变量名，也可提供新的列表
			index=True,             #是否导出索引
			encoding='utf-8'        #编码集       
		)
	'''
	users.to_excel('C:\\Users\\20112004\\Desktop\\tmp\\users.xlsx',index=False,header=['姓名','邮箱','地址'],columns=['Name','Email','Address'])
	print('-' * 80)
	#写入数据库
	import pandas as pd
	from data.read.DatabaseEngines import DatabaseEngines
	users = pd.DataFrame(columns=['Name','Email','Address','Mobile','age','birthday'],
		data=[
			['Harry','jack1@163.com','SD JN','13780924007',20,'1985-12-02'],
			['Jack','jack2@163.com','SD JN','13780924007',26,'1985-12-02'],
			['Tom','jack3@163.com','SD JN','13780924007',27,'1985-12-02'],
			['Will','jack4@163.com','SD JN','13780924007',28,'1985-12-02'],
			['Bill','jack5@163.com','SD JN','13780924007',24,'1985-12-02'],
			['Alex','jack6@163.com','SD JN','13780924007',29,'1985-12-02'],
			['Max','jack7@163.com','SD JN','13780924007',31,'1985-12-02'],
			['Jane','jack8@163.com','SD JN','13780924007',30,'1985-12-02'],
			['Jon','jack9@163.com','SD JN','13780924007',23,'1985-12-02'],
			['Dany','jack10@163.com','SD JN','13780924007',22,'1985-12-02']
		]
	)
	print(users)
	'''
		df.to_sql(
			name='table name',      #表名
			con=engine,             #SQLAlchemy引擎
			if_exists='append',     #如果表已经存在，如何处理,取值：‘fail’：不做任何处理，‘replace’：删除源表并重建新表；‘append’：在原表追加数据
			index=False             #是否导出索引
		)
	'''
	connection_engine = DatabaseEngines.create('mysql')
	users.to_sql(name='tb_user',con=connection_engine,if_exists='replace',index=True)
	print('数据已导入数据库')
```

## 变量列的基本操作