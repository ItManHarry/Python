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