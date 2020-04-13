import json
print('-' * 80)
#将Python对象转换为字符串
s = json.dumps(['Harry',{'age':37,'gender':'M'}])
print('JSON String is : ', s)
print('-' * 80)
#将Python字符串转换为JSON字符串
s = json.dumps("\"foo\bar")
print('Now the JSON String is : ', s)
print('-' * 80)
s = json.dumps('\\')
print('Now the JSON String is : ', s)
print('-' * 80)
#将Python字典对象转换为字符串并对key进行排序
s = json.dumps({'c':0,'w':3,'a':19,'b':39}, sort_keys=True)
print('Now the JSON String is : ', s)
print('-' * 80)