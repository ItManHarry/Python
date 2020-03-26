#异常处理
try:
    open('a.txt')
except Exception as e: 
    print(e.args)
    print(e.errno)
    print(e.strerror)