from collections import Counter
print('-' * 80)
c1 = Counter()
print(c1)
print('-' * 80)
c2 = Counter('hahaIamHarry')
print(c2)
print('-' * 80)
c3 = Counter(['a','Go','Java','Go','Python','Groovy','Kotlin','Java','C','a'])
print(c3)
print('-' * 80)
c4 = Counter({'a':20,'b':30,'c':29})
print(c4)
print('-' * 80)
c5 = Counter(Java=100,Python=200,C=220,JavaScript=300)
print(c5)
#打印每个元素
print(list(c5.elements()))
print('-' * 80)
#求value总和
print(sum(c5.values()))
print('-' * 80)
#转换为list,只保留key
print(list(c5))
print('-' * 80)
#转换为set，至保留key
print(set(c5))
print('-' * 80)
#转换为字典dict
print(dict(c5))
print('-' * 80)
#转换为list，包含key和出现的次数
l = c5.items()
print(l)
print('-' * 80)
#将转换后的"l"再转换为Counter
c = Counter(dict(l))
print(c)
print('-' * 80)
#清空Counter
c.clear()
print(c)
print('-' * 80)
c1 = Counter(a=3,b=2,c=-1)
c2 = Counter(a=1,b=-2,c=3)
print('Count 1 is : ', c1)
print('Count 2 is : ', c2)
#执行加
print('Count1 + Counter2 : ', c1 + c2)
#执行减
print('Count1 - Counter2 : ', c1 - c2)
#交
print('Count1 & Counter2 : ', c1 & c2)
#并
print('Count1 |Counter2 : ', c1 | c2)
#求正
print('+c1 : ', +c1)
#求负
print('-c2 : ', -c2)
print('-' * 80)