#String in action
import sys
#basic string operation
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
#String slicing
print('-' * 80)
s = 'spam'
print(s[0], s[-2])				# Indexing from front or end
print(s[1:3], s[1:], s[:-1])	# Slicing: extract a section
s = 'abcdefghijklmnop'
print(s[1:10:2])				# Skipping items
print(s[::2])
print(s[::-1])
print(s[5:1:-1])
print('spam'[1:3])				# Slicing syntax
print('spam'[slice(1,3)])
print('spam'[::-1])				# Slice objects with index syntax + object
print('spam'[slice(None, None, -1)])
print('-' * 80)
print('System arguments : ', sys.argv[0])
print('System arguments : ', sys.argv[1])
print('System arguments : ', sys.argv[2])
print('System arguments : ', sys.argv[3])
#String Conversion Tools
print('-' * 80)
# Convert from/to string
print("string to number : ", int("42"))
print('plus a number and a string by converting string to number : ', 42 + int('3'))
print('number to string : ', str(42))
print('concatenate a string and a number by converting number to string : ', '40' + str(23))
# Convert to as-code string
print(repr(42))
print(str('spam'), repr('spam'))
#string and float converting
print('float to string : ', str(3.1415))
print('string to float : ', float('1.5'))
text = '1.234E-10'
print(float(text))
print('-' * 80)
print('from character to int : ', ord('s'))
print('from int to character : ', chr(115))
s = '5'
s = chr(ord(s) + 1)
print('now the s is : ',s)
s = chr(ord(s) + 1)
print('now the s is : ',s)
print('2 square is : ', 2 ** 0)
b = '1101'
i = 0
while b != '':
	i = i * 2 + (ord(b[0]) - ord('0'))
	b = b[1:]
print('finally i is : ', i)
print(int('1101', 2))	# Convert binary to integer: built-in
print(bin(13))			# Convert integer to binary: built-in
print('-' * 80)
s = 'spam'
s = s + 'SPAM!'
print(s)
s = s[:4] + 'Burger' + s[-1]
print(s)
s = 'splot'
s = s.replace('pl','pamal')
print(s)
print('That is %d %s bird!' %(1,'dead'))
print('That is {0} {1} bird!'.format(1,'dead'))
print('-' * 80)
s = 'spam'
r = s.find('pas')
print("'pas' is in the s ? ", r)
#String methods
print('-' * 80)
s = 'spammy'
s = s[:3] + 'xx' + s[5:]	# Slice sections from S
print(s)
s = s.replace('xx', 'zz')
print('after replace the s now is : ', s)
print('aa$bb$cc$dd'.replace('$','SPAM'))
s = 'xxxSPAMxxxxSPAMxxxx'
index = s.find('SPAM')		# Search for position
print('index is : ', index)
s = s[:index] + 'EGGS' + s[(index+4):]
print(s)
s = 'xxxSPAMxxxxSPAMxxxx'
print(s.replace('SPAM','EGGS'))		# Replace all
print(s.replace('SPAM','EGGS',1))	# Replace one
print('-' * 80)