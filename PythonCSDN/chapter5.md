# Chapter5 - 面向对象

## 类与对象

- 类：类别，抽象性存在
	
	定义方式：

```python
		class 类名：
			执行语句
			零个或者多个变量
			零个或者多个方法
```
	
	1. Python属于动态语言，随时可以为类/实例增加类变量（只要对类/实例变量赋值，就是增加新的类变量）
	
	2. 类中定义的方法，默认就是实例方法
	
	3. 实例方法的第一个参数会被自动绑定到方法的调用者（该类的实例），因此这些实例方法应该至少定义一个参数，该参数通常会被命名为self
			
- 对象：是类的具体存在
	
	1. 构造方法
	
		1.1. 构造方法是一个特殊的方法，方法名为：__init__
		
		1.2. 创建对象时，自动调用构造方法
		
		1.3. 如果没有定义任何构造方法，Python会自动为该类定义一个只包含一个self参数的、默认的构造方法
		
```python
	#创建及使用对象
	class User:
		#构造方法就是初始化对象的实例变量
		def __init__(self, name='User',password='123456'):
			print('构造方法')
			self.name = name
			self.password = password
		def info():
			print('User name is : ', self.name, '\tPassword is : ', self.password)
	#空类使用pass即可        
	class Employee:
				pass
	#创建对象, 就是调用构造器
	print('-' * 80)
	user1 = User()    
	print(user1.name, user1.password)  
	print('-' * 80)
	user2 = User('Harry')  
	print(user2.name, user2.password)       
	print('-' * 80)
	user3 = User(password='12345678')
	print(user3.name, user3.password)  
	print('-' * 80)
	user4 = User(name='Jack',password='852369')
	print(user4.name, user4.password)  
	print('-' * 80)
```
	
	2. 创建对象
	
		直接创建对象，括号内访问参数即可
		
	3. 操作实例变量
	
		主要是对象实例变量的访问、添加、删除操作
	
```python
	class Item:
	def __init__(self,name='mouse'):
		self.name = name  
	print('-' * 80)   
	#访问变量
	item1 = Item('Displayer')
	print('Item name is : ', item1.name)
	print('-' * 80)  
	#设置变量   
	item1.name= 'Keyword'   
	print('Now item name is : ', item1.name)
	print('-' * 80)     
	#新增新变量
	item1.color = 'Red'
	print('Color is : ', item1.color)
	print('-' * 80)     
	#删除实例变量
	del item1.color
	#color属性已删除，以下输出会报错
	#print('Color is : ', item1.color)
	print('-' * 80)   
```
	
	4. 操作方法
	
```python
	#调用类实例方法
	class Item:
		def info(self):
			print('info')
	#调用方法    
	print('-' * 80)    
	item = Item()
	item.info()		
	print('-' * 80)
	#新增方法
	def newFun(self):
		print('New method')
	item.foo = newFun  
	#注意：新增的方法不会自动绑定self的，需要手动绑定调用
	item.foo(item)  
	print('-' * 80) 
	#新增方式二：使用MethodType将函数包装成实例方法
	from types import MethodType
	item.bar = MethodType(newFun, item)
	item.bar()
	print('-' * 80) 
	#删除新增的方法
	del item.bar
	#以下调用会报错，bar()方法已不存在了
	#item.bar()
	print('-' * 80) 
```	
	
- 实例方法与自动绑定

	1. 使用对象调用方法是，Python会自动绑定方法的第一个参数（通常建议参数名命名为：self）
	
	2. 根据第一个参数出现的位置的不同，第一个参数所绑定的对象略有区别
	
		2.1. 在构造方法中引用该构造方法正在初始化的对象
		
		2.2. 在普通实例方法中引用调用该方法的对象
		
```python
	#实例方法与自动绑定
	class User:
		def __init__(self,name='Tiger'):
			#此处的self代表该构造器正在构造的对象
			self.name = name     
	print('-' * 80)          
	#User构造的对象赋值给u，在User构造器的self实际就是代表u
	u = User()
	print('User Name : ', u.name) 
	print('-' * 80)
	u2 = User('Scott')
	print('User Name : ', u2.name) 
	print('-' * 80)
```

	3. 类中的方法调用其他类中其他的方法时，self不可省略
	
```python
	#类的一个方法调用另外一个方法
	class Dog:
		
		def run(self):
			#类中的方法调用其他类中其他的方法时，self不可省略
			self.jump()
			print('Dog is running!')
			
		def jump(self):
			print('Dog is jumping!')
			
	print('-' * 80)    
	dog = Dog()
	dog.run() 
	print('-' * 80)    
```

	4. self方法可以当做实例方法的返回值，把self参数作为返回值，则可以多次连续调用该方法

```python
	#返回self参数
	class Plant:
		
		def __init__(self, height=2):
			self.height = height
			
		def grow(self):
			self.height += 10
			return self
			
	p = Plant(10)
	p.grow().grow().grow()
	print(p.height)    
```

- 类调用实例方法

```python
	#类调用实例方法
	class Role:
		def test(self):
			print('Test method')
	#test方法本身是实例方法，应该有对象调用
	#但是Python允许类调用实例方法，此时就变成了'未绑定的方法',因此必须手动传入self参数
	r = Role()
	Role.test(r)      
```
## 类方法与静态方法

- 类方法定义

	1. 是有@classmethod修饰
	
	2. 方法的第一个参数定义为cls，用类调用该方法的时候该参数会自动绑定。
	
```python
	#类方法
	class Tiger:
		#1. 使用@classmethod修饰 2. 绑定cls变量
		@classmethod
		def info(cls):
			print('info method')
			print(cls)
	print('-' * 80)
	print(Tiger)
	Tiger.info()
	print('-' * 80)
	#对象调用类方法就相当于类调用，同样也会自动绑定
	t = Tiger()
	t.info()
	print('-' * 80)
```
	
- 静态方法

	1. 使用@staticmethod修饰
	
	2. 对方法参数没有要求，无论如何都不会自动绑定
	
```python
	#静态方法
class Pig:	
	@staticmethod
	def eat(food):
		print('The food is : ', food)
	print('-' * 80)	
	Pig.eat('grass')
	print('-' * 80)
```

| 操作方式 | 实例方法 | 类方法 | 静态方法 |
| --- | --- | ---- | ---- |
| 对象调用  | 自动绑定 | 自动绑定 | 不自动绑定|
| 类调用 | 不自动绑定 | 自动绑定 | 不自动绑定 |