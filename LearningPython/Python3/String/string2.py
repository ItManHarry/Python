#String in action
print('-' * 80)
s = 'abc'
print(len(s))			#the length of the string
print('abc' + 'def')	#concatenate strings
print('Ni!' * 4)		#repeat string
print('-' * 80)
myjob = 'hacker'
for c in myjob :
	print(c, end = ' ')	# Step through items, print each (3.X form)
print('k' in myjob)		#find the character
print('z' in myjob)
print('spam' in 'abcspamdef')	# Substring search, no position returned
print('-' * 80)
s = 'spam'
print(s[0], s[-2])				# Indexing from front or end
print(s[1:3], s[1:], s[:-1])	# Slicing: extract a section
print('-' * 80)