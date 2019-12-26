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