class tester:
	def __init__(self, start):
		self.state = start
	def nested(self, label):
		print(label, self.state)
		self.state += 1
f = tester(0)
f.nested('Spam')
f.nested('Ham')
f.nested('Egges')
g = tester(40)
g.nested('Spam')
g.nested('Ham')
g.nested('Egges')
f.nested('Spam-again')
f.nested('Ham-again')
f.nested('Egges-again')