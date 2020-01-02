#默认情况下，sys.stdin从键盘读取
#如果使用管道输入后，sys.stdin将改为从上一个程序的输出来读取
#将javac命令输出包含'module'的行打印出来
import sys
for line in sys.stdin:
	if 'module' in line:
		print(line)