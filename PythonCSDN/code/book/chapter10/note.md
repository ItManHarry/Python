# 常见模块

Python库参考手册：https://docs.python.org/3/index.html

- 使用sys模块的函数与Python解释器交互

```
	import sys
	#本地字节指示符 - 大端模式返回big，否则返回little
	print(sys.byteorder)
	#Python相关的版权信息
	print(sys.copyright)
	#Python解释器在磁盘上的存放路径
	print(sys.executable)
	#当前系统保存文件使用的字符集
	print(sys.getfilesystemencoding())
	#Python整数支持的最大值
	print(sys.maxsize)
	#Python解释器所在的平台
	print(sys.platform)
	#Python解释器的版本信息
	print(sys.version)
	#Python主解释器的版本号
	print(sys.winver)
```

	通过sys模块的argv属性可以获取运行Python程序的命令行参数。argv属性是一个列表，其列表元素和运行参数的关系如下：
	
		python 程序名 第一个参数、第二个参数、......
		
```
	import sys
	from sys import argv
	print(len(argv))
	for arg in argv:
		print(arg)
```

	动态修改模块的加载路径，使用sys.path属性的append方法
	
```
	import sys
	sys.path.append('e:\\fk_ext')
	import hello
```

- 使用os模块的函数获取操作系统信息

```
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
```

- 使用random模块生成随机数

- 使用time模块

- 日期、时间与字符串相互转换

- JSON及Python的JSON支持

- 正则表达式

- set和frozenset集合

- 双端队列deque的功能和用法

- Python的堆操作

- ChainMap对象的功能和用法

- Counter对象的功能和用法

- defaultdict对象的功能和用法

- 命名元组的功能和用法

- OrderedDict对象的功能和用法

- itertools模块下的迭代器功能函数

- functools模块下的函数修饰器和功能函数