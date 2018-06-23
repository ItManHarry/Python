print('-' * 80)
def f(a):
	a = 99
	print(a)
a = 88
f(a)
print(a)
print('-' * 80)
def changer(a,b):
	a = 2
	b = b[:]
	b[0] = 'Spam'
x = 1
y = [1,2]
changer(x, y)
print('x is : ', x)
print('y is : ', y)
print('-' * 80)
x = 1
a = x
a = 2
print(x)
x = [1,2]
a = x
a[0] = 'Spam'
print(x)
print('-' * 80)