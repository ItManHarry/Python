#局部函数
def outerFun():
    print('outer function ')
    a = 'ok'
    def innerFun():
        #使用nonlocal声明来使用函数中的变量
        nonlocal a
        for i in range(5):              
            print(i, a)
            a = 'i'+str(5)
            print('now a is : ', a)
    innerFun()
outerFun()    
print('-' * 50)
def foo():
    print('foo')
    def bar():
        for i in range(5):
            print(i)
    return bar
r = foo()
r()
print('-' * 50)
foo()()