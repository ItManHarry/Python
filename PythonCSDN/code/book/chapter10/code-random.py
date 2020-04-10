import random
print('-' * 80)
#生成大于等于0.0小于1.0的伪随机浮点数
v1 = random.random()
print('v1 is : ', v1)
print('-' * 80)
#生成大于等于2.5小于10.0的伪随机浮点数
v2 = random.uniform(2.5, 10.0)
print('v2 is : ', v2)
print('-' * 80)
#生成大于等于5小于等于20的随机数
v3 = random.randint(5, 20)
print('v3 is : ', v3)
print('-' * 80)
#生成0到10的伪随机整数
v4 = random.randrange(10)
print('v4 is : ', v4)
print('-' * 80)
#生成0到100的随机偶数
v5 = random.randrange(0, 101, 2)
print('v5 is : ', v5)
print('-' * 80)
#随机抽取数组元素
vl = ['Java','Python','C','Kotlin','Groovy']
v6 = random.choice(vl)
print('v6 is : ', v6)
print('-' * 80)
#对列表进行随机排序
print('Before sort : ', vl)
random.shuffle(vl)
print('After sort : ', vl)
print('-' * 80)
#随机抽取n个独立元素
nvl = random.sample(vl, k = 3)
print('Sample list is : ', nvl)
print('-' * 80)