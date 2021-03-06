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
| x | 字符x(x可代表任意合法的字符) | 
| \uhhhh | 十六进制0xhhhh所表示的Unicode字符 |	
| \t | 制表符('\u0009') | 
| \n | 新行(换行)符('\u000A') | 
| \r | 回车符('\u000D') | 
| \f | 换页符('\u000C') | 
| \a | 报警(bell)符('\u0007') | 
| \e | Escape符('\u001B') | 
| \cx | x对应的控制符。例如：\xM匹配ctrl+M。x值必须为A~Z或a~z之一 | 
	
	- 正则表达式中的特殊字符
	
| 特殊字符 | 说明 | 
| ------------- | ------------- | 
| $ | 匹配一行的结尾 | 	
| ^ | 匹配一行的开头 | 	
| () | 标记子表达式的开始位置和结束位置 | 	
| \[\] | 用于确定中括号表达式的开始位置和结束位置 | 	
| {} | 用于标记前表达式出现频度 | 	
| \* | 指定前面子表达式出现零次或多次 | 	
| + | 指定前面子表达式出现一次或多次 | 		
| ? | 指定前面子表达式出现零次或一次 | 	 	
| . | 匹配除换行符\n之外的所有字符 | 	
| \\ | 用于转义下一字符，或指定八进制、十六进制字符 | 	
| \| | 指定两项之间任选其一 | 	
	
	- 正则表达式所支持的预定义字符
	
| 预定义字符 | 说明 | 
| ------------- | ------------- | 
| . | 匹配除换行符\n之外的所有字符，使用re.S或s.DOTALL后，还可匹配换行符 | 
| \d | 匹配0~9的所有数字 | 	
| \D | 匹配非数字 | 	
| \s | 匹配所有的空白字符，包括空格、制表符、回车符、换页符、换行符等 | 	
| \S | 匹配所有的非空白字符 | 	
| \w | 匹配所有的单词字符，包括0~9的所有数字、26个英文字母和下划线(_) | 	
| \W | 匹配所有的非单词字符 | 
	
	- 方括号表达式
	
| 方括号表达式 | 说明 | 
| ------------- | ------------- | 
| 表示枚举 | \[abc\]:表示a,b,c其中的任一字符 | 
| 表示范围 | \[a-f\]:表示a~f范围内的任一字符 | 	
| 表示求否:^ | \[^abc\]:表示非a,b,c的任意字符 | 
	
	- 边界匹配符

| 边界匹配符 | 说明 | 
| ------------- | ------------- | 
| ^ | 行的开头 | 
| $ | 行的结尾 | 	
| \b | 单词的边界，即只匹配单词前后的空白 | 	
| \B | 单词的边界，即只匹配单词前后的空白 | 	
| \A | 只匹配字符串的开头 | 	
| \Z | 只匹配字符串的结尾，仅用于最后的换行符 | 	

##  set和frozenset集合

	set集合的特征：
	
	1. set不记录元素的添加顺序
	
	2. set的元素不允许重复
	
