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