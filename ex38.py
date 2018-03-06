# _*_ coding:utf-8 _*_
ten_things = "Apple Orange Crow Telephone Light Sugar"
print "Six things are : "
print ten_things
print "Wait there's not 10 things in that list ,let's fix that."
stuff = ten_things.split(" ")
more_stuff = ["Day","Night","Song","Frisbee","Corn","Banana","Girl","Boy"]
print "More stuff : ", more_stuff
while len(stuff) != 10 :
	next_one = more_stuff.pop()
	print "Add : ", next_one
	stuff.append(next_one)
	print "There's %d items now." % len(stuff)
print "Here we go : ", stuff
for s in stuff :
	print "Element is : %s" % s
print "Element of first index : ", stuff[1]
print "Try this : ", stuff[-1]
print ' '.join(stuff)
print "#".join(stuff[3:5])