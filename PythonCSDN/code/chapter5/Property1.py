#属性合成器property
class Rectangle:
	
	def __init__(self, w, h):
		self.w = w
		self.h = h
		
	def getarea(self):
		return self.w * self.h
	#合成area属性	
	area = property(fget=getarea,doc='get rectangle area')
	
    def setsize(self,size):
        self.w = size[0]
        self.h = size[1]
        
    def getsize(self):
        return self.w, self.h
        
    #合成size属性
    size = property(fget=getsize, fset=setsize, doc='get rectangle size')
    
print('-' * 80)
r = Rectangle(10, 5)
print('Rectangle area is : ', r.area)	
print('Rectangle size is : ', r.size)
print('-' * 80)	