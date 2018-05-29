# statement of whiel/for loops
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