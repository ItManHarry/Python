#调用被复写的父类方法
class Employee:
	
	def work(self):
		print('work hard 996...')
		
class Manager(Employee):
	
	def work(self):
		print('work much harder...')
		
	def relax(self):
		print('still work while relaxing...')
        #默认调用复写后的方法
		#self.work()
        #如果此处希望调用父类被重写的方法，可以使用未绑定方法来调用，类名调用方法，未绑定方法，因此需要显示传入一个self参数
		Employee.work(self)
print('-' * 80)
m = Manager()
m.relax()
print('-' * 80)