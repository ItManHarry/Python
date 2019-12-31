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