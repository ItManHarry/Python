#创建及使用对象
class User:
    #构造方法就是初始化对象的实例变量
    def __init__(self, name='User',password='123456'):
        print('构造方法')
        self.name = name
        self.password = password
    def info():
        print('User name is : ', self.name, '\tPassword is : ', self.password)
#空类使用pass即可        
class Employee:
            pass
#创建对象, 就是调用构造器
print('-' * 80)
user1 = User()    
print(user1.name, user1.password)  
print('-' * 80)
user2 = User('Harry')  
print(user2.name, user2.password)       
print('-' * 80)
user3 = User(password='12345678')
print(user3.name, user3.password)  
print('-' * 80)
user4 = User(name='Jack',password='852369')
print(user4.name, user4.password)  
print('-' * 80)