# _*_ coding:utf-8 _*_
print "Let's practice everything."
print "You \'need to know \'about escape with \\ that do \n newlines and \t tabs"
poem = """
	\tThe lovely world
	with logic so firmly planted
	cannot discern \n the needs of love
	nor comprehend passion from intuition
	and requires an explanation
	\n\t\t where there is none
"""
print "-" * 60
print poem
print "-" * 60
five = 10 - 2 + 3 - 6
print "This should be five %d" %five
def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates
start_point = 10000
beans, jars, crates = secret_formula(start_point)
print "Start point is : %d" % start_point
print "Beans : %d, jars : %d, crates : %d" %(beans, jars, crates)	
start_point = start_point / 10
print "We can also do this in this way , start_point is : %d" % start_point
print "Beans : %d, jars : %d, crates : %d" % secret_formula(start_point)