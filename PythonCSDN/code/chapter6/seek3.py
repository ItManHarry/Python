#文件指针
with open('myfile.txt') as f:
	#whence为0 ， 从头计算移动
	print(f.tell())
	f.seek(3)
	print(f.tell())
	#whence为1， 从当前计算移动
	#f.seek(4,1)
	print(f.tell())
	#whence为2， offset为0，移动到文件末尾
	f.seek(0,2)
	print(f.tell())
	#whence为2， offset为-10，从文件末尾移动到倒数第十位
	import os
	print(os.path.getsize('myfile.txt'))
	#f.seek(-10, 2)
	print(f.tell())