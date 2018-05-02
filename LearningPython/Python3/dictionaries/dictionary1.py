print('-' * 80)
print(type({}))
d = {'spam':2,'ham':1,'eggs':3}
print(d['spam'])
print(d)
print(len(d))
if 'ham' in d:
	print('Key ham is in the dictionary')
else:
	print('Key ham is not in he dictionary')
print(list(d.keys()))
print('-' * 80)