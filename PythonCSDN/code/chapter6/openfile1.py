#写模式打开文件，文件内容被清空
open('data.txt', 'w')
#r/r+模式打开文件，都邀请文件必须存在，否则程序报错
file = open('myfile.txt', 'rb', True)
data = file.read(4)
print(str(data, 'gbk'))