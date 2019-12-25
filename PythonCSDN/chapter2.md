# Chapter 2	
	
## 序列、元组

- 列表和元组都属于序列，区别在于列表是可变的，元组不可变（程序是无法修改的）。
	
	创建方式：
	
	1. 列表是方括号，元组是圆括号(如果元组中只有一个元素，必须添加一个逗号)
	
		列表：[1,2,3,4,5]
		
		元组：(1,2,3,4,5)
		
	2. 列表用list()创建，元组用tuple()创建方式：
	
- 列表、元组访问

	1. 列表、元组通过索引进行访问，可以正向访问也可反向访问(访问单个元素)
		
```python
	my_list = [1,2,3,'Python',3.4]
	print(my_list[0], my_list[2], my_list[-2])
```

	2. 截取列表、元素
	
```python
	my_list = [1,2,3,'Python',3.4]
	print(my_list[1:3])
	print(my_list[3:-1])
	print(my_list[1:7:2])
```	

	3. 列表、元组相加
	
	列表、元组支持相加的方法，相加就是列表、元组元素的总和
	
```python
	list1 = [1,2,3]
	list2 = ['a','b','c']
	print("list1 + list2 :",list1 + list2)
	tuple1 = (1,2,3)
	tuple2 = ('a','b','c')
	print("tuple1 + tuple2", tuple1 +tuple2)
```
	
	注意：列表只能和列表相加、元组只能和元组相加。如果列表加元组，需要使用list函数将元组转换为列表后再相加
	
	4. 列表、元组相乘：意义就是把它们包含的元素重复N次(字符串也支持乘法运算)
	
```python
	list = [1,2,3]
	print("list * 3 :", list1 * 3)
	str1 = 'abc'
	print(str1 * 3)
```
	
### 序列相关函数与封包解包

- 函数

	1. len()
	
	2. max()
	
	3. min()
	
- 封包

	把多个值付给一个变量时，Python会自动将多个值封装成元组，这种功能称为序列封包
	
```python
	pck = 1,2,3,'Python',3.4
	print(type(pck))
	print("pck is : ", pck)
```
	
- 解包

	把一个元组付给多个变量时，Python会自动将元组元素分别付给各个变量（变量个数要和元组元素个数相等），这种功能叫做序列解包(适用于元组、字符串)
	
```python
	#全解包
	params = ['python',1, 2]
	a,b,c=params
	print("a is : ",a, "b is : ",b," c is : ",c)
	#部分解包
	params = ('a','b','c','d','e')
	a, *b = params
```

- Python支持将多个元素付给多个变量

```python
	a,b,c = 10 , 'Python', 30
	print("a is : ",a,", b is :", b, ", c is : ", c)
```

- 列表操作方法

	1. 添加
		
		1.1. append()：会把传入的参数追加到列表的最后面，如果传入的是一个列表，那么这个列表会被当做一个元素添加到列表最后面。
		
```python
	list1= [1,2,3]
	list1.append("Java")
	print("list is :", list1)
```

		1.2. extend(): 该方法用于追加另一个列表，它会把列表中的每个元素添加到当前列表
		
```python
	list1= [1,2,3]	
	list1.extend(tuple(range(1,6)))
	print("list is :", list1)
```		
		1.3. insert()：将元素插入到指定的位置
		
```python
	list1= [1,2,3]
	list1.insert(2,'Jack')
	print("list is :", list1)
```
		
	2. 删除
	
		2.1. del语句是Python专门用来执行删除操作的语句，不仅可以删除列表的某个或者某段元素，也可以用来删除变量
		
```python
	list1= [1,2,3,4,5,6]
	del list1[2]
	print('After delete : ', list1)
	del list1[3:5]
	print('After delete : ', list1)
	del list1[2:5:2]
	print('After delete : ', list1)
```
		
		2.2. remove()方法，不根据index删除，删除第一个匹配的元素
		
```python
	list1= [1,2,3,4,5,6]
	list1.remove(5)
	print('After delete : ', list1)
```

		2.3. 元素赋值，也可实现列表的增加和删除元素
		
```python
	my_list = [1,2,3,'Python']
	my_list[-2] = 'Java'
	print("My list is : ", my_list)
	my_list[2:4] = ['a','b','c']
	print("My list is : ", my_list)
	my_list[2:4] = ['Python']
	print("My list is : ", my_list)
	#字符串会被当成数组处理
	my_list[2:4] = 'Python'
	print("My list is : ", my_list)
```

	2.4. 列表常用方法
	
```python
	my_list = [1,2,3,'Python']
	#count()
	print(my_list.count(1))
	#index()
	print(my_list.index(100))
	#pop()
	my_list.pop()
	print(my_list)
	#reverse()
	my_list.reverse()
	print(my_list)
	my_list = [1,5,2,1,8,2,10,4,19]
	print(my_list)
	#sort() - 此方法仅限于列表中的元素是统一类型
	my_list.sort()
	print(my_list)
	my_list.reverse()
	print(my_list)
```

## 字典

### 字典基础

	字典用于保存具有映射关系的数据（key-value对），key不允许重复
	
	创建方式：
	
		1. 花括号直接创建
		
