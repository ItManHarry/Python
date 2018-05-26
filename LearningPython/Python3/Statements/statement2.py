print('-' * 80)
spam = 'Spam'
print('spam is : ', spam)
a, b = 'Harry', 'Jack'
print('a is : ', a)
print('b is : ', b)
[c, d, e] = ['C', 'D', 'E']
print('c is : ', c)
print('d is : ', d)
print('e is : ', e)
x, y, z = 'XYZ'
print('x is : ', x)
print('y is : ', y)
print('z is : ', z)
f, *g = 'ABCDE'
print('f is : ', f)
print('g is : ', g)
spam = ham = 'lunch'
print('spam is : ', spam)
print('ham is : ', ham)
spam += '42'
print('spam is : ', spam)
print('-' * 80)
nudge = 1
wink = 2
a, b = nudge, wink
print('a is : ', a)
print('b is : ', b)
[c, d] = [nudge, wink]
print('c is : ', c)
print('d is : ', d)
nudge, wink = wink, nudge
print('nudge is : ', nudge)
print('wink is : ', wink)
[a, b, c] = (1, 2, 3)
print('a is : ', a)
print('b is : ', b)
print('c is : ', c)
(a, b, c) = "ABC"
print('a is : ', a)
print('b is : ', b)
print('c is : ', c)
((a, b), c) = ('SP', 'AM')
print('a is : ', a)
print('b is : ', b)
print('c is : ', c)
print('-' * 80)
for (a, b, c) in [(1, 2, 3),(4, 5, 6),(7, 8, 9)]:
	print('\ta is : ', a)
	print('\tb is : ', b)
	print('\tc is : ', c)
	print('\t', '*' * 10)
print('-' * 80)
red, green, blue = range(3)
print('red is : ', red)
print('green is : ', green)
print('blue is : ', blue)
l = [1, 2, 3, 4]
while l :
	f, l = l[0], l[1:]
	print('f is : ', f, 'l is : ', l)
seq = [1,2,3,4]
a,b,c,d,*e = seq
print('\ta is : ', a)
print('\tb is : ', b)
print('\tc is : ', c)
print('\td is : ', d)
print('\te is : ', e)
for all in [(1,2,3,4),(5,6,7,8)]:
	a,b,c = all[0],all[1:3],all[3]
	print('a is : ', a)
	print('b is : ', b)
	print('c is : ', c)
print('-' * 80)
a = b = c = 1
b = b + 1
print('\ta is : ', a)
print('\tb is : ', b)
print('\tc is : ', c)
a = b = []
b.append(43)
print('list a is : ', a)
print('list b is : ', b)
print('-' * 80)
l = [1,2]
l.append(3)
l += [4,5]		#the same with the extend method
l.extend([7,8])	#it is very fast in this way
print('finally the list l is : ', l)
l = []
l += 'spam'
print('now the list l is : ', l)
l = l + list('harry')
print('now the list l is : ', l)
l = [1,2,3,4]
m = l
print('list l is : ', l)
print('list m is : ', m)	
l = l + [5,6]	# Concatenation makes a new object
print('list l is : ', l)
print('list m is : ', m)	
l = [1,2,3,4]
m = l
print('list l is : ', l)
print('list m is : ', m)	
l += [5,6]		#But += really means extend
print('list l is : ', l)
print('list m is : ', m)
print('-' * 80)