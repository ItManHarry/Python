def tester(start):
	def nested(label):
		print(label, nested.state)
		nested.state += 1
	nested.state = start
	return nested
f = tester(0)
f('Harry')
f('Jack')
f('Jone')