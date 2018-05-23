import sys
import random
print('-' * 80)
print('OS is : ', sys.platform)
print('Random number is : ', random.random())
print('Random choice is : ', random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print('-' * 80)
s = 'Spam'
print('s length is : ', len(s))
print(s[2])
print(s[1:3])
print(s[:3])
print(s[:])
l = list(s)
print(l)
print(','.join(l))
print(s.find('pa'))
print(s.replace('pa', 'xy'))
print(s)
s = 'aaa,bbb,ccc'
l = s.split(',')
print(l)
s = 'abc\n'
print(s)
print(s.rstrip())
print('lower is : %s, upper is : %s.' %('spam','SPAM'))
print('lower is : {0}, upper is : {1}.'.format('spam','SPAM'))
print('lower is : {}, upper is : {}.'.format('spam','SPAM'))
print('-' * 80)
l = [1,2,3]
print(len(l))
l.append(4)
print(l)
i = 0
while i < len(l):
	print('Element is : ', l[i])
	i += 1
print(l.pop())
print(l.pop(1))
print(l)
l.append(5)
l.append(4)
l.append(9)
l.append(7)
l.append(6)
print(l)
print('from zero to four : ', l[:4])
print('from two to the end : ', l[2:])
l.sort()
print(l)
l.reverse()
print(l)
s = 'abcdefg'
l = list(s)
print(l)
l = list(range(1,10,2))
print(l)
l = [[x * 2, x * 3] for x in range(5)]
print(l)
l = [ord(x) for x in 'spam']
print(l)
print('-' * 80)
