#合成属性 - 使用property函数
class Property:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def setSize(self, size):
        self.width = size[0]
        self.height = size[1]
        
    def getSize(self):
        return self.width, self.height
        
    #合成size属性
    
    size = property(fset=setSize,fget=getSize,doc='size property')
        
    def info(self):
        print('Width is : ', self.width, '\theight is : ', self.height)
        
p = Property(40,20)
print('-' * 80)
p.info()
print('init size is : \t', p.size)
#设置size
p.size = (50,25)
print('set size : \t', p.size)
print('-' * 80)