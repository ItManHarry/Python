'''
	This is my first module , it contains :
	1. Property : my_book
	2. Function : say_hi
	3. Class : User
'''
print('This is a Module')
my_book = 'Crazy Python'
def say_hi(user):
    print('Hi %s welcome to the Python world ' %user)
class User:
        def __init__(self, name):
            self.name = name
        def walk(self):
            print('%s is walking...' %self.name)
        def __repr__(self):
            return 'User[name=%s]' %self.name