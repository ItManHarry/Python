#文件读取 - 字节读取
try:
	file = open('myfile.txt','rb')
	data = file.read(8)
	print(str(data,'gbk'))
except OSError as e:
	print(e)
finally:
    if 'file' in globals():
        print('close the file')
        file.close()