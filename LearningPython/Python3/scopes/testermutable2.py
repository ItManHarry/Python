def tester(start):
	def nested(label):
		print(label, state[0])
		state[0] += 1
	state = [start]
	return nested
f = tester(100)
f('first')
#1
print('Spam')
#2
print('Spam')
#3
print('NI','Spam')
#4
print('NI')
#5
print('NI','Spam')
#6
print('Spam')