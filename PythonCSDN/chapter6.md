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