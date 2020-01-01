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