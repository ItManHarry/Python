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
	
- 按照位置筛选数据
 
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
