x = range(1,10)
y = map(lambda i: i ** 3, x)
for i , value in enumerate(y):
	print('{}^3 = {}'.format(i, value))
y = {k:k**3 for k in x}
for k in y:
	print('Key is : ', k, ' Value is : ', y[k])