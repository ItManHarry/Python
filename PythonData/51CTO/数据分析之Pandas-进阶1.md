# Pandas 进阶1

## Pandas索引

- 索引的用途：
	
	1. 用于分析、可视化、数据展示、数据操作中标记数据行
	
	2. 提供数据汇总、合并、筛选时的关键依据
	
	3. 提供数据重构的关键依据
	
- 注意事项

	1. 索引是不可以直接修改的，只能新增、删除、替换
	
	2. 逻辑索引不应当出现重复值，Pandas不会对此情况报错，存在一定的风险
	
- 创建索引

```python
	import pandas as pd
	from data.read.DatabaseEngines import DatabaseEngines
	#创建时指定索引
	data = pd.DataFrame(data=[
		[1,2,3,4,5],
		[10,20,30,40,50],
		[100,200,300,400,500],
		[1000,2000,3000,4000,5000],
		[10000,20000,30000,40000,50000],
		[100000,200000,3000000,400000,500000]
	],columns=['C01','C02','C03','C04','C05'],index=['a','b','c','d','e','f'])
	print(data)
	print('-' * 80)
	#读取时指定某一列为索引(index_col=?)
	engine = DatabaseEngines.create('mysql')
	print(type(engine))
	users = pd.read_sql('select * from sys_user',con=engine,index_col='tid')
	print(users)
	#创建复合索引
	engine = DatabaseEngines.create('oracle')
	print('执行获取所有的用户信息')
	users = pd.read_sql('select * from gp_operator where status in (0, 1) and orgid = -1 order by name', con=engine,index_col=['id','code'])
	print(users)
```

- 指定某列为索引列

```python
	import pandas as pd
	from data.read.DatabaseEngines import DatabaseEngines	
	users_no_index = pd.read_sql('select * from sys_user',con=engine)		
	#指定某列为索引列
	'''
		df.set_index(
			keys:''         #被指定的索引列列名，复合索引用list格式提供,
			drop=True,      #建立索引后是否删除该列
			append=False,   #是否在原索引基础上添加索引，默认是直接替换原索引
			inplace=False   #是否直接修改原数据
		)
	'''
	users_no_index.set_index('tid',drop=False,inplace=True)
	print('Set MySQL user index : \n', users_no_index)
```

- 将索引还原回列

```python
	import pandas as pd
	from data.read.DatabaseEngines import DatabaseEngines
	#创建时指定索引
	data = pd.DataFrame(data=[
		[1,2,3,4,5],
		[10,20,30,40,50],
		[100,200,300,400,500],
		[1000,2000,3000,4000,5000],
		[10000,20000,30000,40000,50000],
		[100000,200000,3000000,400000,500000]
	],columns=['C01','C02','C03','C04','C05'],index=['a','b','c','d','e','f'])
	print(data)
	print('-' * 80)
	#读取时指定某一列为索引(index_col=?)
	engine = DatabaseEngines.create('mysql')
	print(type(engine))
	users_index = pd.read_sql('select * from sys_user',con=engine,index_col='tid')
	users_no_index = pd.read_sql('select * from sys_user',con=engine)
	print('MySQL user with index : \n', users_index)
	print('MySQL user without index : \n', users_no_index)
	#创建复合索引
	engine = DatabaseEngines.create('oracle')
	users_oracle = pd.read_sql('select * from gp_operator where status in (0, 1) and orgid = -1 order by name', con=engine)
	users_oracle_copy = users_oracle.copy()     #oracle用户数据副本
	users_oracle.set_index(['id','code'],drop=True, inplace=True)
	print('Oracle users with index : \n', users_oracle)
	print('Oracle users without index : \n', users_oracle_copy)
	#指定某列为索引列
	'''
		df.set_index(
			keys:''         #被指定的索引列列名，复合索引用list格式提供,
			drop=True,      #建立索引后是否删除该列
			append=False,   #是否在原索引基础上添加索引，默认是直接替换原索引
			inplace=False   #是否直接修改原数据
		)
	'''
	users_no_index.set_index('tid',drop=True,inplace=True)
	print('Set MySQL user index : \n', users_no_index)
	#将索引还原回列
	'''
		df.reset_index(
			drop = False,   #是否将索引直接删除，而不是还原为变量列
			inplace = False,#是否直接修改原数据
			level=None      #对于多重索引，确定转换哪个级别为变量
		)
	'''
	#还原MySQL用户数据索引
	users_no_index.reset_index('tid',inplace=True)
	print('MySQL user index has been reset : \n', users_no_index)
	users_oracle.reset_index(['code'],drop=True,inplace=True)
	print('Oracle user reset index : \n', users_oracle)
```

- 引用和修改索引

	注：索引是有存储格式的，注意区分数值型和字符型的引用方式
	
