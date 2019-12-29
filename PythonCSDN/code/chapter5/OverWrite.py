#重写父类方法
class Bird:
	
	def fly(self):
		print('bird fly ...')
		
class Ostich(Bird):

	def fly(self):
		print('I can not fly , I can only run...')
		
print('-' * 80)
ostich = Ostich()
ostich.fly()
print('-' * 80)