class Animal(object):
	pass
class Dog(Animal):
	def __init__(self, name):
		self.name = name
	def info(self):
		print self.name
class Cat(Animal):
	def __init__(self, name):
		self.name = name
	def info(self):
		print self.name
class Person(object):
	def __init__(self, name):
		self.name = name
		self.pet = None
	def info(self):
		print "The person's name is : ", self.name
		print "My pet's name is :", self.pet.info()
class Employee(Person):
	def __init__(self, name, salary):
		super(Employee, self).__init__(name)
		self.salary = salary
	def info(self):
		super(Employee, self).info()
		print "The employee's salary is :", self.salary
class Fish(object):
	pass
class Salmon(Fish):
	pass
class Halibut(Fish):
	pass
print "-" * 80
rover = Dog("Rover")
rover.info()
print "-" * 80
satan = Cat("Satan")
satan.info()
print "-" * 80
mary = Person("Mary")
mary.pet = satan
mary.info()
print "-" * 80
frank = Employee("Frank", 120000)
frank.pet = rover
frank.info()
print "-" * 80
flipper = Fish()
crouse = Salmon()
harry = Halibut()
