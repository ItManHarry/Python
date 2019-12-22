#函数 - 基本函数
def printFun():
    '''
        this is a print function
    '''
    print('This is for print.')
    for i in range(5):
        print('i is : ', i)
printFun()
print('-' * 50)
def paramFun(name):
    '''
        this is a print function
        name - an input name
    '''
    print('Hello : ', name)
paramFun('Harry')
print('-' * 50)
def maxFun(x, y):
    r = x if x > y else y
    return r
x = maxFun(19, 30)
print('Max : ', x)
print("Max : ", maxFun(20, 15))
print('-' * 50)
#函数文档
print(paramFun.__doc__)
print('-' * 50)
#多返回值函数（元组）
import random
def multiFun():
    c1 = chr(random.randint(65,90))
    c2 = chr(random.randint(65,90))
    c3 = chr(random.randint(65,90))
    return c1, c2, c3
multiResult = multiFun()
print(multiResult)
a,b,c = multiResult
print('a is : ',a,' b is : ',b,'c is : ',c)
print('-' * 50)
#递归函数
def  frac(n):
    if n < 1:
        print('n should not be less than 1')
        return
    elif n == 1:
        return 1
    else:
        return frac(n-1) * n
print('frac 5 is : ', frac(5))
print('frac 6 is : ', frac(6))   
print('-' * 50)  
#关键字参数
def info(age, height, name='ABC'):
    print('Name : ', name)
    print('Age : ', age)
    print('Height : ', height)
info('ChengGuoqian',36,170)    
print('-' * 50)
info(age=36,name='Harry',height=168)
print('-' * 50)
info(age=36,height=168)
print('-' * 50)
def welcome(name="Harry", message="Welcome to the Python world."):
    print(name,',', message)
welcome('Jack')
welcome(message='change yourself for the future!')
print('-' * 50)
def test(num, *books):
    print("Number : ", num)
    print("Books : ", books)
test(100, 'Java','Python','C#')        
def info2(*names, message):
    for name in names:
        print('%s, %s' %(name, message))
info2('A','B','C','D',message=' welcome you .')   
print('-' * 50)
def info3(*ages, message):
    for age in ages:
        print('%d, %s' %( age, message))
info3(15,23,23,45,message="ok")
print('-' * 50)
def info4(num,*names, **scores):
    print('Number : ', num)
    print("Names : ", names)
    print('Scores : ', scores)
info4(30,'Java','Python','C#', js=100,ps=120,cs=150)  
print('-' * 50)
def info5(*names, message, **scores):
    print('Message : ', message)
    print("Names : ", names)
    print('Scores : ', scores)
info5('a','b','c',js=100,ps=120,cs=150,message='OK')  
print('-' * 50)
def info6(a,b):
    print('a is : ', a)
    print('b is : ', b)
vs1 = (100, 200)
vs2 = ['Python','Java']    
vs3 = {'a':300,'b':400}
vs4 = [1,2,3,4]
info6(*vs1)
print('-' * 50)
info6(*vs2)
print('-' * 50)
info6(**vs3)   
print('-' * 50)
#参数个数不符，函数调用报错（TypeError: info6() takes 2 positional arguments but 4 were given）
#info6(*vs4)