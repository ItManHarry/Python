the_count = [1,2,3,4,5]
fruits = ['Apple','Banana','Orange','Pears','Apricots']
change = [1,'Apple',2,'Apricots',3,'Banana']
print "-" * 60
for n in the_count:
	print "Number : %d" % n
print "-" * 60
for s in fruits:
	print "Fruit : %s" % s
print "-" * 60
for r in change:
	print "Element : %r" % r
print "-" * 60
elements = []
for i in range(0, 6):
	elements.append(i)
for i in elements:
	print "i is : %d" %i
print "-" * 60