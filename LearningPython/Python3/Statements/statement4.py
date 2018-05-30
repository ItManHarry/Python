# statement of while loops
print('-' * 80)
#while True:
	#print('print CTRL+C to stop me!!!')
x = 'spam'
while x:
	if len(x) == 1:
		print(x)
	else:
		print(x, end=' ')
	x = x[1:]
print('-' * 80)
a = 0
b = 10
while a < b:
	if a == b - 1:
		print(a)
	else:
		print(a, end=' ')
	a += 1
print('-' * 80)
#continue , break, pass
x = 10
while x:
	x -= 1
	if x % 2 != 0:
		continue
	print(x)
print('-' * 80)
while True:
	age = input("Please input age : ")
	if age == 'stop':
		print('Game over!!!')
		break
	try:
		print('Number is : ', int(age))
	except:
		print('Bad input...')
print('-' * 80)
y = input('Give me a number : ')
y = int(y)
x = y // 2
while x > 1:
	if y % x == 0:
		print(y, 'has factor', x)
		break
	x -= 1
else:
	print(y, 'is prime')
print('-' * 80)