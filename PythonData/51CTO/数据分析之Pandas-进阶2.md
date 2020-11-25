# Pandas 进阶2

## 使用索引排序

```python
	import pandas as pd
	import random as rd
	#创建数据
	data = [['N%s' %i,'jack%s@163.com' %i, rd.randint(20, 45), '1%s%s%s%s' %(rd.choice([3,5]), rd.randint(0,9), rd.randint(1000,9999), rd.randint(1000,9999)), rd.choice(['F','M']), rd.choice(['山东','河南','山西','河北','湖南','湖北','北京','上海','广州'])] for i in range(5000)]
	columns = ['职号','邮箱','年龄','手机号','性别','地区']
	#print(data)
	df = pd.DataFrame(data=data,columns=columns)
	#设置索引
	df.set_index(['地区','手机号'], drop=True, inplace=True)
	print('Data is : \n', df)
	'''
		df.sort_index(
			level :  ,               #多重索引时，指定使用哪个索引进行排序
			ascending=True ,         #是否升序排列，多列时以列表形式提供
			inplace=False   ,        #是否更改原数据
			na_position = 'last' ,   #缺失值的排序顺序（first/last）
			ignore_index=False  ,    #是否忽略原索引值，若为True，则之前的索引消失并重置为0,1,2,...N - 1
			key = None               #在排序前对索引值引用指定的key函数
		)
	'''
	#索引排序
	print('Data sorted by index : \n', df.sort_index())
	#指定排序顺序，地区升序、手机号降序
	print('Data sorted by index in different ascending way : \n', df.sort_index(ascending=[True, False]))
	#多列索引时，指定按照某列进行排序
	print('Data sorted by index by area : \n', df.sort_index(level='地区', ascending=False))
	#指定排序顺序，地区升序、手机号降序,并取消原索引
	print('Data sorted by index in different ascending way and ignore source indexes: \n', df.sort_index(ascending=[True, False], ignore_index=True))
	#按照手机号前三位进行排序
	print('Sorted by function : \n', df.sort_index(level='手机号', key=lambda x : x.str[:3]))
```

## 按照某一列排序
	
```python
	import pandas as pd
	import random as rd
	#创建数据
	data = [['N%s' %i,'jack%s@163.com' %i, rd.randint(20, 45), '1%s%s%s%s' %(rd.choice([3,5]), rd.randint(0,9), rd.randint(1000,9999), rd.randint(1000,9999)), rd.choice(['F','M']), rd.choice(['山东','河南','山西','河北','湖南','湖北','北京','上海','广州'])] for i in range(5000)]
	columns = ['职号','邮箱','年龄','手机号','性别','地区']
	#print(data)
	df = pd.DataFrame(data=data,columns=columns)
	print('Data : \n', df)
	'''
		df.sort_values(
			by :                        #指定用于排序的变量名，多列时使用列表提供
			ascending=True    ,         #是否升序排列，多列时以列表形式提供
			inplace=False      ,        #是否更改原数据
			na_position = 'last'  ,     #缺失值的排序顺序（first/last）
			ignore_index=False  ,       #是否忽略原索引值，若为True，则之前的索引消失并重置为0,1,2,...N - 1
			key = None                  #在排序前对索引值引用指定的key函数
		)
	'''
	#根据年龄排序
	print('Sorted by age : \n', df.sort_values('年龄', ascending=False))
	print('Source data : \n', df)
```

## 案例筛选

	筛选操作的实质：基于T/F值进行筛选
	
	sl = [True, False, True, True]
	
- 按照实际位置筛选数据
 
```python
	import pandas as pd
	import random as rd
	#创建数据
	data = [['N%s' %i,'jack%s@163.com' %i, rd.randint(20, 45), '1%s%s%s%s' %(rd.choice([3,5]), rd.randint(0,9), rd.randint(1000,9999), rd.randint(1000,9999)), rd.choice(['F','M']), rd.choice(['山东','河南','山西','河北','湖南','湖北','北京','上海','广州'])] for i in range(5000)]
	columns = ['职号','邮箱','年龄','手机号','性别','地区']
	#print(data)
	df = pd.DataFrame(data=data,columns=columns)
	print('Data : \n', df)
	sl = [True, False, True, True]
	print('0 - 10 records : \n', df.iloc[0:10])                         			#取某个范围内的数据不包括右侧边界
	print('0,3,5,7 records : \n', df.iloc[[0,3,5,7]])                   			#取具体的某几条数据
	print('0 - 10 rows, 1 - 3 columns : \n', df.iloc[0:11,1:4])         	#取某几列、某几行数据(范围别)
	print('0 , 11 rows, 1 , 4 columns : \n', df.iloc[[0,11],[1,4]])     	#取某几列、某几行数据(指定哪行哪列)
```	

