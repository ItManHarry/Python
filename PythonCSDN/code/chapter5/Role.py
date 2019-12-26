#类调用实例方法
class Role:
	def test(self):
		print('Test method')
#test方法本身是实例方法，应该有对象调用
#但是Python允许类调用实例方法，此时就变成了'未绑定的方法',因此必须手动传入self参数
r = Role()
Role.test(r)        