# 数据分析库 - Pandas

## Pandas简介：

	pandas 是基于NumPy 的一种工具，该工具是为了解决数据分析任务而创建的。Pandas 纳入了大量库和一些标准的数据模型，提供了
高效地操作大型数据集所需的工具。pandas提供了大量能使我们快速便捷地处理数据的函数和方法。你很快就会发现，它是使Python成
为强大而高效的数据分析环境的重要因素之一。
	
	出处：https://baike.baidu.com/item/pandas/17209606?fr=aladdin
	

## 读取中文数据表表报错

``` python
	UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb4 in position 0: invalid start byte
```

	解决方法：指定encoding为'gbk'即可
	
```python
	import pandas as pd
	df = pd.read_csv('./data/employees.csv',encoding='gbk')
	print(df.info())
```
