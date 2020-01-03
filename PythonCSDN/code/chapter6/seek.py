#文件指针
with open('myfile.txt') as f:
	print(f.tell())
    f.seek(3)
    print(f.tell())