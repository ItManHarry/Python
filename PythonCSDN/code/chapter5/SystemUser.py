#隐藏与封装
class SystemUser:
	
	def __init__(self, name='Noname',passwd='default'):
		self.__name = name
		self.__passwd = passwd
		
	def setName(self, name):
		if isinstance(name, str) and 4 <= len(name) <= 8:
			self.__name = name
		else:
			print('用户名无效')
			
	def getName(self):
		return self.__name
		
	name = property(fget=getName,fset=setName)
	
	def setPasswd(self, passwd):
		if isinstance(passwd, str) and 4 <= len(passwd) <= 8:
			self.__passwd = passwd
		else:
			print('密码无效')
			
	def getPasswd(self):
		return self.__passwd
		
	passwd = property(fget=getPasswd,fset=setPasswd)
    
print('-' * 80)    
u = SystemUser()
u.name = '123'
u.passwd = '123'
print('User name : ', u.name)   
print('User passed : ', u.passwd)   
u.name = 'Guoqian'
u.passwd = 'Jack'
print('User name : ', u.name) 
print('User passed : ', u.passwd)
print('-' * 80)   

class BizUser(SystemUser):
    pass
    
print('-' * 80)
bizUser = BizUser()
print('', bizUser.name)
print('', bizUser.passwd)
print('-' * 80)