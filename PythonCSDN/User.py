#实例方法与自动绑定
class User:
	def __init__(self,name='Tiger'):
		#此处的self代表该构造器正在构造的对象
		self.name = name
#User构造的对象赋值给u，在User构造器的self实际就是代表u
u = User()
print('User Name : ', u.name)        