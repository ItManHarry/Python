#Python字典
#基本创建方式 key-value对
my_dict = {"Java":98, "Python":89,"Javascipt":94}
print(my_dict)
#dict构造器构造，参数为列表或者元组，元素为元组，元组元素只能是两个，一个为key，一个为value
my_dict = dict([("Java",100,),("Python",120),("Javascipt",110)])
print(my_dict)
my_dict = dict((("Java",500,),("Python",600),("Javascipt",700)))
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
#清空字典-clear()
print("Before clear : ", my_dict)
my_dict.clear()
print("After clear : ", my_dict)
#获取值-get()
my_dict = dict([('Python',100),('Java',120),('Js',130)])
print('Now the dictionary is : ', my_dict)
print("Java value is :", my_dict.get('Java'))
#字典更新-update():对于已经存在的key，就是更新value值，对于不存在的key，就是新增key-value
my_dict.update({'Python':140,'C':130})
print("After update : ",my_dict)
my_dict.update([('Java',100),('Vue',150)])
print("After secondary update : ",my_dict)
my_dict.update((('Java',300),('Vue',500)))
print("After thirdly update : ",my_dict)
my_dict.update(Java=1000,HTML=2000)
print('After forth udpate : ',my_dict)
#遍历
print('-' *80)
for key, value in my_dict.items():
    print('Key is :',key, ', and value is :', value)
print('-' *80)
for item in my_dict.items():
     print('Key is :',item[0], ', and value is :', item[1])
print('-' *80)
for key in my_dict.keys():
    print('Key is :',key, ', and value is :', my_dict.get(key))
    print('Key is :',key, ', and value is :', my_dict[key])
print('-' *80)
for value in my_dict.values():
    print("Value is : ", value)
print('-' *80)
#setdefault
value = my_dict.setdefault('Java', 50)
print("Value is : ",value)
value = my_dict.setdefault('CSS', 400)
print("Value is : ", value)
print("Dictionary is :", my_dict)
#fromkeys
print('-' *80)
scores = dict.fromkeys(['Python','Java','HTML'])
print(scores)
scores = dict.fromkeys(['Python','Java','HTML'], 100)
print(scores)
print('-' *80)
#元组匹配 - 根据顺序匹配
string = 'The book name is %s, and the price is : %10.2f'
print(string %('Java',120))
#字典格匹配 - 根据key匹配
string = 'The book name is %(name)s, and the price is : %(price)10.2f'
print(string %{'price':128,'name':'Python'})