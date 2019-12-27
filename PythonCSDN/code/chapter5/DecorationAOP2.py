#函数装饰器与AOP
def decorateFunction(function):
    def aop(*args):
        print(len(args))
        for a in args:
            print('argument : ', a)
        print('function not executed...')
        function(*args)
        print('function executed...')
    return aop
   
@decorateFunction   
def beenDecorated(a,b):
    print('argument a : ', a)
    print('argument b : ', b)
    
beenDecorated(100,200)    