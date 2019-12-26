#返回self参数
class Plant:
    
    def __init__(self, height=2):
        self.height = height
        
    def grow(self):
        self.height += 10
        return self
        
p = Plant(10)
p.grow().grow().grow()
print(p.height)        