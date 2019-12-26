#调用类实例方法
class Item:
	def info(self):
		print('info')
#调用方法    
print('-' * 80)    
item = Item()
item.info()		
print('-' * 80)
#新增方法
def newFun(self):
    print('New method')
item.foo = newFun  
#注意：新增的方法不会自动绑定self的，需要手动绑定调用
item.foo(item)  
print('-' * 80) 
#新增方式二：使用MethodType将函数包装成实例方法
from types import MethodType
item.bar = MethodType(newFun, item)
item.bar()
print('-' * 80) 
#删除新增的方法
del item.bar
#以下调用会报错，bar()方法已不存在了
#item.bar()
print('-' * 80) 