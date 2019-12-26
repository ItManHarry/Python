#类的一个方法调用另外一个方法
class Dog:
    
    def run(self):
        self.jump()
        print('Run')
        
    def jump(self):
        print('Jump')
        
dog = Dog()
dog.run()
dog.jump()        