# _*_ coding:utf-8 _*_
def print_two(*args):
	arg1, arg2 = args
	print "Arg1 is : %r, Arg2 is : %r" % (arg1, arg2)
def print_two_again(arg1, arg2):
	print "Arg1 is : %r, Arg2 is : %r" % (arg1, arg2)
def print_one(arg):
	print "Argument is : ", arg	
def print_none():
	print "Print none argument."
	
print "*" * 60 
print_two("Harry", 35)
print_two_again("Tom", 36)
print_one("Jack")
print_none()
print "*" * 60

def do_add(x, y):
	print "x is : %r, y is : %r" %(x, y)
	z = x + y
	print "Added result is : %r " % z
	return z

z = do_add(100, 300)	
print "z is : %r" % z