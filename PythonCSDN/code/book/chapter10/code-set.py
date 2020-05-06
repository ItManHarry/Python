#set集合
#创建方式一:{}直接创建
print('-' * 80)
set1 = {'a','b','c',34,(10,20,30)}
#添加元素
set1.add('Harry')
set1.add('Jack')
set1.add('Python')
print('Set 1 length is : ', len(set1))
for e in set1:
    print('Element : ' , e)
#删除元素
set1.remove(34)
#如果删除不存在的元素，程序报错Keyerror,但是使用discard方法不会报错
#set1.remove(88)
set1.discard(99)
print('Now the set length is : ', len(set1))
#判断元素是否在set中
print('JJJ is in set ? ', 'JJJ' in set1)
print('-' * 80)
#创建方式二：使用set()函数创建
set2 = set()
#添加元素 - 添加的元素只能是不可变元素，列表/字典是不可以添加的
#以下添加会报错（TypeError: unhashable type: 'list'）
#set2.add([1,2,3,4])
#set2.add({"OK":200,"NOTFOUND":404})
set2.add('Java')
set2.add(123)
set2.add((10,20,30))
set2.add('''
    This is a 
    multyline
    text
''')
set2.add('Python')
print('Set2 length is : ', len(set2))
for e in set2:
    print('Element : ', e)
print('-' * 80)
#子集合判断：issubset或<=
print('set1 is subset of set2 ? ', set1.issubset(set2))
print('set1 is subset of set2 ? ', set1 <= set2)
print('-' * 80)
#父集合判断：issuperset或>=
print('set1 is superset of set2 ? ', set1.issuperset(set2))
print('set1 is superset of set2 ? ', set1 >= set2)
print('-' * 80)
#set1和set2相减：difference或-号，此时set1不受影响
print('set1 : ', set1)
set3 = set1 - set2
print('set1 after - operation :: ', set1)
set4 = set1.difference(set2)
print('set1 after difference operation : ', set1)
print('set2 : ', set2)
print('set1 - set2(use - ) : ', set3)
print('set1 - set2(use difference) : ', set4)
#使用difference_update会改变set1，此方法为void方法。即：差异后的set赋给了set1，此处set5为空
set5 = set1.difference_update(set2)
print('set1 - set2(use difference_update) : ', set5)
print('set1 : ', set1)
print('-' * 80)
print('Now set1 is : ', set1)
print('Now set2 is : ', set2)
set1.add('Java')
set1.add('Python')