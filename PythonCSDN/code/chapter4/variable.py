#变量的作用域
a = 23
name = 'Python'
def info():
    b = "Java"
    print(b)
    print(locals())
print('-' * 50) 
info()
print('-' * 50)
print(globals())
def vars_info():
    #使用globals()获取全局变量字典，然后通过变量名作为key进行访问
    print(globals()['name'])
    name = "C#"
    print(name)
print('-' * 50)     
vars_info()
print(name)
print('-' * 50)
def vars_info2():
    global name
    print(name)
    name = "Javascript"
    print(name)
vars_info2()
print("Now the name is : ", name)    
