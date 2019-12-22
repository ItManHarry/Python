# Chapter4

## 函数

	声明方式：
	
```python
	def 函数名(参数列表):
		//由零条到多条可执行性语句组成的函数
		[return [返回值]]
```	

## 关键数参数和参数默认值

	函数参数传入方式：
		
	1. 通过位置传入

```python
	def info(name, age, height):
    print('Name : ', name)
    print('Age : ', age)
    print('Height : ', height)
	info('ChengGuoqian',36,170) 
```
	
	2. 通过参数名传入（命名参数-关键字参数）
	
```python
	def info(name, age, height):
    print('Name : ', name)
    print('Age : ', age)
    print('Height : ', height)
	info(age=36,name='Harry',height=168)
```

	3. 参数默认值 
	
		3.1. 带默认值的参数要放在后面		
		
```python
	def info(age, height,name='ABC'):
    print('Name : ', name)
    print('Age : ', age)
    print('Height : ', height)
	info(age=36,height=168)
```

		3.2. 如果省略第一个参数值，需要指定后面的关键字进行传值
		
```python
	def welcome(name="Harry", message="Welcome to the Python world."):
    print(name,',', message)
	welcome('Jack')
	welcome(message='change yourself for the future!')
```

## 参数收集与逆向参数收集

- 参数收集

	在形参前面加一个"\*"这样就意味着这个参数可以接受多个参数值,多个参数值被当做元组传入：参数收集的本质就是一个元组。
	
	1. Python允许可变参数位于形参列表的任意位置，但是只允许有一个支持“普通”参数收集的形参
	
```python
	def test(num, *books):
    print("Number : ", num)
    print("Books : ", books)
	test(100, 'Java','Python','C#') 
```	
	
	2. 如果支持“普通”参数收集的形参位于前面，后面的参数则需要使用关键字进行传入
	
```python
	def info2(*names, message):
    for name in names:
        print('%s, %s' %(name, message))
	info2('A','B','C','D',message=' welcome you .')   
```	

	3. 在参数前面加2个星号， 该参数支持关键字参数收集，收集的参数被当做dict处理（一个函数可同时支持普通参数收集和关键字参数收集）
	
```python
	def info4(num,*names, **scores):
    print('Number : ', num)
    print("Names : ", names)
    print('Scores : ', scores)
	info4(30,'Java','Python','C#', js=100,ps=120,cs=150)  
	print('-' * 50)
	def info5(*names, message, **scores):
		print('Message : ', message)
		print("Names : ", names)
		print('Scores : ', scores)
	#关键字参数只收集没有明确定义的关键字参数
	info5('a','b','c',js=100,ps=120,cs=150,message='OK')  
```	
	
- 逆向参数收集

	指的是Python的解包，将元组或者列表或者参数前面加一个星号，函数即可解包。将字典参数前面加两个星号，函数即可自动解包
	
```python
	print('-' * 50)
	def info6(a,b):
		print('a is : ', a)
		print('b is : ', b)
	vs1 = (100, 200)
	vs2 = ['Python','Java']    
	vs3 = {'a':300,'b':400}
	info6(*vs1)
	print('-' * 50)
	info6(*vs2)
	print('-' * 50)
	info6(**vs3) 
```