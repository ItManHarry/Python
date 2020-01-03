#文件写入
with open('myfile2.txt','wb') as f:
	f.write('人生苦短，我用Python'.encode('utf-8'))
    
with open('myfile3.txt', 'w') as f:
    f.write('我要学习，我要成长')