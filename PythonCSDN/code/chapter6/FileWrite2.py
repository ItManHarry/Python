#文件写入 - writelines
import os
with open('myfile4.txt', 'wb') as f:
	f.writelines((('人生苦短'+os.linesep).encode('gbk'),('我用Python'+os.linesep).encode('gbk'),('学习让我不断进步'+os.linesep).encode('gbk')))