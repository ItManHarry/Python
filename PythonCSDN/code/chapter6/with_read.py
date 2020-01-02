#使用with语句打开文件，with会自动关闭文件资源
with open('myfile.txt') as f:
	for line in f:
		print(line)