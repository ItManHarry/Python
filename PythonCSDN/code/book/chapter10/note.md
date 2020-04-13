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

```python
	#生成大于等于0.0小于1.0的伪随机浮点数
	v1 = random.random()
	print('v1 is : ', v1)
	print('-' * 80)
	#生成大于等于2.5小于10.0的伪随机浮点数
	v2 = random.uniform(2.5, 10.0)
	print('v2 is : ', v2)
	print('-' * 80)
	#生成大于等于5小于等于20的随机数
	v3 = random.randint(5, 20)
	print('v3 is : ', v3)
	print('-' * 80)
	#生成0到10的伪随机整数
	v4 = random.randrange(10)
	print('v4 is : ', v4)
	print('-' * 80)
	#生成0到100的随机偶数
	v5 = random.randrange(0, 101, 2)
	print('v5 is : ', v5)
	print('-' * 80)
	#随机抽取数组元素
	vl = ['Java','Python','C','Kotlin','Groovy']
	v6 = random.choice(vl)
	print('v6 is : ', v6)
	print('-' * 80)
	#对列表进行随机排序
	print('Before sort : ', vl)
	random.shuffle(vl)
	print('After sort : ', vl)
	print('-' * 80)
	#随机抽取n个独立元素
	nvl = random.sample(vl, k = 3)
	print('Sample list is : ', nvl)
	print('-' * 80)
```

- 使用time模块

```python
	import time
	print('-' * 80)
	#显示时区
	print(time.tzname)
	print('-' * 80)
	#当前时间转换为字符串
	now_str = time.asctime()
	print('Now is : ', now_str)
	print('-' * 80)
	#将指定的时间（使用包含9个元素的元组表示时间）转换为字符串
	time_str = time.asctime((2019,11,2,12,5,35,0,0,0))
	print('Time is : ', time_str)
	print('-' * 80)
	#将以秒代表的时间转换为字符串
	time_str = time.ctime(9000000000.0)
	print('Time is : ', time_str)
	print('-' * 80)
	#将当前时间转换为struct_time对象
	st = time.gmtime()
	print('Now the struct time is : ', st)
	print('-' * 80)
	#将以秒代表的时间转换为struct_time对象
	st = time.gmtime(300)
	print('Second time struct time is : ', st)
	print('-' * 80)
	#将以秒代表的时间转换为代表当前时间的struct_time对象
	st = time.localtime(300)
	print('Second local time struct time is : ', st)
	print('-' * 80)
	#将元组代表的时间转换为秒数代表的时间
	mt = time.mktime((2019,11,2,12,5,35,0,0,0))
	print('Seconds are : ', mt)
	print('-' * 80)
	#性能计数器的值
	count = time.perf_counter()
	print('Count is : ', count)
	print('-' * 80)
	#当前进程使用CPU的时间
	ct = time.process_time()
	print('CPU process time : ', ct)
	print('-' * 80)
	#将当前时间转换为指定格式的字符串
	now_str = time.strftime('%Y年%m月%d日 %H时%M分%S秒')
	print('Now is : ', now_str)
	print('-' * 80)
	#将指定的时间转换为指定格式的字符串
	time_str = time.strftime('%Y年%m月%d日 %H时%M分%S秒',(2010,1,23,13,22,34,0,0,0))
	print('Time is : ', time_str)
	print('-' * 80)
	#将指定时间字符串转换为struct_time对象
	time_str = '2018-10-12'
	st = time.strptime(time_str, '%Y-%m-%d')
	print('Struct time is : ', st)
	print('-' * 80)
	#获取从1970年1月1日0点到现在过了多少秒
	sds = time.time()
	print('Seconds are : ', sds)
	print('-' * 80)
```

- 日期、时间与字符串相互转换

```python
	import time
	print('-' * 80)
	#显示时区
	print(time.tzname)
	print('-' * 80)
	#当前时间转换为字符串
	now_str = time.asctime()
	print('Now is : ', now_str)
	print('-' * 80)
	#将指定的时间（使用包含9个元素的元组表示时间）转换为字符串
	time_str = time.asctime((2019,11,2,12,5,35,0,0,0))
	print('Time is : ', time_str)
	print('-' * 80)
	#将以秒代表的时间转换为字符串
	time_str = time.ctime(9000000000.0)
	print('Time is : ', time_str)
	print('-' * 80)
	#将当前时间转换为struct_time对象
	st = time.gmtime()
	print('Now the struct time is : ', st)
	print('-' * 80)
	#将以秒代表的时间转换为struct_time对象
	st = time.gmtime(300)
	print('Second time struct time is : ', st)
	print('-' * 80)
	#将以秒代表的时间转换为代表当前时间的struct_time对象
	st = time.localtime(300)
	print('Second local time struct time is : ', st)
	print('-' * 80)
	#将元组代表的时间转换为秒数代表的时间
	mt = time.mktime((2019,11,2,12,5,35,0,0,0))
	print('Seconds are : ', mt)
	print('-' * 80)
	#性能计数器的值
	count = time.perf_counter()
	print('Count is : ', count)
	print('-' * 80)
	#当前进程使用CPU的时间
	ct = time.process_time()
	print('CPU process time : ', ct)
	print('-' * 80)
	#将当前时间转换为指定格式的字符串
	now_str = time.strftime('%Y年%m月%d日 %H时%M分%S秒')
	print('Now is : ', now_str)
	print('-' * 80)
	#将指定的时间转换为指定格式的字符串
	time_str = time.strftime('%Y年%m月%d日 %H时%M分%S秒',(2010,1,23,13,22,34,0,0,0))
	print('Time is : ', time_str)
	print('-' * 80)
	#将指定时间字符串转换为struct_time对象
	time_str = '2018-10-12'
	st = time.strptime(time_str, '%Y-%m-%d')
	print('Struct time is : ', st)
	print('-' * 80)
	#获取从1970年1月1日0点到现在过了多少秒
	sds = time.time()
	print('Seconds are : ', sds)
	print('-' * 80)
```

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