# statement of while loops
print('-' * 80)
for x in ['Harry','Jack','Sam']:
	print('Name is : ', x)
print('-' * 80)
sum = 0
for x in [1,2,3,4,5]:
	sum += x
print('The total is : ', sum)
print('-' * 80)
prod = 1
for x in [1,2,3,4]:
	prod *= x
print('Prod is : ', prod)
print('-' * 80)
s = 'lumberjack'
for x in s:
	print('Letter is : ', x)
print('-' * 80)
t = ('and',' I am ',' OK!')
for x in t:
	print(x)
print('-' * 80)
t = [(1,2),(3,4),(5,6)]
for (a,b) in t:
	print(a,b)
print('-' * 80)
d = {'a':1,'b':2,'c':3}
for k in d:
	print(k, ' =>', d[k])
for (k,v) in d.items():
	print('Key is : ', k, ' value is :', v)
print('-' * 80)
print('-' * 80)
for both in [(1,2),(3,4),(5,6)]:
	a,b = both
	print(a,b)
print('-' * 80)
s = ['Harry','Jack','Sam']
for x in s:
	for c in x:	
		if c == 'c':
			print('find letter a in word[', x ,']')
			break
		else:
			print(c)
	print('finished searching work : ', x)
print('-' * 80)
#for with range
lr1 = list(range(5))
for i in lr1:
	print('Item in lr1 : ', i)
print('-' * 80)
lr2 = list(range(2,5))
for i in lr2:
	print('Item in lr2 : ', i)
print('-' * 80)
lr3 = list(range(1,10,2))
for i in lr3:
	print('Item in lr3 : ', i)
print('-' * 80)
lr4 = list(range(-5, 5))
print(lr4)
lr5 = list(range(5,-5,-1))
print(lr5)
print('-' * 80)
s = 'spam'
for i in range(len(s)):
	print('(',i, ')Character : ', s[i])
print('-' * 80)
for i in range(len(s)):
	s = s[1:] + s[:1]
	print(s)
print('-' * 80)
for i in range(len(s)):
	x = s[i:] + s[:i]
	print(x)
print('-' * 80)
s = 'abcdefghijk'
for i in range(0, len(s), 2):
	print('Character : ', s[i])
print('-' * 80)
l = [1,2,3,4,5]
for x in l:
	x += 1
print(l)
print(x)
for i in range(len(l)):
	l[i] += 1
print('Now the is : ', l)
print('-' * 80)
#for with zip
l1 = [1,2,3,4]
l2 = [5,6,7,8]
l3 = [9,10,11,12]
for (a,b) in zip(l1,l2):
	print(a,b,'--', a+b)
print(list(zip(l1,l2,l3)))
d = {'spam':1,'eggs':2,'toast':3}
print(d)
k = ['spam','eggs','toast']
v = [1,2,3]
d = {}
for zk,zv in list(zip(k,v)):
	d[zk] = zv
print(d)
print('-' * 80)
#for with enumerate
s = 'spam'
for (offset, item) in enumerate(s):
	print(item, 'appears at offset : ', offset)
print('-' * 80)