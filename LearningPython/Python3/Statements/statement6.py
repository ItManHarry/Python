#Iterations and Comprehensions
print('-' * 80)
for x in [1,2,3,4]:
	print(x ** 2)
for x in (1,2,3,4):
	print(x ** 3)
for x in 'spam':
	print(x * 2)
print('-' * 80)
#read file
for line in open('statement1.py'):
	print(line.upper())
print('-' * 80)
l = [1,2,3,4]
print(l)
for i in range(len(l)):
	l[i] += 10
print(l)
l2 = [x + 10 for x in l]
print(l2)
print('-' * 80)
lines = [line.rstrip() for line in open('statement1.py')]
print(lines)
lines = [line.rstrip() for line in open('statement1.py') if line[0] != 'p']
print(lines)
print('-' * 80)
fs = [x+y for x in 'abc' for y in 'xyz']
print(fs)
print('-' * 80)
fls = list(open('statement1.py'))
print(fls)
print('-' * 80)
fts = tuple(open('statement1.py'))
print(fts)
print('-' * 80)
ffs = '&&'.join(open('statement1.py'))
print(ffs)
print('-' * 80)
s = {line for line in open('statement1.py')}
print(s)
print('-' * 80)
num_sum = sum([3,2,4,1,5.0])
print(num_sum)
b = any(['spam','ni',''])
print(b)
b = all(['spam','','ni'])
print(b)
mx = max([3,2,4,5,0])
print(mx)
mn = min([3,2,4,5,0])
print(mn)
print('-' * 80)
def f(a,b,c,d):
	print(a,b,c,d,sep='&')
f(1,2,3,4)
f(*[1,2,3,4])
#f(*open('statement1.py'))
l = [x for x in ['a','','d'] if x]
print(l)
print('-' * 80)