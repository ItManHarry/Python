#Review
#列表、元组(两者的区别就是列表元素可以修改，元组元素不可修改)
print('' * 80)
v_list = [1,2,3,'Java',3.14,"Python"]
v_tuple = (10,20,30,'Harry',40,50)
print('List : ', v_list)
print('Tuple : ', v_tuple)
v_list = list(range(1,10))
v_tuple = tuple(range(5,15))
print('' * 80)
print('Now the list is : ', v_list)
print('Now the tuple is : ', v_tuple)
print('' * 80)
#通过索引访问列表及元组
for i in range(len(v_list)):
    print('Index is : ', i, ' element is : ', v_list[i])
print('-' * 80)
#某个下标对应的值
print('List index 4 , element is : ', v_list[4])    
print('Tuple index 4 , element is : ', v_tuple[4])  
print('-' * 80) 
#包含前面的下标值，不包含后面的下标值    
print('List elements 3 - 5 : ', v_list[3:5])
print('Tuple Elements 3 - 5 : ', v_tuple[3:5])
print('-' * 80)
#带有步长的列表取值范围
print('List elements 1 - 10 , every two : ', v_list[1:10:2])
print('Tuple elements 1 - 10 , every two : ', v_tuple[1:10:2])
print('-' * 80)
#列表、元组相加 - 只是元素的总和
#列表只能和列表相加、元组只能和元组相加。如果列表加元组，需要使用list函数将元组转换为列表后再相加
v_list1 = [1,2,3]
v_list2 = ['a',b'','c']
v_list_sum = v_list1 + v_list2
print('List 1 : ', v_list1)
print('List 2 : ', v_list2)
print('List sum : ', v_list_sum)
print('-' * 80)
#列表相乘，只是元素重复对应的倍数，字符串也支持翻倍
print('List1 : ', v_list1)
print('List1 * 3 : ', v_list1 * 3)
v_str = 'abc'
print('String : ', v_str)
print('String * 3 : ', v_str * 3)
#序列相关函数
print('-' * 80)
#len()序列长度
print('List 1 : ', v_list1)
print('List1 length : ', len(v_list1))
#max/min函数
print('Max element of list1', max(v_list1))
print('Min element of list1', min(v_list1))
print('-' * 80)
#封包，将多个值付给一个变量，Python会自动将多个值封装成元组，这种功能称之为封包
v_params = 1,2,3,'Python',100
print('Param type is : ', type(v_params))
#解包，把一个元组赋给多个变量时，Python会自动将元组元素自动赋值给各个变量，这种功能称之为解包
print('-' * 80)
v_params = (1,2,3,'C#')
a,b,c,d = v_params
print('a is : ',a,'\t b is : ',b,'\t c is : ',c, '\t d is : ', d)
print('-' * 80)
#多个值赋给多个变量:本质就是先封包后解包
a,b,c,d = 1,2,3,'Java'
print('a is : ',a,'\t b is : ',b,'\t c is : ',c, '\t d is : ', d)
print('-' * 80)
#列表操作方法
#追加元素 - append方法
v_list = [1,2,3]
print('List is : ', v_list)
v_list.append('.NET')
print('After append one element : ', v_list)
print('-' * 80)
#extend()追加另一列表/元组所以的元素到当前列表
v_list.extend(list(range(4,8)))
print('After extend a list : ', v_list)
v_list.extend(tuple(range(8,10)))
print('After extend a tuple : ', v_list)
print('-' * 80)
#insert()将元素插入到指定的位置
v_list.insert(5, 'Python')
print('Insert one element of index 5 : ', v_list)
print('-' * 80)
#删除元素- 方式一：del Python专门执行删除的语句，可以删除列表元素、字典元素以及变量
print('Before delete the list is :', v_list)
del v_list[3]
print('First delete (delete index 3 element) : ', v_list)
del v_list[1:3]
print('Second delete (delete [1 - 3] index elements) : ', v_list)
del v_list[2:6:2]
print('Second delete (delete [2 - 6] step 2 elements) : ', v_list)
print('-' * 80)
#remove()方法，不是根据下标删除元素，而是删除第一个匹配的元素
print('Before remove the list is :', v_list)
v_list.remove(7)
print('Remove element 7 : ', v_list)
print('-' * 80)