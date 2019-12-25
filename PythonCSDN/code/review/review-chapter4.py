#Review Chapter 4
#函数
print('-' * 80)
def hi():
    print('Hello , I am Harry')
hi()   
print('-' * 80) 
#带有参数的函数
def paramFunction(name,age):
    print('Name is : ', name, '\tage is : ', age)
#通过位置方式传入
paramFunction('Harry', 36)
print('-' * 80)     
#通过关键字传入
paramFunction(age=36,name='ChengGuoqian')
print('-' * 80)     
#带有默认值的函数，带有默认值的参数要放在不带默认值的参数后面
def defaultParamFun(age,name='Jack'):
    print('Name is : ', name, '\tage is : ', age)
defaultParamFun(36)
print('-' * 80)   
#如果省略第一个参数，后面的参数需要使用关键字进行传入
def defaultParamFun2(name='ChengGuoqian',age=36):
    print('Name is : ', name, '\tage is : ', age)
defaultParamFun2('Harry')    
defaultParamFun2('Sam',24)
defaultParamFun2(age=25)
print('-' * 80)     
#参数收集
def multiParam1(amount, *books):
    print('Amount is : ', amount)
    print('Books : ', books)
    for book in books:
        print('Book name : ', book)
multiParam1(100, 'Python','Java','Vue')        
print('-' * 80)   
#如果普通参数收集放到了其他形参前面，形参只能通过关键字传参方式传入
def multiParam2(*books, amount):
    print('Amount is : ', amount)
    print('Books : ', books)
    for book in books:
        print('Book name : ', book)
#以下调用会报错
#multiParam2('Python','Java','Vue'， 200)  
#正确的调用方式如下
multiParam2('Python','Java','Vue',amount=200)  
print('-' * 80)   
#前面加两个星号，表示通过关键字进行参数收集，参数会按照字典进行处理
def multiParam3(amount,*books,**scores):
    print('Amount is : ', amount)
    print('Books is : ', books)
    print('Scores is : ', scores)
multiParam3(100,'Java','C#','.NET',english=120,math=120,chinese=100)    
print('-' * 80)
def multiParam4(*names, message,**scores):
    print('Names is : ', names)
    print('Message is : ', message)
    print('Scores is : ', scores)
multiParam4('Harry','Jack','Tom',message='I am OK!',english=120,math=120,chinese=100)    
print('-' * 80)   