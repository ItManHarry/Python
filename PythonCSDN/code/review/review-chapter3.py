#Review Chapter 3
#if 
print('-' *80)
age = 25
if age > 18:
    print('成年人!')
else:
    print('未成年!')
#if elif else
print('-' *80)
name = 'Jack'
if name == 'Harry':
    print('I am Harry.')
elif name == 'Jack':
    print('I am Jack')
else:
    print('I am someone else!')
print('-' *80)
#三目运算符
grade = input('Input your grade (A,B,C) : ')
score = 100 if  grade == 'A' else 90 if grade == 'B' else 80
print('Score : ', score)
print('-' *80)
v_list = []
if v_list:
    print('List is not empty!')
else:
    print('List is empty!')
print('-' * 80)
#pass : 占位，不做操作
if v_list:
    print('list is ok')
else:
    pass
print('-' * 80)        
#while
v_list = list(range(1,25))
i = 0
while i < len(v_list):
    print('Index is : ', i, '\tvalue is : ', v_list[i])
    i += 1
print('-' * 80)
v_dict = {'OK':200,'ERROR':400,'NOTFOUND':404,'SYSERROR':500}
print('Keys type : ', type(v_dict.keys()))
keys = list(v_dict.keys())
i = 0
while i < len(keys):
    print('Key is : ', keys[i], '\tvalue is : ', v_dict.get(keys[i]))
    i += 1
print('-' * 80)
#for in 
for e in v_list:
    print('Element : ', e)
print('-' * 80)
for key, value in v_dict.items():
     print('Key is : ', key, '\tvalue is : ', value)
print('-' * 80)
#列表推导式
new_list = [str(i) + '-' + str(i) for i in list(range(1,6))]
print('New list is : ', new_list)
print('-' * 80)
#break continue return
for i in list(range(1,20)):
    if i == 15:
        break
    else:
        print('i is : ', i)
print('-' * 80)        
for i in list(range(1,20)):
    if i % 2 == 0:
        continue
    else:
        print('i is : ', i)    
print('-' * 80)