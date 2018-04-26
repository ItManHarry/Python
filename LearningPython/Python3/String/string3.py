print('-' * 80)
s = 'spammy'
l = list(s)
for i in l :
	print("Item is : ", i)
l[3] = 'x'
l[4] = 'x'
s = ''.join(l)
print('Now the s is : ', s)
line = 'aaa bbb ccc'
c1 = line[0:3]
c2 = line[8:]
print('c1 is : ', c1)
print('c2 is : ', c2)
cols = line.split()
print(cols)
line = 'bob,hacker,40'
cols = line.split(',')
print(cols)
line = "I'mSPAMaSPAMlumberSPAMjack"
cols = line.split('SPAM')
print(cols)
line = 'The knights who says Ni!\n'
print(line)
print(line.rstrip())
print(line.upper())
print(line.lower())
print(line.isalpha())
print(line.startswith('The'))
print(line.endswith('Ni!\n'))
if line.find('Ni') != -1:				# Search via method call or expression
	print('Ni is in the line')
else:
	print('Ni is not in the line')
if 'Ni' in line:
	print('Ni is in the line')
else:
	print('Ni is not in the line')
s = 'a+b+c+d'
x = s.replace('+','x')
print(x)
print('-' * 80)
print('There is %d %s bird!' % (1, 'dead'))
e = 'Ni'
print('The knights who says %s!' %e)
print('%d %s %g you' % (1, 'spam', 4.0))
print('%s -- %s -- %s' % (42, 3.1415, [1,2,3]))
print('-' * 80)
x = 1234
res = 'integers:...%d...%-6d...%06d' %(x,x,x)
print(res)
x = 1.23456789
print(x)
print('%e | %f | %g' %(x,x,x))
print('%E' %x)
print('%-6.2f | %05.2f | %+06.1f' %(x,x,x))
print('%s' % x, str(x))
print('-' * 80)
#Dictionary-Based Formatting Expressions
print('%(qty)d more %(food)s' %{'qty':1,'food':'spam'})
reply = """
	Greeting...
	Hello %(name)s
	Your age is %(age)s
"""
values = {'name':'Harry','age':35}
print(reply % values)
food = 'spam'
qty = 10
#print(vars())
print('%(qty)d more %(food)s' % vars())
print('-' * 80)