try:
	a = int(input('Number A:'))
	b = int(input('Number B:'))
	print('a / b is : ', a / b)
except (ValueError, ArithmeticError) as e:
	print(e)
	print(type(e))