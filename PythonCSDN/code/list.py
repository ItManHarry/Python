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