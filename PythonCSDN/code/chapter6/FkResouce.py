class FkResource:
	def __init__(self,tag):
		self.tag = tag
		
	def __enter__(self):
		print('Resource tag is : ', self.tag)
		return 'python'
	'''
		这三个参数都代表了异常
		ex_type:异常类型
		ex_value:异常值
		ex_traceback:异常traceback
	'''
	def __exit__(self, ex_type, ex_value, ex_traceback):
		if ex_traceback:
			print('资源异常关闭')
		else:
			print('资源正常关闭')
# 1. 执行with后的表达式（FkResource('crazypython')）
# 2. 执行__enter__()方法，并将返回值付给as后面的变量
# 3. with语句块执行完成或者遇到异常时，__exit__()方法自动执行		
with FkResource('crazypython') as fk:
	print('fk is : ', fk)
	print('before')
	raise Exception(20,'error')
	print('after')
	