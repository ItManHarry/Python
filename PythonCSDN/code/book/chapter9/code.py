#Python模块和包
#import sys
#print(sys.argv[0])
from sys import argv as v, winver as w
print(v[0])
print(w)
import Model1 as m1
print(m1.my_book)
print(m1.say_hi('Jack'))
u = m1.User('Harry')
print(u)
u.walk()
from all_module import *
hello()
world()
'''
    以下方法报错，hi方法不在__all__数组中
'''
#hi()