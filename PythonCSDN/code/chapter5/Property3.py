#合成属性 - 使用@property装饰器
class Property:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
     
    @property    
    def size(self):
        return self.width, self.height
      
    @size.setter
    def size(self, size):
        self.width = size[0]
        self.height = size[1]
        
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