```python
	import pandas as pd
	from data.read.DatabaseEngines import DatabaseEngines
	#创建时指定索引
	data = pd.DataFrame(data=[
		[1,2,3,4,5],
		[10,20,30,40,50],
		[100,200,300,400,500],
		[1000,2000,3000,4000,5000],
		[10000,20000,30000,40000,50000],
		[100000,200000,3000000,400000,500000]
	],columns=['C01','C02','C03','C04','C05'],index=['a','b','c','d','e','f'])
	print(data)
	print('-' * 80)
	#读取时指定某一列为索引(index_col=?)
	engine = DatabaseEngines.create('mysql')
	print(type(engine))
	users_index = pd.read_sql('select * from sys_user',con=engine,index_col='tid')
	users_no_index = pd.read_sql('select * from sys_user',con=engine)
	print('MySQL user with index : \n', users_index)
	print('MySQL user without index : \n', users_no_index)
	#创建复合索引
	engine = DatabaseEngines.create('oracle')
	users_oracle = pd.read_sql('select * from gp_operator where status in (0, 1) and orgid = -1 order by name', con=engine)
	users_oracle_copy = users_oracle.copy()     #oracle用户数据副本
	users_oracle.set_index(['id','code'],drop=True, inplace=True)
	print('Oracle users with index : \n', users_oracle)
	print('Oracle users without index : \n', users_oracle_copy)
	#指定某列为索引列
	'''
		df.set_index(
			keys:''         #被指定的索引列列名，复合索引用list格式提供,
			drop=True,      #建立索引后是否删除该列
			append=False,   #是否在原索引基础上添加索引，默认是直接替换原索引
			inplace=False   #是否直接修改原数据
		)
	'''
	users_no_index.set_index('tid',drop=True,inplace=True)
	print('Set MySQL user index : \n', users_no_index)
	#将索引还原回列
	'''
		df.reset_index(
			drop = False,   #是否将索引直接删除，而不是还原为变量列
			inplace = False,#是否直接修改原数据
			level=None      #对于多重索引，确定转换哪个级别为变量
		)
	'''
	#还原MySQL用户数据索引
	users_no_index.reset_index('tid',inplace=True)
	print('MySQL user index has been reset : \n', users_no_index)
	users_oracle.reset_index(['code'],drop=True,inplace=True)
	print('Oracle user reset index : \n', users_oracle)
	print('-' * 80)
	print('Indexes : ', users_oracle.index)
	print('Index names : ', users_oracle.index.names)
	#修改索引名称
	users_oracle.index.names = ['数值ID']
	print('Now the index names : ', users_oracle.index.names)
	print(users_oracle)
	#修改索引值：索引值是无法单个修改的，所以此处的修改本质上就是全部修改
	print('MySQL user : \n', users_index)
	users_index.index.names = ['自增ID']
	print('MySQL user index name changed : \n', users_index)
	users_index.index = ['id00%s' %i for i in range(12)]
	print('MySQL user index value changed : \n', users_index)
```	

- 强行更新索引

	reindex可以使用DataFrame中不存在的数值建立索引，并据此扩充新索引值对应的索引行/列，同时进行缺失值填充操作
	
```python
	import pandas as pd
	import random as rd
	#创建数据
	data = [['N%s' %i,'jack%s@163.com' %i, rd.randint(20, 45), '1%s%s%s%s' %(rd.choice([3,5,6]), rd.randint(0,9), rd.randint(1000,9999), rd.randint(1000,9999)), rd.choice(['F','M'])] for i in range(4000)]
	columns = ['姓名','邮箱','年龄','手机号','性别']
	print(data)
	df = pd.DataFrame(data=data,columns=columns)
	print(df)
	#强行更新索引
	'''
		df.reindex(
			labels: [...],          #类数组结构的数值，将按此数值重建索引，非必需
			axis:                   #针对哪个轴进行重建 : ('index','columns') or number(0, 1)
			copy=True,              #建立新对象而不是直接修改原数据
			level :                 #考虑被重建的索引级别  
			#缺失数据的处理方式
			method :                #针对已经排过序的索引，确定数据单元格无数据的填充方式，非必需
			pad / ffill:            #用前面有效值进行填充
			backfill / bfill:       #用后面有效值进行填充
			nearest:                #使用最接近的数值进行填充
			fill_value=np.NaN:      #缺失值使用什么数值代替
			limit=None              #向前/向后填充的最大步长                              
		)
	'''
	print('Reindex without fill : \t', df.reindex([1,2,40,50,100,1000,2000,4001]))
	print('Reindex using ffill : \t', df.reindex([1,2,40,50,100,1000,2000,4001], method='ffill'))
	print('Reindex using a value : \t', df.reindex([1,2,40,50,100,1000,2000,4001], fill_value='Null'))
```