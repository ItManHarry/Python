print("-" * 80)
l = [123, 'spam', 1.23]
for i in l :
	print('The element is : ', i)
print("-" * 80)
print('The list length is : ', len(l))
print("-" * 80)
i = 0
while i < len(l):
	print('Index is : ', i , ', and the value is : ', l[i])
	i += 1
print('-' * 80)
print('The first element is : ', l[0])
print('The first elements are : ', l[:-1])
l2 = l + [4,5,6]
l3 = l * 2
print(l)
print(l2)
print(l3)