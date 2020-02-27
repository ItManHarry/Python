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
#带有默认值的参数要放在不带默认值参数的后面
def function2(name, age=25):
    print('Name is : ', name, ', age is : ', age)
function2("Harry")
#参数收集
def function3(amount, *books):
    print('Amount is : ', amount)
    print('books type is : ', type(books))
    for book in books:
        print('Book is : ', book)
function3(300, 'Python','Java','C','Groovy')
#如果普通参数收集放到了其他形参前面，形参只能通过关键字传值
def function4(*books,amount):
    print('Amount is : ', amount)
    print('books type is : ', type(books))
    for book in books:
        print('Book is : ', book)
function4('Python','Java','C','Groovy',amount=300)
def function5(year,*classes,**scores):
    for cls in classes:
        print('Class is : ', cls)
    print('Scores type : ', type(scores))
    for k,v in scores.items():
        print('Class : ', k, ', score : ', v)
    print('Year : ', year)
function5(2020,'A','B','C',A=100,B=200,C=300)   
def function6(year,*temp,**scores):
    for key, value in scores.items():
        print('Class : ', key, ', score : ', value)
    print('Year is : ', year)
function6(2020,1,2,3,A=100,B=200,C=300)       
#反向参数收集
params1 = (100, 200)
params2 = dict(a=5000,b=6000)
def function7(a,b):
    print('a is : ', a, ', b is : ', b)
function7(*params1)  
function7(**params2)
#变量作用域
a = "Globle variable"
def info():
    print(globals()['a'])
    global a
    a = 'Locale variable'
    print(globals()['a'])
    print(a)
info()   
print('Now the a is : ',a) 
#内部函数
def outer(p):
    print('Outer param is : ', p)
    a = 'aaa'
    print('Outer a is : ', a)
    def inner(ip):
        nonlocal a, p
        for i in range(5):
            a += str(i)
            p +=str(i)
    inner('inner param')
    print('Final a is : ', a, 'Final p is : ', p)
outer('ppp')    