```python
	my_dict = {"Java":98, "Python":89,"Javascipt":94}
	print(my_dict)
```
		
		2. dict构筑器, 可以传入多个列表或者元组参照作为key-value对,也可对dict指定关键字创建字典，此时字段的key不允许使用表达式
		
```python
	#dict构造器构造，参数为列表，列表元素为元组，元组元素只能是两个，一个为key，一个为value
	my_dict = dict([("Java",100,),("Python",120),("Javascipt",110)])
	print(my_dict)
	my_dict = dict((("Java",500,),("Python",600),("Javascipt",700)))
	print(my_dict)
	#dict构造器指定关键字创建字典，此时字段的key不允许使用表达式
	my_dict = dict(Java=200,Python=300,Javascript=400)
	print(my_dict)
```	

	3. 访问字典数据，使用key即可
	
	```python
	#dict构造器构造，参数为列表，列表元素为元组，元组元素只能是两个，一个为key，一个为value
	my_dict = dict([("Java",100,),("Python",120),("Javascipt",110)])
	print(my_dict)
	#dict构造器指定关键字创建字典，此时字段的key不允许使用表达式
	my_dict = dict(Java=200,Python=300,Javascript=400)
	print(my_dict)
	#数据访问 - 通过key 访问
	print("Java : ", my_dict['Java'])
```	

	4. 字典数据修改，如果key不存在，相当增加key-value对,如果存在，就是修改对应key的value值
	
```python
	my_dict = dict(Java=200,Python=300,Javascript=400)
	#修改value，如果key不存在，相当增加key-value对,如果存在，就是修改对应key的value值
	my_dict['Vue'] = 500
	print(my_dict)
	my_dict['Java'] = 900
	print(my_dict)
```
	
	5. 删除，通过del语句实现即可
	
```python
	my_dict = dict(Java=200,Python=300,Javascript=400)
	del my_dict['Vue']
	print(my_dict)
```

	6. 使用in, not in判断是否包含某一元素，只判断key就行了
	
```python
	my_dict = dict(Java=200,Python=300,Javascript=400)
	#判断是否存在某个key-value对
	print('Java' in my_dict)
	print('Vue' in my_dict)
	print('Vue' not in my_dict)
```

### 字典的高级用法

- 字典的常用方法

	1. clear()方法，清空所有的key-value对
	
```python
	#清空字典-clear()
	my_dict = dict(Java=200,Python=300,Javascript=400)
	print("Before clear : ", my_dict)
	my_dict.clear()
	print("After clear : ", my_dict)
```
	
	2. get()方法，根据key获取value(和方括号加key值效果一样)
	
```python
	#获取值-get()
	my_dict = dict([('Python',100),('Java',120),('Js',130)])
	print('Now the dictionary is : ', my_dict)
	print("Java value is :", my_dict.get('Java'))
```
	
	3. update()方法， 对于已经存在的key，就是更新value值，对于不存在的key，就是新增key-value
	
```python
	#字典更新-update():对于已经存在的key，就是更新value值，对于不存在的key，就是新增key-value
	#传值方式和构筑方法一致
	my_dict.update({'Python':140,'C':130})
	print("After update : ",my_dict)
	my_dict.update([('Java',100),('Vue',150)])
	print("After secondary update : ",my_dict)
	my_dict.update((('Java',300),('Vue',500)))
	print("After thirdly update : ",my_dict)
	my_dict.update(Java=1000,HTML=2000)
	print('After forth udpate : ',my_dict)
```

	4. 使用items()方法、keys(), values() 方法获取字典所有的键值对、键值、值
	
```python
	#遍历
	print('-' *80)
	for key, value in my_dict.items():
		print('Key is :',key, ', and value is :', value)
	print('-' *80)
	for item in my_dict.items():
		 print('Key is :',item[0], ', and value is :', item[1])
	print('-' *80)
	for key in my_dict.keys():
		print('Key is :',key, ', and value is :', my_dict.get(key))
		print('Key is :',key, ', and value is :', my_dict[key])
	print('-' *80)
	for value in my_dict.values():
		print("Value is : ", value)
	print('-' *80)
```

	5. setdefault()方法，获取某个key对应的值，如果存在对应key，则直接返回key对应的value，如果不存在，则会返回指定的default值，同时会将key-value加到字典中
	
```python
	#setdefault
	value = my_dict.setdefault('Java', 50)
	print("Value is : ",value)
	value = my_dict.setdefault('CSS', 400)
	print("Value is : ", value)
	print("Dictionary is :", my_dict)
```

	6. fromkeys()方法，用于将序列直接转换为字典，默认字典的value为None，也可以设置一个默认值，此方法也可作为创建字典的一种方法
	
```python
	#fromkeys
	print('-' *80)
	scores = dict.fromkeys(['Python','Java','HTML'])
	print(scores)
	scores = dict.fromkeys(['Python','Java','HTML'], 100)
	print(scores)
```

- 使用字典格式化字符串

```python
	#元组匹配 - 根据顺序匹配
	string = 'The book name is %s, and the price is : %10.2f'
	print(string %('Java',120))
	#字典格匹配 - 根据key匹配
	string = 'The book name is %(name)s, and the price is : %(price)10.2f'
	print(string %{'price':128,'name':'Python'})
```