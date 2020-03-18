#函数
def fn(n):
    if n == 0:
        return 1
    elif n == 1:
        return 4
    else:
        return 2 * fn(n-1) + fn(n-2)
print(fn(10))    
print('-' * 80)    
def swap(a, b):
    print('Before swap the a is %s, b is %s' %(a, b))
    a, b = b, a
    print('After swap the a is %s, b is %s' %(a, b))
a = 100 
b = 200
swap(a, b)    
print('After invoke the swap function  a is %s, b is %s' %(a, b))
print('-' * 80)    
def map(data, function):
    result = []
    for e in data:
        result.append(function(e))
    return result
def square(n):
    return n * n
def cube(n):
    return n * n * n
def fac(n):
    result = 1
    for index in range(2, n + 1):
        result += index
    return result
data = [0,3,4,9,5,8]
print(map(data, square))
print(map(data, lambda x : x*x))
print(map(data, cube))
print(map(data, lambda n : n * n * n))
print(map(data, fac))