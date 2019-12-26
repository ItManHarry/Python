#实例方法与自动绑定
class User:
    def __init__(self, name='Jack'):
        self.name = name
        
    def info(self):
        print('OK\t', self.name)
        
#实例化User对象
u1 = User()
u1.info()      
u2 = User('Tom')
u2.info()  
u2.info()  