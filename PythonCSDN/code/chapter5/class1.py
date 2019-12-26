#第一个类
class  Person:
    print('Person')
    #类体中定义的变量为类变量
    name = 'Sam'
    age = 1
    def info(self):
        print('Name : ',self.name, '\tage : ', self.age)
print('Name is : ', Person.name)
Person.age = 36
print('Age is : ', Person.age)
#Python属于动态语言，随时可以为类增加类变量（只要对类应用的变量赋值，就是增加新的类变量）
Person.address = 'ShanDong Yantai'
print('Address is : ', Person.address)
#也是随时删除变量
del Person.address
#以下语句会报错，因为address属性已被删除
#print('Address is : ', Person.address)