- 按照索引值筛选/混合索引值筛选

```python
	import pandas as pd
	import random as rd
	#创建数据
	data = [['N%s' %i,'jack%s@163.com' %i, rd.randint(20, 45), '1%s%s%s%s' %(rd.choice([3,5]), rd.randint(0,9), rd.randint(1000,9999), rd.randint(1000,9999)), rd.choice(['F','M']), rd.choice(['山东','河南','山西','河北','湖南','湖北','北京','上海','广州'])] for i in range(5000)]
	columns = ['职号','邮箱','年龄','手机号','性别','地区']
	#print(data)
	df = pd.DataFrame(data=data,columns=columns)
	df.set_index(['地区','手机号'], inplace = True)
	print('Data : \n', df)
	sl = [True, False, True, True]
	#按照索引值筛选
	print('Shanghai and Hunan : \n', df.loc[['上海','湖南']])
	#print(df.loc[[('河北','15254809555'),('广州','15273142801')]])
	#多索引筛选
	'''
		df.xs(
			key,            				#索引值
			level=None      		#使用哪个索引
			drop_level=True 		#是否删除索引列
		)
	'''
	print('ShangHai data : \n', df.xs('上海', level=0, drop_level=False))
```

- 条件筛选

	1. 按照数据范围进行筛选
	
	df[df.column > value]
	
	2. 列表筛选
	
	df.isin(values)
	
		values为序列：对应每个具体值
		values为字典：对应各个变量值
		values为数据框：同时对应数值和变量名称
		
```python
	import pandas as pd
	import random as rd
	#创建数据
	data = [['N%s' %i,'jack%s@163.com' %i, rd.randint(20, 45), '1%s%s%s%s' %(rd.choice([3,5]), rd.randint(0,9), rd.randint(1000,9999), rd.randint(1000,9999)), rd.choice(['F','M']), rd.choice(['山东','河南','山西','河北','湖南','湖北','北京','上海','广州'])] for i in range(5000)]
	columns = ['职号','邮箱','年龄','手机号','性别','地区']
	#print(data)
	df = pd.DataFrame(data=data,columns=columns)
	df.set_index(['地区','手机号'], inplace = True)
	print('Data : \n', df)
	#年龄范围筛选
	print('Person whose age above 30 : \n',df[df.年龄 > 30])
	#列表筛选
	ages = [23,25,30,35,40]
	print('Person whose age in (23,25,30,35,40) : \n', df[df.年龄.isin(ages)])
	#将索引恢复为列
	df.reset_index(['地区','手机号'],inplace=True)
	#只设置地区为索引列
	df.set_index('地区', inplace=True)
	print('Person live in 山东 and 山西 : \n', df[df.index.isin(['山东','山西'])])
	#多重条件联合查询
	print('Person age between 25 and 35', df[(df.年龄 > 25) & (df.年龄 < 35)])
```

	#类SQL语句查询
	
```python
	import pandas as pd
	import random as rd
	#创建数据
	data = [['N%s' %i,'jack%s@163.com' %i, rd.randint(20, 45), '1%s%s%s%s' %(rd.choice([3,5]), rd.randint(0,9), rd.randint(1000,9999), rd.randint(1000,9999)), rd.choice(['F','M']), rd.choice(['山东','河南','山西','河北','湖南','湖北','北京','上海','广州'])] for i in range(5000)]
	columns = ['code','email','age','mobile','gender','area']
	#print(data)
	df = pd.DataFrame(data=data,columns=columns)
	df.set_index(['area','mobile'], inplace = True)
	print('Data : \n', df)
	'''
		df.query(
			expr:           #类SQL语句表达式(可以使用前缀‘@’引用环境变量，等号为==，而不是=；注：目前不支持like)
			inplace=False   #是否替换原数据
		)
	'''
	#年龄25 - 35之间,非上海人
	print('Person age between 25 and 35 : \n', df.query("age > 25 and age < 35 and area not in ('上海')"))
	age = 30
	#年龄30 - 35之间,非上海人
	print('Person age between %s and 35 : \n' %age, df.query("age > @age and age < 35 and area not in ('上海')"))
```	