print('-' * 80)	
l = [1,2,3]
print('Length of the list l is : ', len(l))	# Length
l += [4,5,6]								# Concatenation
print('Now the list l is : ', l , ' ,and the length is : ', len(l))
l = l * 4									# Repetition
print('Now the list l is : ', l , ' ,and the length is : ', len(l))
print('-' * 80)
print(str([1,2]) + "34")					# concatenate string and list by str method
print([1,2] + list('34'))					# concatenate list and string by list method
print('-' * 80)
print('There are ', l.count(3) , ' 3s in the list l' )
if 3 in l:
	print('3 is in the list l ')
else:
	print('3 i not in the list l ')
# lterate the list
for i in l :
	print('list l item : ', i)
s = set(l)		# get unique items by using set object
print(s)
#list comprehensions
res = [c * 4 for c in 'SPAM']
print(res)
res = list(map(abs, [-1,-2,0,1,2]))
print(res)
print('-' * 80)