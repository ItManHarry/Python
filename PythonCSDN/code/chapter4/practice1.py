#定义计算N的阶乘函数
#方式一：使用循环执行阶乘计算
print('-' * 50)
def factorial1(n):
    r = 1
    if n < 1:
        print('n should not less than 1')
        return
    else:
        for i in range(1, n+1):
            r *= i
    return r
print('5 factorial is : ', factorial1(5))  
print('-' * 50)
#方式二：使用递归
def factorial2(n):
    if n < 1:
        return
    elif n == 1:
        return 1
    else:
        return factorial2(n-1) * n
print('5 factorial is : ', factorial2(5))
print('-' * 50)
#方式三：使用reduce()函数
#函数用法： reduce(function, sequence, [,initial])
import functools
def function(x, y):
    return x * y
def factorial3(n):
    if n < 1:
        return
    else:
        #也可用lambda匿名函数
        #return functools.reduce(function, range(1, n+1))
        return functools.reduce(lambda x, y:x * y, range(1, n+1))
print('5 factorial is : ', factorial3(5))
print('-' * 50)   