#Python字典
#基本创建方式 key-value对
my_dict = {"Java":98, "Python":89,"Javascipt":94}
print(my_dict)
#dict构造器构造，参数为列表，列表元素为元组，元组元素只能是两个，一个为key，一个为value
my_dict = dict([("Java",100,),("Python",120),("Javascipt",110)])
print(my_dict)
#dict构造器指定关键字创建字典，此时字段的key不允许使用表达式
my_dict = dict(Java=200,Python=300,Javascript=400)
print(my_dict)
#数据访问 - 通过key 访问
print("Java : ", my_dict['Java'])
#修改value，如果key不存在，相当增加key-value对,如果存在，就是修改对应key的value值
my_dict['Vue'] = 500
print(my_dict)
my_dict['Java'] = 900
print(my_dict)
#删除key-value对
del my_dict['Vue']
print(my_dict)
#判断是否存在某个key-value对
print('Java' in my_dict)
print('Vue' in my_dict)
print('Vue' not in my_dict)