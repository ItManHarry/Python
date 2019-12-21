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