```python
	#set集合
	#创建方式一:{}直接创建
	print('-' * 120)
	set1 = {'a','b','c',34,(10,20,30)}
	#添加元素
	set1.add('Harry')
	set1.add('Jack')
	set1.add('Python')
	print('Set 1 length is : ', len(set1))
	for e in set1:
		print('Element : ' , e)
	#删除元素
	set1.remove(34)
	#如果删除不存在的元素，程序报错Keyerror,但是使用discard方法不会报错
	#set1.remove(88)
	set1.discard(99)
	print('Now the set length is : ', len(set1))
	#判断元素是否在set中
	print('JJJ is in set ? ', 'JJJ' in set1)
	print('-' * 120)
	#创建方式二：使用set()函数创建
	set2 = set()
	#添加元素 - 添加的元素只能是不可变元素，列表/字典是不可以添加的
	#以下添加会报错（TypeError: unhashable type: 'list'）
	#set2.add([1,2,3,4])
	#set2.add({"OK":200,"NOTFOUND":404})
	set2.add('Java')
	set2.add(123)
	set2.add((10,20,30))
	set2.add('''
		This is a 
		multyline
		text
	''')
	set2.add('Python')
	print('Set2 length is : ', len(set2))
	for e in set2:
		print('Element : ', e)
	print('-' * 120)
	#子集合判断：issubset或<=
	print('set1 is subset of set2 ? ', set1.issubset(set2))
	print('set1 is subset of set2 ? ', set1 <= set2)
	print('-' * 120)
	#父集合判断：issuperset或>=
	print('set1 is superset of set2 ? ', set1.issuperset(set2))
	print('set1 is superset of set2 ? ', set1 >= set2)
	print('-' * 120)
	#set1和set2相减：difference或-号，此时set1不受影响
	print('set1 : ', set1)
	set3 = set1 - set2
	print('set1 after - operation :: ', set1)
	set4 = set1.difference(set2)
	print('set1 after difference operation : ', set1)
	print('set2 : ', set2)
	print('set1 - set2(use - ) : ', set3)
	print('set1 - set2(use difference) : ', set4)
	#使用difference_update会改变set1，此方法为void方法。即：差异后的set赋给了set1，此处set5为空
	set5 = set1.difference_update(set2)
	print('set1 - set2(use difference_update) : ', set5)
	print('set1 : ', set1)
	print('-' * 120)
	print('Now set1 is : ', set1)
	print('Now set2 is : ', set2)
	set1.add('Java')
	set1.add('Python')
	#获取两个集合的合集：intersection或&,set1不会发生改变
	print('-' * 120)
	print('Before intersection set1 is : ', set1)
	print('Before intersection set2 is : ', set2)
	set6 = set1.intersection(set2)
	print('Intersected set6 is : ', set6)
	set7 = set1 & set2
	print('Intersected set7 is : ', set7)
	print('After intersection set1 is : ', set1)
	print('After intersection set2 is : ', set2)
	print('-' * 120)
	#使用difference_update会改变set1，此方法为void方法。即：差异后的set赋给了set1，此处set8为空
	set8 = set1.intersection_update(set2)
	print('Now the set1 is : ', set1)
	print('Now the set2 is : ', set2)
	print('set8 is : ', set8)
	print('-' * 120)
	#将range封装成set
	set1 = set(range(5))
	set2 = set(range(3,7))
	set2.add(5)
	set2.add(6)
	set2.add(7)
	print('set1 is : ', set1)
	print('set2 is : ', set2)
	#异或运算
	set9 = set1 ^ set2
	print('set9 is : ', set9)
	#计算两个集合的并集，不改变set1
	set10 = set1.union(set2)
	print('set10 is : ', set10)
	#计算两个集合的并集，改变set1,set11为空
	set11 = set1.update(set2)
	print('After update set1 is : ', set1, ', set11 is : ' , set11)
	print('-' * 120)
```
	
	frozenset是set的不可变版本，它有两个主要的作用：
	
	1. 当集合元素不需要改变时，使用frozenset代替set更安全
	
	2. 当某些API需要不可变对象时，必须使用frozenset代替set。
	
```python
	#frozenset
	fset = frozenset('Kotlin')
	tmp = {'Java'}
	#以下程序报错：AttributeError: 'frozenset' object has no attribute 'add'
	#fset.add('Groovy')
	#set.add(tmp)
	print('-' * 120)
```

##  双端队列deque的功能和用法

