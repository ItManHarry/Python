x = 88
def f1():
	x = 99
	def f2():
		print(x)
	f2()
f1()
def f3():
	x = 199
	def f4():
		print(x)
	return f4
action = f3()
action()	
def maker(n):
	def action(x):
		return x ** n
	return action
action = maker(3)
print(action(2))
g = maker(4)
print(g(2))
print(action(2))
def maker2(n):
	return lambda x:x ** n
h = maker2(3)
print(h(4))
def f5():
	x = 88
	def f6(x=x):
		print(x)
	f6()
f5()
def func1():
	x = 999
	func2(x)
def func2(x):
	print(x)
func1()
def lambdafunc1():
	x = 4
	action = (lambda n : x ** n)
	return action
x = lambdafunc1()
print(x(2))
def lambdafunc2():
	x = 4
	action = (lambda n, x = x : x ** n)
	return action
x = lambdafunc2()
print(x(2))
print('-' * 80)
def makeActions():
	acts = []
	for i in range(5):
		acts.append(lambda x, i = i : i ** x)
	return acts
actions = makeActions()
print(actions[0](2))
print(actions[1](2))
print(actions[2](2))
print(actions[3](2))
print(actions[4](2))
print('-' * 80)
def arbitraryFunc():
	x = 999
	def af1():
		def af2():
			print(x)
		af2()
	af1()
arbitraryFunc()
print('-' * 80)