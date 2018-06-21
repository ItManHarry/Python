def tester(start):
	state = start
	def nested(label):
		nonlocal state
		state += 1
		print(label, state)
	return nested
f = tester(0)
f('Spam')
f('Eggs')
f('Ham')
g = tester(40)
g('Spam')
g('Eggs')
f('Bacon')