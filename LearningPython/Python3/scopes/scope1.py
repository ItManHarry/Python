x = 99
def func(y):
	z = x + y
	return z

print(func(1))

x = 88

def func2():
	global x
	x = 200
	print(x)

def func3():
	global x
	x = 300
	print(x)
	
func3()
func2()
print(x)