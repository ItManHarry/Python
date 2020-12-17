# Pandas 进阶4

## 数据分组

```python
	import pandas as pd
	import random as rd
	data = [[rd.choice(['A','B','C','D']), rd.choice(['CLASS-1','CLASS-2','CLASS-3']), rd.randint(0, 100), i] for i in range(200)]
	columns = ['Group', 'Class', 'Score' , 'Index']
	df = pd.DataFrame(data=data, columns=columns)
	print('Data is : \n', df)
	df.to_excel('C:\\Users\\20112004\\Desktop\\tmp\\scores.xlsx')
	print('Write to the Excel finished ...')
	#分组
	'''
		df.groupby(
			by :                #用于分组的变量名/函数
			axis = 0 :
			level = None :      #相应的轴存在多重索引时，指定用于分组的级别
			as_index = True :   #在结果中将组标签作为索引
			sort = True :       #结果是否按照分组关键字进行排序 
			dropna = True :     #是否将NA看作普通键值用于分组
		)
	'''
	dg1 = df.groupby('Group')
	#分组结果（值为字典，key为列值，value为索引list）
	print('Group data 1 column : \n', dg1.groups)
	#分组结果描述
	print('Group describe 1 column : \n', dg1.describe())
	dg1.describe().to_excel('C:\\Users\\20112004\\Desktop\\tmp\\group1column.xlsx')
	dg2 = df.groupby(['Group','Class'])
	print('Group data 2 columns : \n', dg2.groups)
	print('Group describe 2 columns : \n', dg2.describe())
	dg2.describe().to_excel('C:\\Users\\20112004\\Desktop\\tmp\\group2columns.xlsx')
```	

## 分组汇总

	使用aggregate函数进行汇总
	
	df.aggregate(),使用时直接简写为agg
	
	可以直接使用的函数有 ：
	
	1. count() : 统计非空值的个数
	
	2. size():  统计分组大小，包含空值
	
	3. sum(): 统计分组合计值
	
	4. mean(): 平均数
	
	5. median(): 算数中位数
	
	6. min():最小值
	
	7. max()：最大值
	
	8. std():标准差
	
	9. var():方差
	
	10. skew():分度
	
	11. kurt():偏度
	
	12. quantile():分位数
	
	13. apply():函数批量运行
	
	14. cov():斜方差
	
	15. corr():相关系数
	
```python
	import pandas as pd
	import random as rd
	import numpy as np
	data = [[rd.choice(['A','B','C','D']), rd.choice(['CLASS-1','CLASS-2','CLASS-3']), rd.choice(['TYPE-1','TYPE-2','TYPE-3']), rd.randint(0, 100), i] for i in range(200)]
	columns = ['Group', 'Class', 'Type', 'Score' , 'Index']
	df = pd.DataFrame(data=data, columns=columns)
	print('Data is : \n', df)
	df.to_excel('C:\\Users\\20112004\\Desktop\\tmp\\scores.xlsx')
	print('Write source data to the Excel finished .')
	#汇总函数
	'''
		df.agg()
	'''
	#先进行分组
	dg1 = df.groupby('Group')
	#导出数据
	dg1.describe().to_excel('C:\\Users\\20112004\\Desktop\\tmp\\groupby1.xlsx')
	#执行汇总 - 个数统计
	dg1.agg('count').to_excel('C:\\Users\\20112004\\Desktop\\tmp\\groupby-count.xlsx')
	#执行汇总 - 中位数
	dg1.agg('median').to_excel('C:\\Users\\20112004\\Desktop\\tmp\\groupby-median.xlsx')
	#执行汇总 - 平均数&中位数
	dg1.agg(['mean','median']).to_excel('C:\\Users\\20112004\\Desktop\\tmp\\groupby-mix.xlsx')
	#引用非内置函数
	dg1.agg(np.sum).to_excel('C:\\Users\\20112004\\Desktop\\tmp\\groupby-numpy.xlsx')
	#引用自定义函数
	def mymean(x):
		return x.mean()
	dg1.agg(mymean).to_excel('C:\\Users\\20112004\\Desktop\\tmp\\groupby-udf.xlsx')
	#交叉表
	pd.crosstab(df.Class, df.Type).to_excel('C:\\Users\\20112004\\Desktop\\tmp\\groupby-crosstab.xlsx')
	#指定分组列名
	dg1.agg(
		样本量 = pd.NamedAgg(column='Score', aggfunc='count'),
		平均分 = pd.NamedAgg(column='Score', aggfunc=np.mean),
		最低分 = pd.NamedAgg(column='Score', aggfunc='min'),
		最高分 = pd.NamedAgg(column='Score', aggfunc='max')
	).to_excel('C:\\Users\\20112004\\Desktop\\tmp\\groupby-names1.xlsx')
	dg1.agg(
		样本量 = pd.NamedAgg('Score', 'count'),
		平均分 = pd.NamedAgg('Score', np.mean),
		最低分 = pd.NamedAgg('Score', 'min'),
		最高分 = pd.NamedAgg('Score', 'max')
	).to_excel('C:\\Users\\20112004\\Desktop\\tmp\\groupby-names2.xlsx')
```