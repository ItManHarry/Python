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
'''
    导入包
    1. 包的创建
        1.1. 创建一文件夹
        1.2. 编写__init__.py文件    
'''
import self_package1
print('=' * 80)
print(self_package1.__doc__)
print(type(self_package1))
print(self_package1)
print('=' * 80)
'''
    导入包下的各个模块，此时没有编辑__init__.py文件
'''
'''
import fk_package
import fk_package.print_shape
from fk_package import billing
import fk_package.arithmetic_chart
fk_package.print_shape.print_blank_triangle(5)
im = billing.Item(4.5)
print(im)
fk_package.arithmetic_chart.print_multiple_chart(5)
'''
'''
    导入包下的各个模块，此时编辑__init__.py文件,__init__.py文件内容如下：
    from . import print_shape
    from .print_shape import *
    from . import billing
    from .billing import *
    from . import arithmetic_chart
    from .arithmetic_chart import *
'''
import fk_package as fp
fp.print_blank_triangle(5)
im = fp.Item(4.5)
print(im)
fp.print_multiple_chart(5)
'''
    查看模块内容的方法如下：
    1. 使用dir()函数，但是这个会包含大量以下划线打头的程序单元，可以使用列表推导式是进行过滤
    >>> import string
    >>> [e for e in dir(string) if not e.startswith('_')]
    2. 使用模块本身提供的__all__变量进行查看即可
    >>> import string
    >>> string.__all__
    使用__doc__属性查看文档
    >>> print(string.capwords__doc__)
    使用__file__查看源文件路径
    >>>string__file__
'''