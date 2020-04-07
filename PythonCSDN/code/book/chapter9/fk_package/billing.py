'''
	定义Item类
'''
class Item:
	def __init__(self, price):
		self.price = price
	def __repr__(self):
		return 'Item[price=%g]' %self.price