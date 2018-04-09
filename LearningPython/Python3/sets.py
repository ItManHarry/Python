print('-' * 80)
x = set('spam')
y = {'h','a','m'}
print(x, y)
print('-' * 80)
#get the same elements
s = x & y
print(s)
#union all
s = x | y
print(s)
#find the different elements
d = x - y
print(d)
#superset
print(x > y)
s = {x ** 2 for x in [1,2,3,4]}
print(s)
print('-' * 80)
l = list(set([1,2,3,1,4,2,1]))
print(l)
s = set('spam') - set('ham')
print(s)
print(set('spam') == set('aspm'))
print('p' in set('spam'), 'p' in 'spam', 'ham' in ['eggs','spam','ham'])
print('-' * 80)