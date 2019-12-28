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


## 函数装饰器

- @staticmethod和@classmethod的本质就是函数装饰器

- staticmethod和classmethod都是Python内置的函数

- 使用@符号引用已有的函数，可以修饰其他函数

- 当程序使用“@函数”（比如函数A）装饰另一个函数（比如函数B）时，实际完成以下两步：

	1. 将被修饰的函数（函数B）作为参数传给@符号引用的函数（函数A）
	
	2. 将函数B替换（装饰）成第一步的返回值
	
```python
	#函数装饰器
	def foo(fn):
		print('function foo')
		print(fn)
		return 'PythonProgramming'
		
	@foo
	def bar():
		print('function bar')
	print('-' * 80)
	print(bar)
	print('-' * 80)
	foo(bar)
```	

	3. 函数装饰器与AOP
	
```python
	#函数装饰器与AOP
	def foo(fn):
		print('function foo')
		def aspect(*args):
			print('before function execution...')
			fn(*args)
			print('after function execution...')
		return aspect
		
	@foo
	def bar(a,b):
		print('function bar')
		print('a is : ', a)
		print('b is : ', b)
	print('-' *80)
	bar(10,20)
	print('-' * 80)
```

## 类变量与实例变量

- 类变量：在类空间或通过类引用赋值的变量

- 实例变量：通过对象引用或self引用赋值的变量

- 通过类可以获取、修改类变量

- 通过对象只可以获取类变量的值，不能修改类变量的值

- 如果试图通过实例设置类变量，其结果就是新增了实例变量

```python
	#类变量与实力变量
	class ClassA:
		v1 = 'variable1'
		
		def __init__(self, name, age):
			self.name = name
			self.age = age
			
	ClassA.type = 'class type'
	print('-' * 80)
	print('Class Variable 1 : ', ClassA.v1)
	print('Class Variable 2 : ', ClassA.type)
	print('-' * 80)
	#实例只能访问类变量
	ca = ClassA('Jack',36)
	print('Class Variable 1 : ', ca.v1)
	print('Class Variable 2 : ', ca.type)
	#如果试图通过实例设置类变量，其结果就是新增了实例变量
	ca.v1 = 'ca v1'
	print(ca.v1)
	print(ClassA.v1)
	print('-' * 80)
```

- 使用property合成属性（相当于实例变量）

- property(fget=None,fset=None,fdel=None,doc=None)

- 使用property()函数合成属性时，也可根据需要只传入少量参数，如合成只读属性就无需设置fget参数

	1. 使用property方法

```python
	#属性合成器property 
	class Rectangle:
		
		def __init__(self, w, h):
			self.w = w
			self.h = h
			
		def getarea(self):
			return self.w * self.h
		#合成area属性	
		area = property(fget=getarea,doc='get rectangle area')
		
		def setsize(self,size):
			self.w = size[0]
			self.h = size[1]
			
		def getsize(self):
			return self.w, self.h
			
		#合成size属性
		size = property(fget=getsize, fset=setsize, doc='get rectangle size')
		
	print('-' * 80)
	r = Rectangle(10, 5)
	print('Rectangle area is : ', r.area)	
	print('Rectangle size is : ', r.size)
	print('-' * 80)	
```

	2. 使用@property装饰器
	
```python
	#合成属性
	class Property:
		
		def __init__(self, width, height):
			self.width = width
			self.height = height
		 
		@property    
		def size(self):
			return self.width, self.height
		  
		@size.setter
		def size(self, size):
			self.width = size[0]
			self.height = size[1]
			
		def info(self):
			print('Width is : ', self.width, '\theight is : ', self.height)
			
	p = Property(40,20)
	print('-' * 80)
	p.info()
	print('init size is : \t', p.size)
	#设置size
	p.size = (50,25)
	print('set size : \t', p.size)
	print('-' * 80)
```

## 隐藏与封装

- 隐藏机制

	规定：凡是以双下划线开头的，Python都会把他们隐藏起来
	
	1. 将实例变量、工具方法名以双下划线开头，就实现了隐藏：隐藏的目的就是保证对象的完整性
	
	2. 提供方法（默认暴露）来操作实例变量
	
```python
	#隐藏与封装
	class SystemUser:
		
		def __init__(self, name='Noname',passwd='default'):
			if isinstance(name, str) and 4 <= len(name) <= 8:
				self.__name = name
			else:
				self.__name = 'Noname'
			if isinstance(passwd, str) and 4 <= len(passwd) <= 8:
				self.__passwd = passwd
        else:
            self.__passwd = 'default'
			
		def setName(self, name):
			if isinstance(name, str) and 4 <= len(name) <= 8:
				self.__name = name
			else:
				print('用户名无效')
				
		def getName(self):
			return self.__name
			
		name = property(fget=getName,fset=setName)
		
		def setPasswd(self, passwd):
			if isinstance(passwd, str) and 4 <= len(passwd) <= 8:
				self.__passwd = passwd
			else:
				print('密码无效')
				
		def getPasswd(self):
			return self.__passwd
			
		passwd = property(fget=getPasswd,fset=setPasswd)
		
	print('-' * 80)    
	u = SystemUser()
	u.name = '123'
	u.passwd = '123'
	print('User name : ', u.name)   
	print('User passed : ', u.passwd)   
	u.name = 'Guoqian'
	u.passwd = 'Jack'
	print('User name : ', u.name) 
	print('User passed : ', u.passwd)
	print('-' * 80)   
```