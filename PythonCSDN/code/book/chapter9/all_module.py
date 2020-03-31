#__all__变量：过滤对外暴露的方法及变量
def hello():
	print('Hello, python.')
def world():
    print('Python world is funny...')
def hi():
	print('Hi , can you call me?')
__all__= ['hello','world']	