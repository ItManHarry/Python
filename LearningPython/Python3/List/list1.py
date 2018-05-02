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
l = ['spam','Spam','SPAM']
print(l[2])
print(l[-2])
print(l[1:])
l[1] = 'eggs'
print(l)
l[0:2] = ['eat','more']
print(l)
print('-' * 80)
ml = [[1,2,3],[4,5,6],[7,8,9]]
print(ml[1])
print(ml[1][1])
print(ml[2][0])
print('-' * 80)
l = [1,2,3]
l[1:2] = [4,5]
print(l)
l[1:1] = [6,7]
print(l)
l[1:2] = []
print(l)
print('-' * 80)
l = [1]
l[:0] = [2,3,4]
print(l)
l[len(l):] = [5,6,7]
print(l)
l.extend([8,9,10])
print(l)
print('-' * 80)
l = ['eat','more','SPAM!']
l.append('please')
print(l)
l.sort()
print(l)
print('-' * 80)
l = ['abc','ABD','aBe']
l.sort()
print(l)
l.sort(key=str.lower)
print(l)
l.sort(key=str.lower,reverse=True)
print(l)
l = ['abc','ABD','aBe']
print(sorted(l, key=str.lower, reverse=True))
print(l)
print(sorted([x.lower() for x in l], reverse=True))
print('-' * 80)
l = [1,2]
l.extend([3,4,5,6])
print(l)
l.pop()
print(l)
l.reverse()
print(l)
print(list(reversed(l)))
print(l)
l = []
l.append(1)
l.append(2)
print(l)
l.pop()
print(l)
print('-' * 80)
l = ['spam','eggs','ham']
print(l.index('eggs'))
l.insert(1, 'toast')
print(l)
l.remove('eggs')
print(l)
l.pop(1)
print(l)
print(l.count('spam'))
print('-' * 80)
l = ['spam','eggs','ham','toast']
del(l[0])
print(l)
del(l[1:])
print(l)
l = ['Already','got','one']
l[1:] = []
print(l)
l[0] = []
print(l)
print('-' * 80)