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
	
	