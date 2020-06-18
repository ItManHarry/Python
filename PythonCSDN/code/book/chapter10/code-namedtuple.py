from collections import namedtuple
print('-' * 80)
#定义命名元组类
Point  = namedtuple('Point',['x','y'])
#初始化Point对象，即可用位置参数，也可用命名参数
p = Point(11, y = 12)
#普通元组方式访问元素
print('Element 0 : ', p[0], ', Element 1 : ',  p[1])
print('-' * 80)
#执行解包
x,y = p
print('x is : ', x, 'y is : ', y)
print('-' * 80)
#根据字段名访问元素
print('Element x : ', p.x, ', Element y : ',  p.y)
print(p)
print('-' * 80)
#data
data = ['East','North']
p = Point._make(data)
print(p)
print('-' * 80)
#转化为orderedDict
print(p._asdict())
print('-' * 80)
#更改某个元素值
p._replace(y='South')
print(p._replace(y='South'))
print('-' * 80)
Color = namedtuple('Color', ['red','green','blue'])
Pixel = namedtuple('Pixel', Point._fields+Color._fields)
p = Pixel(11,12,255,119,128)
print(p)
print('-' * 80)