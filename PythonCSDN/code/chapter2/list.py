#列表 元组
my_list = [1,2,3,'Python',3.4]
print(my_list)
my_list = list(range(2,10))
print(my_list)
#元组一旦创建，元素无法被程序修改
my_tuple = (1,2,3.4,"Python")
print(my_tuple)
my_tuple =tuple(range(3,10))
my_tuple = tuple(my_list)
print(my_tuple)
#如果元组中只有一个元素，必须添加一个逗号
my_tuple2 = (5, 10,"Java","Python")
print(my_tuple2)
my_list = list(my_tuple2)
#index， 索引不可越界
print('My list is : ', my_list, ', the length of the list is :' , len(my_list))
print(my_list[0], my_list[2], my_list[-2])
#索引不可越界
#print(my_list[7])
my_list = [1,2,3,'Python',3.4]
print(my_list[1:3])
print(my_list[3:-1])
print(my_list[1:7:2])
list1 = [1,2,3]
list2 = ['a','b','c']
print("list1 + list2 :",list1 + list2)
tuple1 = (1,2,3)
tuple2 = ('a','b','c')
print("tuple1 + tuple2", tuple1 +tuple2)
print("list * 3 :", list1 * 3)
str1 = 'abc'
print(str1 * 3)
#len(),max(),min()
my_list = ['.Net','C','Java','Python','Javascript','Vue','jQuery']
print("my_list length : ", len(my_list))
print("max str :", max(my_list))
print("min str :", min(my_list))
#序列封包
pck = 1,2,3,'Python',3.4
print(type(pck))
print("pck is : ", pck)
#全解包
params = ['python',1, 2]
a,b,c=params
print("a is : ", a, "b is : ",b," c is : ",c)
#部分解包
params = ('a','b','c','d','e')
a, *b = params
print("a is : ",a,", b is :", b)
first, *rest, last = params
print("first is :", first, ", last is :", last, "rest is :", rest)
a,*b,c="www.python.org"
print("a is : ",a,", b is :", b, ", c is : ", c)
#多个值付给多个变量
a,b,c = 10 , 'Python', 30
print("a is : ",a,", b is :", b, ", c is : ", c)
#添加、删除、替换元素
list1= [1,2,3]
list1.append("Java")
print("list is :", list1)
list1.append(tuple(range(1,6)))
print("list is :", list1)
list1.extend(list(range(2,6)))
print("list is :", list1)
list1.insert(2,'Jack')
print("list is :", list1)
#delete
del list1[2]
print('After delete : ', list1)
del list1[3:5]
print('After delete : ', list1)
del list1[2:5:2]
print('After delete : ', list1)
list1.remove(5)
print('After delete : ', list1)
#更改列表元素
my_list = [1,2,3,'Python']
my_list[-2] = 'Java'
print("My list is : ", my_list)
my_list[2:4] = ['a','b','c']
print("My list is : ", my_list)
my_list[2:4] = ['Python']
print("My list is : ", my_list)
#字符串会被当成数组处理
my_list[2:4] = 'Python'
print("My list is : ", my_list)
#count()
print(my_list.count(1))
#index()
print(my_list.index(100))
#pop()
my_list.pop()
print(my_list)
#reverse()
my_list.reverse()
print(my_list)
my_list = [1,5,2,1,8,2,10,4,19]
print(my_list)
#sort()
my_list.sort()
print(my_list)
my_list.reverse()
print(my_list)