# 常见模块

Python库参考手册：https://docs.python.org/3/index.html

## 使用sys模块的函数与Python解释器交互

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

##  使用random模块生成随机数

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

##  使用time模块

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

##  日期、时间与字符串相互转换

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

##  JSON及Python的JSON支持

```python
	import json
	print('=' * 180)
	#将Python对象转换为字符串
	s = json.dumps(['Harry',{'age':37,'gender':'M'}])
	print('JSON String is : ', s)
	print('-' * 80)
	#将Python字符串转换为JSON字符串
	s = json.dumps("\"foo\bar")
	print('Now the JSON String is : ', s)
	print('-' * 80)
	s = json.dumps('\\')
	print('Now the JSON String is : ', s)
	print('-' * 80)
	#将Python字典对象转换为字符串并对key进行排序
	s = json.dumps({'c':0,'w':3,'a':19,'b':39}, sort_keys=True)
	print('Now the JSON String is : ', s)
	print('-' * 80)
	#将Python对象转换为字符串，在逗号和冒号之间没有空格
	s = json.dumps([1, 2, 3, {'x':4,'y':5}])
	print('s is : ', s)
	s = json.dumps([1, 2, 3, {'x':4,'y':5}], separators=(',',';'))
	print('s is : ', s)
	print('-' * 80)
	#缩进
	s = json.dumps({'Python':5,'Kotlin':7,'Java':10,'Groovy':8}, sort_keys=True,indent=4)
	print('s is : ', s)
	print('-' * 80)
	#使用JSONEncoder的encode方法将Python对象转换为字符串
	s = json.JSONEncoder().encode({"names":("唐僧","孙悟空","猪悟能","沙悟净")})
	print('s is : ', s)
	#将转换后的json字符串写入文件
	f = open('data.json', 'w')
	json.dump(['Java','Groovy','C',{'Python':'OK'}],sort_keys=True,indent=4, fp=f)
	print('=' * 180)
	#字符串转换为Python对象
	r = json.loads('["Java",{"others":["C","Python","Kotlin","Groovy", 1, 2, 3]}]')
	print(type(r), r)
	print('-' * 80)
	#文件读取JSON字符串后转换为Python对象
	f = open('data.json')
	r = json.load(f)
	print(type(r), r)
	print('-' * 80)
```

## 正则表达式

### 正则表达式对象&方法

	1. re.compile(pattern, flags=0) 将正则表达式编译成_sre.SRE_Pattern对象
	
	2. re.match(pattern, string, flags=0) 从字符串开始位置来匹配正则表达式，如果从开始位置匹配不成功，则返回None
	
	3. re.search(pattern, string, flags=0) 扫描整个字符串，并返回字符串第一处匹配pattern的匹配对象
	
	注：match()和search()的区别：match()必须从字符串起始位置匹配，search()则可以扫描整个字符串
	
```python
	import re
	print('=' * 180)
	p = re.compile('www')
	print(type(p))
	m1 = re.match(p,'www.fkit.org')
	print(type(m1))
	print(m1.span())
	print(m1.group())
	print(re.match('fkit','www.fkit.org'))
	print('-' * 80)
	m2 = re.search('www','www.fkit.org')
	print(type(m2))
	print(m2.span())
	print(m2.group())
	print('-' * 80)
	m3 = re.search('fkit','www.fkit.org')
	print(m3.span())
	print(m3.group())
	print('=' * 180)
```	

	4. re.findall(pattern, string, flags=0) 扫描整个字符串，并返回字符串中匹配pattern的子串组成的列表
	
	5. re.finditer(pattern, string, flags=0) 扫描整个字符串，并返回字符串中匹配pattern的子串组成的迭代器
	
```python
	import re
	r = re.findall('fkit','Fkit is good, I like the fkit and the Fkit.org web',re.I)
	print(type(r))
	print(r)
	r = re.finditer('fkit','Fkit is good, I like the fkit and the Fkit.org web',re.I)
	print(type(r))
	for e in r:
		print(e.span() ,'-->',e.group())
```

	6. re.fullmatch(pattern, string, flags=0) 整个字符串匹配pattern，不匹配则会返回None
	
	7. re.sub(pattern, repl, string, count=0,flags=0)将字符串中所有匹配pattern的内容都替换为repl(repl可以是一个字符串，也可以是一个函数)，
	count控制替换的次数，默认为0替换全部
	
```python
	import re
	my_date = '2020-04-24'    
	print('Date string : ', my_date)
	print(re.sub(r'-','/',my_date))
	my_str = 'Java is a good language , and the Python too'
	print('String : ', my_str)
	print(re.sub(r'o', 'u', my_str))
```

	8. re.split(pattern, string, maxsplit=0, flags=0)使用pattern对字符串进行分割
	
```python
	import re
	my_str = 'a,b,c,d,e,f'
	my_list = my_str.split(',')
	print(my_list)
	r = re.split(',', my_str)
	print(type(r))
	print(r)
```

	9. re.purge()清除正则表达式缓存
	
	10. re.escape(pattern)
	
```python
	import re
	print(re.escape(r'www.crazyit.org is good, and I love it'))
	print(re.escape(r'A-Zand0_9?'))
```

	11. 正则表达式旗标
	
		11.1. re.A或re.ASCII:该旗标只控制\w,\W,\b,\B,\d,\D,\s,\S只匹配ASCII字符，而不匹配所有的Unicode字符
		
		11.2. re.DEBUG:显示编译正则表达式的Debug信息
		
		11.3. re.I或re.IGNORECASE:使用正则表达式匹配时不区分大小写
		
```python
	import re
	print(re.findall(r'fkit','Fkit is a good domain, FKIT is good'))
	print(re.findall(r'fkit','Fkit is a good domain, FKIT is good',re.I))
```

		11.4. re.L或re.LOCALE:根据当前区域设置使用正则表达式匹配时不区分大小写，只对bytes模式起作用
		
		11.5. re.M或re.MULTLINE:多行模式
		
		11.6. re.S或s.DOALL:让(.)能匹配包含换行符在内的所有字符。
		
		11.7. re.U或re.Unicode:该旗标控制\w,\W,\b,\B,\d,\D,\s,\S匹配所有的Unicode字符，Python3.x完全是多余的，Python3.x默认匹配所有的Unicode。
		
		11.8. re.X或re.VERBOSE:允许分行书写正则表达式
		
### 创建正则表达式
	
	- 正则表达式支持的合法字符
	
| 字符 | 说明 | 
| ------------- | ------------- | 
| x | Content Cell | 
| \uhhhh | Content Cell |	
| \t | Content Cell | 
| \n | Content Cell | 
| \r | Content Cell | 
| \f | Content Cell | 
| \a | Content Cell | 
| \e | Content Cell | 
| \cx | Content Cell | 
	
	- 正则表达式中的特殊字符
	
	- 正则表达式所支持的预定义字符
	
	- 方括号表达式
	
	- 边界匹配符

##  set和frozenset集合

##  双端队列deque的功能和用法

##  Python的堆操作

##  ChainMap对象的功能和用法

##  Counter对象的功能和用法

##  defaultdict对象的功能和用法

##  命名元组的功能和用法

##  OrderedDict对象的功能和用法

##  itertools模块下的迭代器功能函数

##  functools模块下的函数修饰器和功能函数