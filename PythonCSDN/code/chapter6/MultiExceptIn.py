f = None
try:
	f = open('abc.txt')
	print(f.read())
except:
	print('exception happened...')
finally:
	#程序判断文件是否存在，存在才close
	if f:
		#此处即为异常的嵌套
		try:
			f.close()
		except:
			print('close file failed...')