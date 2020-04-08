import os
#操作系统名称
print(os.name)
#系统环境变量
ens = os.environ
for k, v in ens.items():
    print('Key : ', k, ', value : ', v)
#当前系统登录用户名
print(os.getlogin())
#打印当前进程
print(os.getpid())
#打印父进程
print(os.getppid())
#CPU数量
print(os.cpu_count())
#系统路径分隔符
print(os.sep)
#当前系统的分隔符
print(os.pathsep)
#当前系统的换行符
print(os.linesep)
#返回适合加密使用的、最多由3个字节组成的bytes对象
print(os.urandom(3))