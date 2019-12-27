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