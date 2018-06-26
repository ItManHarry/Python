print('-' * 80)
def echo(*args, **kwargs):
	print(args, kwargs)
echo(1,2,a=3,b=4)
print('-' * 80)
def konly(a,*b,c):
	print(a,b,c)
konly(1,2,c=3)
konly(a=1,c=3)
konly(1,2,3,c=4)
print('-' * 80)
def kwonly(a,*,b,c):
	print(a,b,c)
kwonly(1,c=3,b=2)
kwonly(c=3,b=2,a=1)
#kwonly(1)
print('-' * 80)
def kwonly2(a,*,b='spam',c='eggs'):
	print(a,b,c)
kwonly2(1)
kwonly2(1,c=3)
kwonly2(a=1)
kwonly2(c=3,b=2,a=1)
print('-' * 80)
def min1(*args):
	res = args[0]
	for arg in args[1:]:
		if arg < res:
			res =arg
	return res
def min2(first, *rest):
	for arg in rest:
		if arg < first:
			first = arg
	return first
def min3(*args):
	tmp = list(args)
	tmp.sort()
	return tmp[0]
print(min1(3,4,1,2))
print(min2("cc","bb","aa"))
print(min3([2,2],[1,1],[3,3]))
print('-' * 80)
def minmax(test, *args):
	res = args[0]
	for arg in args[1:]:
		if test(arg, res):
			res = arg
	return res
def lt(x, y):
	return x < y
def gt(x, y):
	return x > y
print(minmax(lt, 4,2,1,5,6,3))
print(minmax(gt, 4,2,1,5,6,3))
print('-' * 80)