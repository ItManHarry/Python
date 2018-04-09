l = [None] * 100
print(l)
print(type(l))
print(type(type(l)))
if type(l) == type([]):
	print('Yes , l is a list')
if type(l) == list:
	print('Sure, l is a list')
if isinstance(l, list):
	print('I said, l is a list')