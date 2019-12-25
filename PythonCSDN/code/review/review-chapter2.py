#Review
#列表、元组(两者的区别就是列表元素可以修改，元组元素不可修改)
print('' * 100)
v_list = [1,2,3,'Java',3.14,"Python"]
v_tuple = (10,20,30,'Harry',40,50)
print('List : ', v_list)
print('Tuple : ', v_tuple)
v_list = list(range(1,10))
v_tuple = tuple(range(5,15))
print('' * 100)
print('Now the list is : ', v_list)
print('Now the tuple is : ', v_tuple)
print('' * 100)
#通过索引访问列表及元组
for i in range(len(v_list)):
    print('Index is : ', i, ' element is : ', v_list[i])
print('-' * 100)
#某个下标对应的值
print('List index 4 , element is : ', v_list[4])    
print('Tuple index 4 , element is : ', v_tuple[4])  
print('-' * 100) 
#包含前面的下标值，不包含后面的下标值    
print('List elements 3 - 5 : ', v_list[3:5])
print('Tuple Elements 3 - 5 : ', v_tuple[3:5])
print('-' * 100)
#带有步长的列表取值范围
print('List elements 1 - 10 , every two : ', v_list[1:10:2])
print('Tuple elements 1 - 10 , every two : ', v_tuple[1:10:2])
print('-' * 100)
#列表、元组相加 - 只是元素的总和
#列表只能和列表相加、元组只能和元组相加。如果列表加元组，需要使用list函数将元组转换为列表后再相加
v_list1 = [1,2,3]
v_list2 = ['a',b'','c']
v_list_sum = v_list1 + v_list2
print('List 1 : ', v_list1)
print('List 2 : ', v_list2)
print('List sum : ', v_list_sum)
print('-' * 100)
#列表相乘，只是元素重复对应的倍数，字符串也支持翻倍
print('List1 : ', v_list1)
print('List1 * 3 : ', v_list1 * 3)
v_str = 'abc'
print('String : ', v_str)
print('String * 3 : ', v_str * 3)
#序列相关函数
print('-' * 100)
#len()序列长度
print('List 1 : ', v_list1)
print('List1 length : ', len(v_list1))
#max/min函数
print('Max element of list1', max(v_list1))
print('Min element of list1', min(v_list1))
print('-' * 100)
#封包，将多个值付给一个变量，Python会自动将多个值封装成元组，这种功能称之为封包
v_params = 1,2,3,'Python',100
print('Param type is : ', type(v_params))
#解包，把一个元组赋给多个变量时，Python会自动将元组元素自动赋值给各个变量，这种功能称之为解包
print('-' * 100)
v_params = (1,2,3,'C#')
a,b,c,d = v_params
print('a is : ',a,'\t b is : ',b,'\t c is : ',c, '\t d is : ', d)
print('-' * 100)
#多个值赋给多个变量:本质就是先封包后解包
a,b,c,d = 1,2,3,'Java'
print('a is : ',a,'\t b is : ',b,'\t c is : ',c, '\t d is : ', d)
print('-' * 100)
#列表操作方法
#追加元素 - append方法
v_list = [1,2,3]
print('List is : ', v_list)
v_list.append('.NET')
print('After append one element : ', v_list)
print('-' * 100)
#extend()追加另一列表/元组所以的元素到当前列表
v_list.extend(list(range(4,8)))
print('After extend a list : ', v_list)
v_list.extend(tuple(range(8,10)))
print('After extend a tuple : ', v_list)
print('-' * 100)
#insert()将元素插入到指定的位置
v_list.insert(5, 'Python')
print('Insert one element of index 5 : ', v_list)
print('-' * 100)
#删除元素- 方式一：del Python专门执行删除的语句，可以删除列表元素、字典元素以及变量
print('Before delete the list is :', v_list)
del v_list[3]
print('First delete (delete index 3 element) : ', v_list)
del v_list[1:3]
print('Second delete (delete [1 - 3] index elements) : ', v_list)
del v_list[2:6:2]
print('Second delete (delete [2 - 6] step 2 elements) : ', v_list)
print('-' * 100)
#remove()方法，不是根据下标删除元素，而是删除第一个匹配的元素
print('Before remove the list is :', v_list)
v_list.remove(7)
print('Remove element 7 : ', v_list)
print('-' * 100)
#元素赋值也可实现列表的增加和删除
v_list = list(range(1,10))
print('The origin list is : ', v_list)
#指定索引插入一个值，列表新增一个元素
v_list[3] = 'Java'
print(v_list)
#指定索引索引域插入N个值，列表新增N个元素
v_list[4:6] = ['Python','C#','JavaScript']
print(v_list)
#指定索引索引域插入1个值，列表较少N个元素
v_list[0:3] = [100]
print(v_list)
#字符串会被当成数组处理
v_list[5:7] = 'Harry'
print(v_list)
print('-' * 100)
#列表方法
#统计元素个数count()
print('element r count : ', v_list.count('r'))
print('element 200 count : ', v_list.count(200))
print('-' * 100)
#定位元素坐标, 返回第一个匹配元素的坐标
print('element r index : ', v_list.index('r'))
print('-' * 100)
#弹出元素pop()，弹出最后一个元素
v_list.pop()
print('After pop the list is : ', v_list)
print('-' * 100)
#翻转列表
v_list.reverse()
print('Now the list is : ', v_list)
print('-' * 100)
#排序 - 此方法仅限同种类型的元素
v_list = [1,100,20,15,200,43,45,190]
print('Before sort : ', v_list)
v_list.sort()
print('After sort asc: ', v_list)
v_list.reverse()
print('desc order : ', v_list)
print('-' * 100)
#字典 - 字典创建方式
#方式一：{}直接创建
v_dict1 = {'Python':100,'Java':200,'Groovy':300}
print('Use {} to create a  dictionary : ', v_dict1)
print('-' * 100)
#方式二：使用dict构造器构筑，传值方式有二：1：传入多个列表或者元组（列表、元组的元素个数为2）2：传入关键字，关键字不允许使用表达式
v_dict2 = dict([['A',1000],['B',2000],['C',3000],['D',4000]])
print('Use dict to create a dictionary  1 : ', v_dict2)
v_dict3 = dict([('OK',200),('ERROR',400),('NOTFOUND',404)])
print('Use dict to create a dictionary  2 : ', v_dict3)
v_dict4 = dict((('A',200),('B',400),('C',404)))
print('Use dict to create a dictionary  3 : ', v_dict4)
v_dict5 = dict((['AA',200],['BB',400],['CC',404]))
print('Use dict to create a dictionary  4 : ', v_dict5)
v_dict6 = dict(AAA=100,BBB='JACK',CCC=3.14)
print('Use dict to create a dictionary  5: ', v_dict6)
print('-' * 100)
#字典访问 方式一：类型列表下标访问，方式二：使用get方法
print('Use [] way (v_dict1[\'Python\']): ', v_dict1['Python'])
print('Use get() way ( v_dict1.get(\'Python\')): ', v_dict1.get('Python'))
print('-' * 100)
#更改元素,存在key，则修改value值，不存在，则新增元素
print('Before update : ', v_dict2)
v_dict2['B'] = 'Change'
v_dict2['E'] = 500
print('After update : ', v_dict2)
print('-' * 100)
#删除字典元素 del
print('Before delete : ', v_dict2)
del v_dict2['C']
print('After delete : ', v_dict2)
print('-' * 100)
#in/not in 判断是否存在某个元素 : 根据key进行判断
print('A' in v_dict2)
print('C' in v_dict2)
print('-' * 100)
#清空字典
print('Before clear : ', v_dict3)
v_dict3.clear()
print('After clear : ', v_dict3)
print('-' * 100)
#update : 存在key，更新value值，否则新增key-value , 参数形式和dict构筑字典方式的参数一致
print('Before update : ', v_dict4)
v_dict4.update((('A',900),))
print('After update 1: ', v_dict4)
v_dict4.update([('D',100),('E',200),('F',300)])
print('After update 2: ', v_dict4)
v_dict4.update(E=800,H=600)
print('After update 3: ', v_dict4)
print('-' * 100)
#遍历
print('Dictiionary 5 : ', v_dict5)
print('-' * 100)
#遍历item
for k, v in v_dict5.items():
    print('Key is : \t', k, '\tvalue is :\t', v)
