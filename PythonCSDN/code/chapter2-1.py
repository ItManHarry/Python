#创建列表、生成随机大写字符，插入到列表中
NUM = 10
# 方式一
#创建空列表
list = []
#生成随机大写字母
import random
for i in range(NUM):
    n = random.randint(65, 90)
    #转换为字符并添加到列表中
    list.append(chr(n))
print('List : ', list)
print('-' * 80)
#方式二 列表推导式
#result = ['表达式' for i in range(NUM)]
result = [chr(random.randint(65, 90)) for i in range(NUM)]
print('Result : ', result)
print('-' * 80)
#方式三 
import numpy
result = [chr(a) for a in numpy.random.randint(65, 90, [NUM, 1])]
print('Result ', result)