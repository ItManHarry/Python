#Python流程控制
s = ""
if s:
    print('非空字符串')
else:
    print('空字符串')
l = []
if l:
    print('非空列表')
else:
    print('空列表')
d = {}
if d:
    print('非空字典')
else:
    print('空字典')
pass   
print('-' * 80) 
#isinstance函数
v_list = [1,23,34.5,'a',109.8,100,'Harry',300,'b']
v_sum = 0
v_count = 0
for i in v_list:
    if isinstance(i, int) or isinstance(i, float):
        v_count += 1
        v_sum += i
print('列表 ： ', v_list)        
print('总和 ：', v_sum)        
print('总数 ：', v_count)
print('平均数 ：', v_sum / v_count)
print('-' * 80) 
#列表推导式
v_range = range(10)
v_list = [x*x for x in v_range if x % 2 != 0]
print(v_list)
print('-' * 80) 
#生成器推导式
v_generator = (x * x for x in v_range if x % 2 == 0)
print(type(v_generator))
for i in v_generator:
    print(i, end='\t')
#嵌套列表推导式  
print('')  
v_list = [(x, y) for x in range(5) for y in range(4)]
print(v_list)
print('-' * 80) 
#列表合并函数zip() - 压缩列表长度不等时，压缩长度取决于短的列表长度
list1 = list(range(5))
list2 = ['a','b','c']
z = zip(list1,list2)
print('-' * 80) 
print(type(z))
for i in z:
    print(i)
list1 = ['Java', 'Python', 'C']    
list2 = [78.0, 75.5, 86.5]
list3 = [5,8,10]
for data in zip(list1, list2,list3):
    for i in data:
        print(i)
v_dict = dict(zip(list1,list2))    
print(v_dict)
print('-' * 80) 
#reversed()函数,对原数组、元组没有影响
for i in reversed(v_range):
    print(i)
print('-' * 80) 
#sorted()函数
v_list = [5,2,9,28,12,4,3,3,24,100]
for i in sorted(v_list, reverse=True):
    print(i)
print('-' * 80)   
#九九乘法表
list1 = range(1,10)
#通过列表推导式生成全部的乘法表
nn = [str(y) + ' X ' + str(x) + ' = ' + str(x*y) for x in list1 for y in range(1,x+1)]
#print(len(nn))
index = 0
for i in range(0,9):    
    index += i
    #print('from : ', index, ', to :', index+i+1)
    for s in nn[index:index+i+1]:
        print(s, end='\t' )
    print('')