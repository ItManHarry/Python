import json
print('=' * 180)
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
#将Python对象转换为字符串，在逗号和冒号之间没有空格
s = json.dumps([1, 2, 3, {'x':4,'y':5}])
print('s is : ', s)
s = json.dumps([1, 2, 3, {'x':4,'y':5}], separators=(',',';'))
print('s is : ', s)
print('-' * 80)
#缩进
s = json.dumps({'Python':5,'Kotlin':7,'Java':10,'Groovy':8}, sort_keys=True,indent=4)
print('s is : ', s)
print('-' * 80)
#使用JSONEncoder的encode方法将Python对象转换为字符串
s = json.JSONEncoder().encode({"names":("唐僧","孙悟空","猪悟能","沙悟净")})
print('s is : ', s)
#将转换后的json字符串写入文件
f = open('data.json', 'w')
json.dump(['Java','Groovy','C',{'Python':'OK'}],sort_keys=True,indent=4, fp=f)
print('=' * 180)
#字符串转换为Python对象
r = json.loads('["Java",{"others":["C","Python","Kotlin","Groovy", 1, 2, 3]}]')
print(type(r), r)
print('-' * 80)
#文件读取JSON字符串后转换为Python对象
f = open('data.json')
r = json.load(f)
print(type(r), r)
print('-' * 80)