class Person:
	
	def __init__(self, age):
		if age > 30 or age < 10:
			raise #RuntimeError异常
		self.__age = age
		
	def setage(self, age):
		#要求年龄必须在10-30之间
		if age > 30 or age < 10:
			#raise                                                                                  #情况一：RuntimeError异常
            #raise ValueError                                                              #情况二：引发指定类的默认异常对象
            raise ValueError(age, '年龄必须介于10-30之间')          #情况三：引发异常对象
		self.__age = age
		
	def getage(self):
		return self.__age
		
	age = property(fget=getage,fset=setage)
    
person = Person(25)
print(person.age)
person.age = 45
print(person.age)