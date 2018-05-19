import copy
print('-' * 80)
x = [1,2,3]
l = ['a',x,'b']
d = {'x':x,'y':2}
d2 = {'x':x.copy(),'y':2}
d3 = copy.deepcopy(d)
print('List : ', l)
print('Dictionary : ', d)
print('Dictionary 2 : ', d2)
print('Dictionary 3 : ', d3)
print('-' * 80)
x[1] = 'X'
print('List : ', l)
print('Dictionary : ', d)
print('Dictionary 2 : ', d2)
print('Dictionary 3 : ', d3)
print('-' * 80)
l1 = [1,('a',3)]
l2 = [1,('a',3)]
if l1 == l2:
	print('list2 == list2(They have same values)')
else:
	print('list1 != list2')
if l1 is l2:
	print('list1 is list2(They point to the same reference)')
else:
	print('list1 is not list2(They do not point to the same reference)')
s1 = 'spam'
s2 = 'spam'
if s1 == s2 and s1 is s2:
	print('string1 and string2 are all the same(both the value and the reference)')
else:
	print('string1 and string2 are not the same')
s1 = 'a longer string'
s2 = 'a longer string'
if s1 == s2 and s1 is s2:
	print('string1 and string2 are all the same(both the value and the reference)')
else:
	print('string1 and string2 are not the same')
print('-' * 80)
l1 = [1,('a',2)]
l2 = [2,('a',3)]
print('l1 is lass than l2 : ', l1 < l2)
print('l1 equals with l2 : ', l1 == l2)
print('l1 is greater than l2 : ', l1 > l2)
print('abc is less than ac ? ', 'abc' < 'ac')
print('-' * 80)
print(bool(1))
print(bool('spam'))
print(bool(''))
print(bool({'a':1}))
print(bool(None))
print('-' * 80)
print('type of list : ', type([1]))
print('type of list : ', type([]) == list)
print('type of list : ', isinstance([1], list))
print('-' * 80)