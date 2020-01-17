#Review Chapter 5
#创建类
class User:
	
	def __init__(self, name='Jack',pwd='123456'):
		self.name = name
		self.pwd = pwd
		
	def info(self):
		print('Name : %s , password : %s' %(self.name, self.pwd))
        
print('-' * 80)
user = User()
user.info()
print('-' * 80)
user = User('Sam')
user.info()
print('-' * 80)
user = User('Harry', '12345678')
user.info()
print('-' * 80)
user = User(pwd='4566789')
user.info()
print('-' * 80)
user = User(pwd='526341',name='Tom')
user.info()
#修改实例变量
print('-' * 80)
user = User(pwd='526341',name='User1')
user.info()
user.name = 'User2'
user.info()
#新增变量
user.address = 'SD YT'
print(user.address)
#删除变量
del user.address
#以下输出报错
#print(user.address)
print('-' * 80)
#新增方法一：直接新增
def newFunc(self):
    print('This is a new Method...')
user.hi = newFunc
#新增方法不会自动绑定self实例，需要手动绑定
user.hi(user)    
print('-' * 80)
#新增方式二：使用MethodType将方法包装成实例方法
def newFunc2(self):
    print('This is another new method : ', self.name)
from types import MethodType
user.hello = MethodType(newFunc2, user)
user.hello()
print('-' * 80)
#类中的方法调用其他方法时，self不可省略
class Dog:
    
    def run(self):
        self.jump()
        print('Dog is running...')
        
    def jump(self):
        print('Dog is jumping...')
        
dog = Dog()
dog.run()
print('-' * 80)     
#self可以作为实例方法的返回值，把self参数作为实例方法的返回值，则可以多次连续调用该方法
class Plant:

    def __init__(self, height=2):
        self.height = height
        
    def grow(self):
        self.height += 2
        return self
        
plant = Plant(1.5)
plant.grow().grow().grow()
print('Now the plant height is : ', plant.height,'(m)')       
print('-' * 80)
#类调用实例方法
class Role:
    
    def info(self):
        print('Role info ...')
        
r = Role()
r.info()
#类调用实例方法，此时就变成了‘未绑定方法’，self参数必须手动传入
Role.info(r)        
print('-' * 80)
#类方法 - 1. @classmethod， 2. 方法的第一个参数定义为cls
class Tiger:
    @classmethod
    def info(cls):
        print('class method...')
        print(cls)
        
Tiger.info()    
#对象调用类方法等同于类调用，同样也会自动绑定
t = Tiger()
t.info()
print('-' * 80)
#静态方法 - @staticmethod 方法参数没有要求

class Pig:

    @staticmethod
    def eat(food):
        print('The pig is eating : ', food)

p = Pig()
p.eat('grass')
print('-' * 80)
#函数装饰器
def foo(fn):
    print('foo function')
    print(fn)
    print('PythonFunction')
    
@foo    
def bar():
        print('bar function')
    
    
print(bar)
print('-' * 80)
foo(bar)
print('-' * 80)