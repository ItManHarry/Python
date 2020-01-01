#使用linecache读取文件
import linecache
try:
	print(linecache.getline('readFile5.py',2))
except:
	print('Error occured while read the file...')