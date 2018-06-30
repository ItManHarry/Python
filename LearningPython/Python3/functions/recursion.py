#recursion
def mysum1(l):
	print(l)
	if not l:
		return 0
	else:
		return l[0] + mysum1(l[1:])
#test the function
s1 = mysum1([1,2,3,4,5,6])
print('Sum is : ', s1)
def mysum2(l):
	print(l)
	return 0 if not l else l[0] + mysum2(l[1:])
s2 = mysum2([1,2,3,4,5,6])
print('Sum is : ', s2)
def mysum3(l):
	print(l)
	return l[0] if len(l) == 1 else l[0] + mysum3(l[1:])
s3 = mysum3([1,2,3,4,5,6])
print('Sum is : ', s3)
def mysum4(l):
	print(l)
	first, *rest = l
	return first if not rest else first + mysum4(rest)
s4 = mysum4([1,2,3,4,5,6])
print('Sum is : ', s4)
print('-' * 80)
def mysum5(l):
	print('l is : ', l)
	if not l:
		return 0
	else:
		return notempty(l)
def notempty(l):
	return l[0] + mysum5(l[1:])
s5 = mysum5([1,2,3,4,5,6])
print('Sum is : ', s5)