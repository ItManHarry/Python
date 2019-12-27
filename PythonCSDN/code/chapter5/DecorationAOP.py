#函数装饰器与AOP
def foo(fn):
	print('function foo')
	def aspect(*args):
		print('before function execution...')
		fn(*args)
		print('after function execution...')
	return aspect
	
@foo
def bar(a,b):
	print('function bar')
	print('a is : ', a)
	print('b is : ', b)
print('-' *80)
bar(10,20)
print('-' * 80)