```python
	from collections import deque
	print('-' * 80)
	stack = deque(('Kotlin','Python'))
	stack.append('Erlang')
	stack.append('Swift')
	stack.append('Groovy')
	print('Elements in stack : ',stack)
	#执行pop，后添加的元素先出栈
	print(stack.pop())
	print(stack.pop())
	print(stack.pop())
	print(stack.pop())
	print('After pop , now the stack is : ',stack)
	print('-' * 80)
	#清空栈
	stack.clear()
	print('Stack has been cleared : ', stack)
	#添加元素
	stack.append('A')
	stack.append('B')
	stack.append('C')
	stack.insert(2, 'D')
	print('Now the stack is : ', stack)
	print('-' * 80)
	#执行popleft，先添加的元素先出栈
	print(stack.popleft())
	print(stack.popleft())
	print(stack.popleft())
	print('Now the stack is : ', stack)
	print('-' * 80)
	#rotate方法，交换收尾元素
	stack.append('A')
	stack.append('B')
	print('Before rotate', stack)
	stack.rotate()
	print('After rotate', stack)
```

##  Python的堆操作

```python
	from heapq import *
	print('-' * 80)
	lt = list(range(10))
	lt.append(0.5)
	#list data
	print(type(lt))
	print(lt)
	print('-' * 80)
	#将list转换为堆
	heapify(lt)
	print(type(lt))
	print(lt)
	print('-' * 80)
	heappush(lt, 7.2)
	print(lt)
	print(heappop(lt))
	print(heappop(lt))
	print('Now the list is : ', lt)
	print('-' * 80)
	#heapreplace:弹出最小元素，压入指定元素
	print(heapreplace(lt, 8.1))
	print('After replace : ', lt)
	print('-' * 80)
	#输出最大的三个元素
	print('Three largest elements : ', nlargest(3, lt))
	#输出最小的三个元素
	print('Three largest elements : ', nsmallest(3, lt))
	print('-' * 80)
```

##  ChainMap对象的功能和用法

```python
	from collections import ChainMap
	import builtins
	import os, argparse
	print('-' * 80)
	a = {'Kotlin':90,'Python':86}
	b = {'Go':93,'Python':92}
	c = {'Swift':89,'Go':87}
	cm = ChainMap(a,b,c)
	print('ChainMap : ', cm)
	print('Python : ', cm['Python'])
	print('Go : ', cm['Go'])
	print('-' * 80)
	my_name = 'Harry'
	def test():
		my_name = 'Jack'
		pylookup = ChainMap(locals(), globals(), vars(builtins))
		print(pylookup['my_name'])
		print(pylookup['len'])
	test()    
	print('-' * 80)
	defaults = {'color':'Blue','user':'Harry'}
	parser = argparse.ArgumentParser()
	parser.add_argument('-u','--user')
	parser.add_argument('-c','--color')
	namespace = parser.parse_args()
	command_line_args = {k:v for k,v in vars(namespace).items() if v}
	combined = ChainMap(command_line_args, os.environ, defaults)
	print(combined['color'])
	print(combined['user'])
	print('-' * 80)
```

##  Counter对象的功能和用法

```python
	from collections import Counter
	print('-' * 80)
	c1 = Counter()
	print(c1)
	print('-' * 80)
	c2 = Counter('hahaIamHarry')
	print(c2)
	print('-' * 80)
	c3 = Counter(['a','Go','Java','Go','Python','Groovy','Kotlin','Java','C','a'])
	print(c3)
	print('-' * 80)
	c4 = Counter({'a':20,'b':30,'c':29})
	print(c4)
	print('-' * 80)
	c5 = Counter(Java=100,Python=200,C=220,JavaScript=300)
	print(c5)
	#打印每个元素
	print(list(c5.elements()))
	print('-' * 80)
	#求value总和
	print(sum(c5.values()))
	print('-' * 80)
	#转换为list,只保留key
	print(list(c5))
	print('-' * 80)
	#转换为set，至保留key
	print(set(c5))
	print('-' * 80)
	#转换为字典dict
	print(dict(c5))
	print('-' * 80)
	#转换为list，包含key和出现的次数
	l = c5.items()
	print(l)
	print('-' * 80)
	#将转换后的"l"再转换为Counter
	c = Counter(dict(l))
	print(c)
	print('-' * 80)
	#清空Counter
	c.clear()
	print(c)
	print('-' * 80)
	c1 = Counter(a=3,b=2,c=-1)
	c2 = Counter(a=1,b=-2,c=3)
	print('Count 1 is : ', c1)
	print('Count 2 is : ', c2)
	#执行加
	print('Count1 + Counter2 : ', c1 + c2)
	#执行减
	print('Count1 - Counter2 : ', c1 - c2)
	#交
	print('Count1 & Counter2 : ', c1 & c2)
	#并
	print('Count1 |Counter2 : ', c1 | c2)
	#求正
	print('+c1 : ', +c1)
	#求负
	print('-c2 : ', -c2)
	print('-' * 80)
```

