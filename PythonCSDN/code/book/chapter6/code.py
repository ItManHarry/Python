#枚举
import enum
class Orientation(enum.Enum):
    EAST = '东'
    SOUTH = '南'
    WEST = '西'
    NORTH = '北'
    def info(self):
        print('This is a [%s] enumerate.' %self.value)
        
print(Orientation.SOUTH)   
print(Orientation.SOUTH.value)
print(Orientation['WEST'])
print(Orientation['WEST'].value)
print(Orientation('南'))
Orientation.EAST.info()
for name, member in Orientation.__members__.items():
    print('Name : ', name, ' ,value :  ', member.value)