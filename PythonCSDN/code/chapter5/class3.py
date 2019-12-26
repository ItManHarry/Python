#操作实例变量
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