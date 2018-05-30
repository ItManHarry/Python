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