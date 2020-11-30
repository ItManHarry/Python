# Pandas 进阶3

## 修改列值

```python
	import pandas as pd
	import numpy as np
	print('-' * 80)
	df = pd.DataFrame(
		{
			'Col1': 1.2,
			'Col2': [1,2,3,4,5,6],
			'Col3': ['a','b','c','d','e','f'],
			'Col4': 'Cons1',
			'Col5': 100
		}
	)
	print('Source data is : \n', df)
	print('-' * 80)
	#添加一新列
	df.newcol = 1       #此写法虽然不会报错，但是不会生效
	print('Now the data is : \n', df)
	df['newcol'] = [100,200,300,400,480,980]    #此写法为正确的写法
	print('-' * 80)
	print('Now the data is : \n', df)
	#改变新列值为平方根
	df['newcol'] = np.sqrt(df['newcol'])
	print('Change the new column value : \n', df)
	#基于原变量做函数计算
	'''
		df.apply(
			func:           #希望对行/列执行的函数表达式
			axis = 0        #对行还是列进行计算  0/'index' : 针对列进行计算  1/'columns' : 针对行进行计算， 一般只针对列进行计算
		)
	'''
	import math
	df['newcol'] = df['newcol'].apply(math.sqrt)
	print('Change the column value for the second time : \n',  df)
	#使用自定义函数
	def first_char(v_str):
		return v_str[:1]
	df['name'] = ['Tom','Jack','Sam','Rose','Harry','Alex']
	print('Add a name column : \n', df)
	df['name'] = df['name'].apply(first_char)
	print('Name column changed : \n', df)
	#多个列的单元格进行相同计算
	df[['Col5','newcol']] = df[['Col5','newcol']].applymap(math.sqrt)
	print('Use applymap : \n', df)
	#assign命令，不修改原数据，生成新的数据源(新的数据源包含了所有旧的数据源列信息，同时新增了assign对应的列)
	ndf = df.assign(new = df['Col1'].apply(math.sqrt))
	print('DataFrame is : \n', df)
	print('New DataFrame is : \n', ndf)
	#指定位置插入新的变量列
	'''
		#该方法会直接修改原数据
		df.insert(
			loc :                   #插入位置的索引 : 0 <= loc <= len(columns)
			column:                 #插入列的名称
			value:                  #Series或者数组结构的变量值
			allow_duplicates=False  #是否允许列名重复
		)
	'''
	df.insert(1, 'NewColumn', '123456')
	print('Insert a column : \n', df)	
```

## 替换值

```python
	import pandas as pd
	import numpy as np
	print('-' * 80)
	df = pd.DataFrame(
		{
			'Col1': 1.2,
			'Col2': [1,2,3,4,5,6],
			'Col3': ['a','b','c','d','e','f'],
			'Col4': 'Cons1',
			'Col5': 100
		}
	)
	print('Source data is : \n', df)
	print('-' * 80)	
	#修改/替换变量值
	df.insert(2, 'Province', ['山东','山东省','上海','上海市','上海','上海市'])
	print('Now the data is : \n', df)
	#定位数据
	print('Province is Shanghai row data : \n', df[df['Province'].isin(['上海'])])
	print('Province is Shanghai cell data : \n', df['Province'][df['Province'].isin(['上海'])])
	#执行替换 - 以下方式会给出警告
	df['Province'][2] = '上海市'
	df['Province'][4] = '上海市'
	print('Now the data is : \n', df)
	#以下写法不会报警
	df.loc[4, 'Province'] = '山东省'
	print('Now the data is : \n', df)
	#替换值
	'''
		df.replace(
			to_replace = None               #要被替换的原值，所有严格匹配的数值将会被value替换，可以是：str/regex/list/dict/Series/numeric/None
			value: None                     #要换成的新值
			inplace = False                 #是否替换原数据
		)
	'''
	#精确替换
	df.replace('上海市','上海',inplace=True)
	print('After replace : \n', df)
	#替换某列的值
	df['Province'].replace('山东省','山东',inplace=True)
	print('ShanDong changed : \n', df)
	#多值替换
	df.replace(['上海','山东'],['上海市','山东省'], inplace=True)
	print('Multi inplace data frame : \n', df)
	df['Province'].replace(['上海市','山东省'],['上海','山东'], inplace=True)
	print('Multi inplace data column : \n', df)
```

##  指定数值范围的替换

- 正则表达式完成替换

	df.replace(regex, newvalue)
	
- 使用行筛选方式完成替换

```python
	import pandas as pd
	import numpy as np
	print('-' * 80)
	df = pd.DataFrame(
		{
			'Col1': 1.2,
			'Col2': [1,2,3,4,5,6],
			'Col3': ['a','b','c','d','e','f'],
			'Col4': 'Cons1',
			'Col5': 100
		}
	)
	print('Source data is : \n', df)
	print('-' * 80)
	#iloc绝对定位替换
	df['Col1'].iloc[2:5] = 2.5
	print('Now the data is : \n', df)
	#loc相对位置替换
	df['Col4'].loc[2:5] = 'NewValue'
	print('Now the data is : \n', df)
	df.loc[df['Col2'] < 5, 'Col5'] = 200
	print('Now the data is : \n', df)
	df.Col5[df.Col2 < 5] = 300
	print('Now the data is : \n', df)
	#query必须使用index定位，然后实现数值替换
	df.loc[df.query("Col1 < 2 and Col5 < 300").index, 'Col4'] = 'Harry'
	print('Now the data is : \n', df)
```

## 哑变量&变量分段

```python
	import pandas as pd
	import numpy as np
	print('-' * 80)
	df = pd.DataFrame(
		{
			'Col1': 1.2,
			'Col2': [1,2,3,4,5,6],
			'Col3': ['a','b','c','d','e','f'],
			'Col4': 'Cons1',
			'Col5': 100
		}
	)
	print('Source data is : \n', df)
	print('-' * 80)
	#哑变量
	'''
		pd.get_dummies(
			data:               #对应的数据框/变量列
			prefix = None       #哑变量前缀
			prefix_sep = '_'    #哑变量序号分隔符
			dummy_na = False    #是否为NaNs专门设定一个哑变量列
			drop_first = False  #是否返回k-1哑变量，而不是k个变量
		)
	'''
	print(pd.get_dummies(df.Col2, prefix='Dummy'))
	print(pd.get_dummies(df, columns=['Col3'], prefix='列4'))
	#数值变量分段(分箱)
	'''
		pd.cut(
			x:                      #进行分段的变量名称
			bins:                   #具体的分段设定(int : 被等距等分的段数, sequence of scalars : 具体的每一个分段起点，必须包括最值，可不等距)
			right=True              #每段是否包括右侧界值
			labels=None             #为每个分段提供自定义标签
			include_lowest = False  #第一段是否包括最左侧界值，需要和right参数配合使用
		)
		
		pd.pcut()       #按照频数，而不是按照取值范围进行等分
	'''
	df['Class'] = pd.cut(df.Col2, bins=[1,3,7], right=False)
	print('Now the data is : \n', df)
```