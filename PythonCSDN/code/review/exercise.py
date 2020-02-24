#列表推导式
list = [str(i)+"-"+str(i) for i in list(range(6))]
print(list)
#字典默认值
dic = dict(A=100,B=200,C=300,D=400)
for k,v in dic.items():
    print('Key is : %s, value is %s' %(k, v))
value = dic.setdefault('D', 500)
print('Value is : ', value)    
#函数
def function1(a, b):
    print('Param a is : ', a, ', param b is : ', b)
#参数传入 - 位置传入
function1(100, 200)    
#参数传入 - 关键字传入
function1(a=300, b= 400)
