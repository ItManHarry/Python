class Employee:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self,address):
        print(self.name, self.age,address)

e = Employee(age=25,name='Sam')        
e.info('Beijing')
e.name = 'Harry'
e.age = 36
e.info('Shanghai')