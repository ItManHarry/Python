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
print(d)
d['ham'] = ['grill','bake','fry']
print(d)
#delete the item
del(d['eggs'])
print(d)
d['brunch'] = 'Bacon'
print(d)
print('-' * 80)
d = {'spam':2,'ham':1,'eggs':3}
print(d)
print(list(d.values()))
print(list(d.items()))
print(d.get('spam'))
print(d.get('toast'))
print(d.get('toast', 99))
print(d)
#use update method to merge the dictionaries
d2 = {'toast':4,'muffin':5,'spam':8}
d.update(d2)
print('Now the dictionary is : ', d)
print('and the dictionary 2 is : ', d2)
#pop a dictionary by key
d.pop('toast')
print('After poped the toast , now the dictionary is : ', d)
print('-' * 80)
table = {'1975':'Holy Grail',
		 '1979':'Life of Brain',
		 '1983':'The Meaning of Life'}
year = '1975'
movie = table[year]
print('The movie in 1975 : ', movie)
for year in table:
	print('Year : ', year , ' the movie : ', table[year])
table = {'Holy Grail':'1975',
		 'Life of Brain':'1979',
		 'The Meaning of Life':'1983'}
print('The movie Holy Grail year : ',table['Holy Grail'])
print(list(table.items()))		
key = 'Holy Grail'
print('Year : ', table[key])
v = '1975'
s = [key for (key, value) in table.items() if value == v]
print(s)
s = [key for key in table.keys() if table[key] == v]
print(s)
print('-' * 80)