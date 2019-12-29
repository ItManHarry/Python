#继承
class Fruit:
	
	def info(self):
		print('fruit is good to health...')
		
class Apple(Fruit):
	pass
	
print('-' * 80)
apple = Apple()
apple.info()
print('-' * 80)