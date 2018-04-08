print('-' * 80)
t = (1,2,3,4,4)
print(t)
for e in t:
	print('Element is : ', e)
t = t + (5,6)
print(t)
print('The first element is : ', t[0])
#index of the element
print('Element "4" index is : ', t.index(4))
#count the element
print('The element "4" appears ', t.count(4), ' times.')
print('-' * 80)
t = (2,3) + t[1:]
print(t)
print('-' * 80)
#the parentheses can be omitted
t = '', 3.0, [11,22,33]
print(t)
print(t[1])
print(t[2][1])
print('-' * 80)