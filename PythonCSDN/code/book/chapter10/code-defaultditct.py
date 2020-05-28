from collections import defaultdict
print('-' * 80)
#普通字典
sd = {}
#默认值字典 - 值默认为int类型的值
dd = defaultdict(int)
#访问不存在的key
#普通字典报错，[KeyError: 'a']
#print('Simple dict : ', sd['a'])
print('Default dict : ', dd['a'])
print('-' * 80)
#设置默认值
s = [('Python',1,100),('Java',3,200),('Python',4,300),('Groovy',5,400),('Java', 5,500),('Groovy',20,600)]
for e1,e2,e3 in s:
    print('Element 1 : ',e1,', element 2 : ',e2,',element 3 : ',e3)
print('-' * 80)
s = [('Python',1),('Java',3),('Python',4),('Groovy',5),('Java', 5),('Groovy',20)]
for k, v in s:
    print('Key is : ', k, ', value is : ', v)
#方式一：普通字典
d = {}
for k, v in s:
    d.setdefault(k, []).append(v)
print(list(d.items()))    
#方式二：默认值字典
d = defaultdict(list)
for k,v in s:
    d[k].append(v)
print(list(d.items()))    
print('-' * 80)