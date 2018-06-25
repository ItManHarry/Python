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
def multiple(x, y):
	x = 2
	y = [3,4]
	return x, y
x = 1
y = [1, 2]
x, y = multiple(x, y)
print(x, y)
print('-' * 80)
def func(a,b,c):
	print(a,b,c)
func(1,2,3)
func(c=100,b=99,a=98)
func(101,c=103,b=102)
print('-' * 80)
def defaultFun(a,b=2,c=3):
	print(a,b,c)
defaultFun(1)
defaultFun(a=100)
defaultFun(a=10,c=20)
defaultFun(11,b=12)
print('-' * 80)
def tuplefunc(*args):
	print(args)
tuplefunc()
tuplefunc(1)
tuplefunc(1,2,3,4)
print('-' * 80)
def dictfunc(**args):
	print(args)
dictfunc()
dictfunc(a=1,b=2)
dictfunc(a=1,b=2,c=3)
print('-' * 80)
def multiplefunc(a,*pargs,**kargs):
	print(a,pargs,kargs)
multiplefunc(1,2,3,x=1,y=2)
print('-' * 80)
def unpackfunc(a,b,c,d):
	print(a,b,c,d)
args = (1,2)
args += (3,4)
unpackfunc(*args)
unpackfunc(5,6,7,8)
args = {'a':9,'b':10,'c':11,'d':12}
unpackfunc(**args)
print('-' * 80)