print('-' * 80)
d = {'food':'Spam','quantity':4,'color':'pink'}
print(d['food'])
print(d['quantity'])
print(d['color'])
d['quantity'] += 1
print(d['quantity'])
print(d)
print('-' * 80)
#create an empty dictionary
d = {}
#give it keys and values
d['name'] = 'Harry'
d['age'] = 35
d['job'] = 'IT'
print(d)
print('-' * 80)
#create a dictionary by using 'dict' method
d = dict(name='Harry',age=35,job='IT',favor='Movies')
print(d)
print('-' * 80)
#create a dictionary by using 'dict' and 'zip' methods
d = dict(zip(['name','job','age','favor','gender'],['Harry','IT',35,'Movies','M']))
print(d)
print('-' * 80)
#nesting dictionary
d = {
	'name':{'first':'Bob','last':'Smith'},
	'jobs':['dev','mgr'],
	'age':40.5
}
print(d)
print(d['name'])
print(d['name']['last'])
print(d['jobs'])
for job in d['jobs']:
	print('Job is : ' , job)
d['jobs'].append('it')
print(d)
print('-' * 80)
#Missing the keys
d = {'a':1,'b':2,'c':3}
d['e'] = 99
print(d)
if not 'f' in d:
	print('Missing the key of f')
else:
	print(d['f'])
#check the missing key using another way
v = d.get('f', 0)
print('v is : ', v)
v = d['x'] if 'x' in d else 0
print('v is : ', v)
print('-' * 80)
#sorting the keys:for loops
ks = list(d.keys())
print(ks)
ks.sort()
print(ks)
for k in ks:
	print('The key is : ', k , ' and the value is : ', d[k])
for k in sorted(d):
	print(k, ' => ', d[k])
print('-' * 80)