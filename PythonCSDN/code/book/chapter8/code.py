#Python类的特殊方法
#__repr__()方法
'''
    类的自我描述，类似java的toString()方法
'''
class Apple:
    def __init__(self, color,weight):
        self.color = color
        self.weight = weight
        
    def __repr__(self):
        return "Apple[color="+self.color+",weight="+str(self.weight)+"]"
a = Apple('Red', 4.56)        
print(a)
#析构方法 __del__ 
'''
    说明：
    1. 对一个变量执行del操作，该变量所引用的对象不一定会被回收!
    只有当对象的引用计数变为0时，该对象才会被回收。因此，如果一个对象
    有多个变量引用它，那么del其中的一个对象是不会回收该对象的。
    2. 如果父类提供了__del__()方法，则系统重写__del__()时必须显式调用父类的
    __del__()方法，这样才能保证合理地回收父类实例的部分属性
'''    
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def __del__(self):
        print('对象已删除！')
        
im = Item('鼠标', 26.5)        
x = im
del im
print('-------------')
#__dir__方法
'''
    列出对象内部的所有属性（包括方法）名，该方法返回包含所有属性（方法）名
    的序列。
'''
im2 = Item('鼠标', 26.5)  
print(im2.__dir__())
print(dir(im2))
#__dict__属性
'''
    用于查看对象内部存储的所有属性名和属性值组成 的字典，通常程序直接调用
    该属性即可。
'''
print(im2.__dict__)
print(im2.__dict__['name'])
print(im2.__dict__['price'])
im2.__dict__['name'] = '键盘'
im2.__dict__['price'] = 52.9
print(im2.name)
print(im2.price)
#__getattr__, __setattr__等
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def __setattr__(self, name, value):
        print('------set %s ------' %name)
        if name == 'size':
            self.width, self.height = value
        else:
            self.__dict__[name] = value
    def __getattr__(self, name):
        print('------get %s ------' %name)
        if name == 'size':
            return self.width, self.height
        else:
            raise AttributeError
            
    def __delattr__(self, name):
        print('------del %s ------' %name)
        if name == 'size':
            self.__dict__['width'] = 0
            self.__dict__['height'] = 0
            
rect = Rectangle(3,4)            
print(rect.size)
rect.size = 6,8
print(rect.size)
del rect.size
print(rect.size)
#反射相关的方法
