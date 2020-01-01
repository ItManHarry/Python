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