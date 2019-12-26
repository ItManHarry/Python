#静态方法
class Pig:	
	@staticmethod
	def eat(food):
		print('The food is : ', food)
print('-' * 80)	
Pig.eat('grass')
print('-' * 80)