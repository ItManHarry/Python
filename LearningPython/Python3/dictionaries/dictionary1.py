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
#Other Ways to Make Dictionaries
d = {}
d['name'] = 'Harry'
d['age'] = 35
print(d)
d = dict(name='Bob',age=26)
print('Now the d is : ', d)
d = dict([('name','Jack'),('age',40)])
print('After change the dictionary now is : ', d)
#create a dictionary by using fromkeys method:the values are all the same
d = dict.fromkeys(['a','b','c'],100)
print('Dictionary created by fromkeys method : ', d)
#create a dictionary by zip method
d = dict(zip(['a','b','c'],[1,2,3]))
print(d)
for k in d.keys():
	print('Key is : ', k , ' value : ', d[k])
d = {x:x**2 for x in [1,2,3,4]}
print(d)
d = {c:c*4 for c in 'SPAM'}
print(d)
d = {c.lower():c+'!' for c in ['AAA','BBB','CCC']}
print(d)
d = dict.fromkeys('spam')
print(d)
d = dict(a=1,b=2,c=3)
print(d)
k = d.keys()
print(k)
l = list(k)
print(l)
v = d.values()
print(v)
print(list(v))
for k in d.keys():
	print('Key is : ', k , ' value is : ', d[k])
for k in d:
	print('Key is : ', k , ' value is : ', d[k])

print('-' * 80)