i = 0
numbers = []
while i < 6 :
	print "At the top i is : %d" % i
	numbers.append(i)
	i += 1
	print "Now the i is : %d" % i
	print "At the bottom i is : %d" % i
print "The numbers are : "
for n in numbers :
	print "Number is : %d" % n