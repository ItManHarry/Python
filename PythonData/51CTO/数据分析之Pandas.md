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
	import pandas as pd
	from sqlalchemy import create_engine
	engine = create_engine('mysql+pymysql://root:root2019@localhost:3306/sdb?charset=gbk')
	print(type(engine))
	users = pd.read_sql('select * from sys_user',con=engine)
	print(users)
	uc = pd.read_sql('select count(*) from sys_user', con=engine)
	print(type(uc))
	print(uc)
```

### 数据读入/保存命令总结

|---数据格式---|---读入命令---|---保存命令---|
| 剪贴板 | read_clipboard | to_clipboard |