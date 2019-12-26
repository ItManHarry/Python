# Chapter 3 - 流程控制 if while for-in

## 程序流程

- 顺序结构

- 分支结构

	1. if分支基础
	
		语法格式一：
		
			if 条件:
				执行体
				
		语法格式二：
			
			if 条件:
				执行体
			else:
				执行体
				
		语法格式三：
		
			if 条件:
				执行体
			elif 条件:
				执行体
			else
				执行体
	
	2. if分支高级
	
		2.1 if条件可以是任意值，除了False本身之外，各个代表'空'的None、空字符串、空元组、空列表、空字典，都会被当做False，一下各个值都会被当成False处理：
		
		False/None/0/""/()/[]/{}
		
		2.2. 三目运算符
		
			表达式 if 条件 else 表达式
			
		2.3. pass语句，只是占位，不执行任何操作

- 循环结构

	1. while循环
	
		格式：
			while test_expression:
				body_statements
				[iteration_statements]
				
		由于列表和元组都是有索引的，所以可以通过while循环来遍历列表和元组
		
```python
	v_list = [1,2,3,4,5,3,3,4,5,2,9,8,10]
	v_dict = {'A':100,'B':200,'C':300,'D':400}
	print(len(v_list))
	print('-' * 80)
	i = 0
	while i < len(v_list):
		print(v_list[i])
		i += 1
	print('-' * 80)
	i = 0
	v_keys = list(v_dict.keys())
	while i < len(v_keys):
		print('Key : ', v_keys[i], ', Value : ', v_dict[v_keys[i]])
		i += 1
```
	
	2. for-in循环
	
		遍历列表、元组、字典
		
```python
	v_list = [1,2,3,4,5,3,3,4,5,2,9,8,10]
	v_dict = {'A':100,'B':200,'C':300,'D':400}
	print('-' * 80)
	for i in v_list:
		print(i)
	print('-' * 80)
	for k, v in v_dict.items():
		print('Key : ', k, ', Value : ', v)
	print('-' * 80)
	for i in range(10):
		print(i)
```

	3. 列表推导式
	
	语法格式：
	
		[表达式  for 循环计数器 in 可迭代对象]

	4. break , continue,return