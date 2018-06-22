def tester(start):
	def nested(label):
		print('state is : ', state)
		print(label, state[0])
		state[0] += 1
	state = [start]
	return nested
f = tester(100)
f('First')
f('Second')
f('Third')