#遍历key
print('-' * 100)
for k in v_dict5.keys():
    print('Key is : \t', k, '\tvalue is :\t', v_dict5[k])
print('-' * 100)
#遍历value
for v in v_dict5.values():
    print('Value : \t', v)
print('-' * 100)
#setdefault方法，获取字段元素值，如果存在key，则返回对应的value，如果不存在，则返回默认值，同时字典新增一个key-value
print('Dictiionary 6 : ', v_dict6)
v1 = v_dict6.setdefault('NF', 404)
v2 = v_dict6.setdefault('BBB', 500)
print('Value 1 is : \t', v1)
print('Value 2 is : \t', v2)
print('Dictiionary 6 : ', v_dict6)
print('-' * 100)
#fromkeys，使用序列构筑字典,默认值为None，也可指定默认值
v_dict7 = dict.fromkeys(['K1','K2','K3','K4'])
v_dict8 = dict.fromkeys(('KEY1','KEY2','KEY3'), 100)
print('Dictiionary create by list : ', v_dict7)
print('Dictiionary create by tuple : ', v_dict8)
print('-' * 100)
#格式化字符串 ， 根据key匹配， 元组根据位置匹配
v_str = "The book's name is : %s, and the price is : %10.2f"
print(v_str %('Crazy Java', 134))
v_str = "The book's name is : %(name)s, and the price is : %(price)10.2f"
print(v_str %{'price':138, 'name':'Crazy Linux'})
print('-' * 100)