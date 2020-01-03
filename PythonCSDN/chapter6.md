# Chapter6 - 文件操作

## 打开文件

- open函数

	格式如下：
	
		open(file_name, [access_mode],[buffering])
		
- 文件操作模式

	1. r：读模式
	
	2. w：写模式
	
	3. a：追加模式
	
	4. +：读写（更新）模式，可与其他模式混合使用，如何r+代表读取模式，w+也代表读写模式
	
	5. b：二进制模式，可与其他模式混合使用，如何rb+表示二进制，wb+也表示二进制读写
	
- 使用w/w+/a/a+模式打开文件，文件可以不存在，程序会自动创建

```python
	#写模式打开文件，文件内容被清空
	open('data.txt', 'w')
	#r/r+模式打开文件，都邀请文件必须存在，否则程序报错
	open('myfile.txt', 'a')
```

- 如果没有指定b默认，以字符为单位执行读写文件，如果指定了b模式，则以字节为单位进行文件读写

- open()函数的第三个参数为0或者False，那么打开文件是不带有缓冲的，如果为1或者True时，此时文件读写是带有缓冲的，I/O性能会比较好。

## 按字节读取文件

	b模式下读取文件，
	
	read(n)读取那个字节的数据，如果不指定n，默认读取全部的文件。
	
```python
	#文件读取 - 字节读取
	try:
		file = open('myfile.txt','rb')
		data = file.read(8)
		print(str(data,'gbk'))
	except OSError as e:
		print(e)
		print(e.args)
		print(e.errno)
		print(e.strerror)
	finally:
		if 'file' in globals():
			print('close the file')
			file.close()
```

	字符模式读取文件：
	
```python
	#文件读取 - 字符读取
	try:
		file = open('myfile.txt','r')
		data = file.read(6)
		print(data)
	except OSError as e:
		print(e)
	finally:
		if 'file' in globals():
			print('close the file')
			file.close()
```

- 按行读取文件

	如果文件是文本文件，则可以按行读取，文件对象提供了两个方法读取行
	
	1. readline([n])：读取一样内容，如果指定了参数n，则读取该行的n个字符
	
	2. readlines()：读取所有的行
	
```python
	#按行读取文件 - 逐行读取
	try:
		f = open('myfile.txt')
		while True:
			line = f.readline()
			if not line:
				break
			print(line)
	except:
		print('Error occured while reading the file...')
	finally:
		if f in globals():
			f.close()
			
	#按行读取文件 - 读取全部行
	try:
		f = open('myfile.txt')
		lines = f.readlines()
		print(lines)
		for line in lines:
			print(line)
	except:
		print('Error occured while reading the file...')
	finally:
		if f in globals():
			f.close()
```	

- 文件迭代器

	1. 文件本身就是可以迭代的，因此程序可以可以使用for-in循环进行文件的读取
	
	2. 也可使用list()函数将文件转换为列表，就像readlines()方法返回值一样
	
```python
	#读取文件 - 文件迭代器
	try:
		f = open('myfile.txt')
		for line in f:
			print(line)
	except:
		print('Error occured while read the file...')
	finally:
		if 'f' in globals():
			f.close()
```

- 使用linecache读取文件：该模块主要读取Python源文件，编码为utf-8

```python
	#使用linecache读取文件
	import linecache
	try:
		print(linecache.getline('readFile5.py',2))
	except:
		print('Error occured while read the file...')
```

- 管道输入

	管道的作用：把前一个命令的输出，作为下一个命令的标准输入
	
	管道输入的语法如下：
		
		cmd1|cmd2|cmd3...
		
	Python的标准输入：
	
		sys.stdin

- with语句

	with语句用以管理资源关闭
	
	比如：如果把打开的文件放到with语句中，with语句会自动关闭文件
	
```python
	#使用with语句打开文件，with会自动关闭文件资源
	with open('myfile.txt') as f:
		for line in f:
			print(line)
```

	使用with语句管理的资源必须是一个实现了上下文管理协议（context manage protocol）的类，实现上下文管理协议的类必须实现以下两个方法：
	
	1. context_manager.__enter__():进入上下文资源管理器自动调用的方法
	
	2. context_manager.__exit__(exc_type,exc_value,exc_traceback):退出上下文资源管理器自动调用的方法```python
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
```

- 文件指针与文件写入

	1. 文件指针
	
		1.1 seek(offset[,whence]):该方法把文件指针指到某个位置
		
		1.2. tell():判断文件的指针位置
		
```python
	#文件指针
	with open('myfile.txt') as f:
		#whence为0 ， 从头计算移动
		print(f.tell())
		f.seek(3)
		print(f.tell())
		#whence为1， 从当前计算移动
		f.seek(4,1)
		print(f.tell())
		#whence为2， offset为0，移动到文件末尾
		f.seek(0,2)
		print(f.tell())
		#whence为2， offset为-10，从文件末尾移动到倒数第十位
		import os
		print(os.path.getsize('myfile.txt'))
		f.seek(-10, 2)
		print(f.tell())
```
		1.3. 写入有两种方式
		
			A: write(str/bytes):输出字符串或者字节串。只有以二进制打开的文件才能输出字节串
			
```python
	#文件写入 - write
	with open('myfile2.txt','wb') as f:
		f.write('人生苦短，我用Python'.encode('utf-8'))
```
			
			B: writelines(可迭代对象)：输出多个字符串或者字节串
			
```python
	#文件写入 - writelines
	import os
	with open('myfile4.txt', 'wb') as f:
		f.writelines((('人生苦短'+os.linesep).encode('gbk'),('我用Python'+os.linesep).encode('gbk'),('学习让我不断进步'+os.linesep).encode('gbk')))
```
		
	2. 文件写入