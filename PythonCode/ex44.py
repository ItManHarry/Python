class Parent(object):
	def implicit(self):
		print "Parent's implicit() method"
	def override(self):
		print "Parent's override() method"
	def altered(self):
		print "Parent's altered()"
class Child(Parent):
	def override(self):
		print "Child's override method"
	def altered(self):
		print "Before the Parent's altered()"
		super(Child, self).altered()
		print "After the Parent's altered()"
p = Parent()
c = Child()
p.implicit()
c.implicit()
p.override()
c.override()
p.altered()
c.altered()