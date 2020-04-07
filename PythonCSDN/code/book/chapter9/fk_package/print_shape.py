'''
	打印空心三角形
'''
def print_blank_triangle(n):
	if n < 0:
		raise ValueError('n必须大于零')
	for i in range(n):
		print(' ' * (n - i - 1), end='')
		print('*', end=' ')
		if i != n-1:
			print(' ' * (2*i-1),end='')
		else:
			print(' *' * (2*i-1),end='')
		if i != 0:
			print('*')
		else:
			print('')