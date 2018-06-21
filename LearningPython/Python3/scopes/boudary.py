def tester(start):
	def nested(label):
		global state
		state = 0
		print(label, state)
	return nested
f = tester(0)
f('ABC')
print('state:', state)