##  defaultdict对象的功能和用法

```python
	from collections import defaultdict
	print('-' * 80)
	#普通字典
	sd = {}
	#默认值字典 - 值默认为int类型的值
	dd = defaultdict(int)
	#访问不存在的key
	#普通字典报错，[KeyError: 'a']
	#print('Simple dict : ', sd['a'])
	print('Default dict : ', dd['a'])
	print('-' * 80)
	#设置默认值
	s = [('Python',1,100),('Java',3,200),('Python',4,300),('Groovy',5,400),('Java', 5,500),('Groovy',20,600)]
	for e1,e2,e3 in s:
		print('Element 1 : ',e1,', element 2 : ',e2,',element 3 : ',e3)
	print('-' * 80)
	s = [('Python',1),('Java',3),('Python',4),('Groovy',5),('Java', 5),('Groovy',20)]
	for k, v in s:
		print('Key is : ', k, ', value is : ', v)
	#方式一：普通字典
	d = {}
	for k, v in s:
		d.setdefault(k, []).append(v)
	print(list(d.items()))    
	#方式二：默认值字典
	d = defaultdict(list)
	for k,v in s:
		d[k].append(v)
	print(list(d.items()))    
	print('-' * 80)
```

##  命名元组的功能和用法

```python
	from collections import namedtuple
	print('-' * 80)
	#定义命名元组类
	Point  = namedtuple('Point',['x','y'])
	#初始化Point对象，即可用位置参数，也可用命名参数
	p = Point(11, y = 12)
	#普通元组方式访问元素
	print('Element 0 : ', p[0], ', Element 1 : ',  p[1])
	print('-' * 80)
	#执行解包
	x,y = p
	print('x is : ', x, 'y is : ', y)
	print('-' * 80)
	#根据字段名访问元素
	print('Element x : ', p.x, ', Element y : ',  p.y)
	print(p)
	print('-' * 80)
	#data
	data = ['East','North']
	p = Point._make(data)
	print(p)
	print('-' * 80)
	#转化为orderedDict
	print(p._asdict())
	print('-' * 80)
	#更改某个元素值
	p._replace(y='South')
	print(p._replace(y='South'))
	print('-' * 80)
	Color = namedtuple('Color', ['red','green','blue'])
	Pixel = namedtuple('Pixel', Point._fields+Color._fields)
	p = Pixel(11,12,255,119,128)
	print(p)
	print('-' * 80)
```

##  OrderedDict对象的功能和用法

```python
	from collections import OrderedDict
	print('-' * 80)
	dx = OrderedDict(b=5,c=3,a=6)
	print(dx)
	print('-' * 80)
	dx = OrderedDict()
	dx['a'] = 100
	dx['t'] = 300
	dx['e'] = 490
	dx['c'] = 590
	for k,v in dx.items():
		print('Key is : ', k, ' ,Value is : ', v)
	print('-' * 80)
```

##  itertools模块下的迭代器功能函数

	1. 排列组合工具函数
	
		1.1. product(p, q, ...[repeat=1]) : 用序列p、q、......中的元素进行排列组合
		
		1.2. permutations(p[,r]) : 从序列p中取出r个元素组成全排列
		
		1.3. combinations(p, r): 从序列p中取出r个元素组成全排列，元素不允许重复
		
		1.4. combinations_with_replacement(p, r): 从序列p中取出r个元素组成全排列，元素允许重复
	
##  functools模块下的函数修饰器和功能函数