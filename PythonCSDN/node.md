# Python基础

## 变量

- Python变量无需提前声明，可以随时声明使用

- Python变量类型可变

### 字符串

- 字符串的基础用法

	1. 字符串可包含任何字符
	
	2. 即可单引号也可双引号	
	

- 字符串拼接

	1. 使用“+”拼接
	
	2. 使用str()或者repr()函数进行转换
	
	3. repr()会以Python表达式的形式来表示值
	
	
- 使用input()向用户生成一条提示，然后获取用户输入内容（Python2使用的是raw_input()）

- 长字符串与原始字符串

	1.  三引号（单双都可以）表示长字符串
	
	2. 原始字符串以r开头，原始字符串不会把反斜线当做成特殊字符
	
	3. 如果原始字符串包含引号，同样需要进行转义

- 字节串和字符串

	1. 字符串有多个字符组成，字节串有多个字节组成
	
	2. 字节串和字符串除了操作的数据单元不同，他们所支持的方法基本相同，字节串也是不可变序列
	
	
	3. 字符串和字节串相互转换（三种方式）
	
		3.1.  如果字符串内容都是ASCII字符，在字符在前面加b前缀即可构建字节串
		
		3.2. 使用bytes()函数将字符串转换为字节串
		
		3.3. 使用encode()函数将字符串转换为字节串
		
		3.4 调用bytes对象的decode()方法将bytes对象解码成字符串
- 字符串的高级用法

	1. 转义字符
	
		\b 退格符
		\n 换行符
		\r 回车符
		\t 制表符
		\" 双引号
		\' 单引号
		\\ 反斜线		
	
	2. 字符串格式化
	
		使用%加上转换说明符实现字符串格式化， Python转换说明符如下：
		
			d,i 	转换为带符号的十进制整数
			
			o  	转换为带符号的八进制整数
			
			x,X	转换为带符号的十六进制整数
			
			e,E	转换为科学计数法表示的浮点数
			
			f,F		转换为十进制的浮点数
			
			g		智能选择f或e格式
			
			G 		智能选择F或E格式
			
			C		转换为单字符（只接受整数或单字符字符串）
			
			r		使用repr()将变量或者表达式转换为字符串
			
			s		使用str()将变量或者表达式转换为字符串
	
	3. 调用函数操作字符串
	
		3.1. 基于索引的计算
		
		3.2. in运算
		
		3.3. len()运算
		
		3.4. min()/max()函数
		
		3.5. title()方法：将字符串的首字母大写
		
		3.6. lower() 方法：将字符串小写
		
		3.7. upper()方法：将字符串大写
		
		3.8. strip()方法：去除前后的空格
		
		3.9. lstrip()方法：去除前端的空格
		
		3.10. rstrip()方法：去除后面的空格
		
		3.11. startwith()方法：是否某个字符打头
		
		3.12. endswith()方法：是否某个字符结尾
		
		3.13. find()方法：查找字符是否存在，找到返回index值，否则返回-1
		
		3.14. index() 方法：查找字符是否存在，找到返回index值，否则报ValueError
		
		3.15. replace()方法：使用指定的字符串替换字符串中的目标字符
		
		3.16. translate()方法：使用指定的翻译映射表对字符串进行替换
		
		3.17. split()方法：分割字符串
		
		3.18. join()方法：连接字符串
		
## 运算符

- 赋值运算符及扩展的赋值运算符

	1. “=”赋值	

- 算数运算符

	1. +，-，*，/，//(整除)，%，**
	
	2. 复杂的数学运算需要导入math模块
	
	3. 扩展运算符
	
		3.1. += : x += y(x = x + y)
		3.2 -= : x -= y(x = x - y)
		3.3. *= : x *= y(x = x * y)
		3.4. /= : x /= y(x = x / y)
		3.5. //= : x //= y(x = x // y)
		3.6. %= : x %= y(x = x % y)
		3.7. **= : x **= y(x = x ** y)

- 索引运算符

	1. 索引运算符就是方括号
	
	2. 方括号中可以使用单个索引值，访问单个元素
	
	3. 方括号也可以使用索引范围，还可以设置步长
	
	4. 索引运算符适用于所有的序列（字符串、字节串、列表、元组等）
	
- 比较运算符和逻辑运算符
	
	1. >, >= : 大于，大于等于
	
	2. <, <= : 小于，小于等于
	
	3. == : 等于
	
	4. != : 不等于
	
	5. is(is not) : 判断两个变量的引用对象是否相同（不相同），如果相同（不相同）则返回True， 否则返回False
	
	6. and : 与，任一操作数为False，返回便是False
	
	7. or : 或，任一操作为为True，返回便是True
	
	8. not : 非，操作数为False，返回True，操作数为True，返回False
	
- 三目运算符

	Python用if来代替三目运算符
	
	语法： True_Statements if expression else Else_Statements
	
```python	
	age = 25
	print('age bigger than 25' if age > 25 else print('age less than 25'))
```

	if支持嵌套
	
	
	注：True_Statements可以放置多个语句，如果用“,”号隔开，则返回多个语句返回值组合的元组，如果用“;”号隔开，则返回第一条语句返回的值
	
```python	
	age = 25
	s = print("比25大"), "成年人" if  age > 25 else print('小于或者等于25')
	print(s)
``` 
	
- in运算符

	判断一个元素是否在序列之中
	
	
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
	
	注意：列表只能和列表相加、元组只能和元组相加。如果列表加元组，需要视图list函数将元组转换为列表后再相加
	
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

	6. fromkeys()方法，用于将字典直接转换为字典，默认字典的value为None，也可以设置一个默认值，此方法也可作为创建字典的一种方法
	
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