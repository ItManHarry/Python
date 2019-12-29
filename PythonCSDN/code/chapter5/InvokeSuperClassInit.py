#调用父类的构造器
class Employee:
	
	def __init__(self, salary):
		self.salary = salary * 1.8
		
class Manager(Employee):
	
	def __init__(self, salary, title):
        #当子类的初始化操作和父类的初始化操作相同时，
        #我们不应该直接复制父类的初始化代码，这样不利于后期项目的升级
        #因此，此处需要调用父类的构造方法
        #方式一：使用未绑定方式调用
		Employee.__init__(self, salary) 
		self.title = title
		
m = Manager(8000, 'Manager')
print(m.salary)
print(m.title)