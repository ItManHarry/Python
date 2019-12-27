#函数装饰器
def foo(fn):
	print('function foo')
	print(fn)
	return 'PythonProgramming'
	
@foo
def bar():
	print('function bar')
print('-' * 80)
print(bar)
print('-' * 80)
foo(bar)
print('-' * 80)