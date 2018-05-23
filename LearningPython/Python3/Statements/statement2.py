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
print('-' * 80)