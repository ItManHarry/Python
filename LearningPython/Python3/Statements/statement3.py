# statement of if
print('-' * 80)
if 1:
	print('1 is the same with the True')
if not 1:
	print('it is 1')
else:
	print('it is not 1	')
x = 'killer rabbit'
if x == 'roger':
	print('shave and a haircut')
elif x == 'bugs':
	print('What is up doc?')
else:
	print('Run away, run away...')
choice = 'ham'
print({'spam':1.25,
	   'ham':1.99,
	   'eggs':0.99,
	   'bacon':1.10}[choice])
if choice == 'spam':
	print(1.25)
elif choice == 'ham':
	print(1.99)
elif choice == 'eggs':
	print(0.99)
elif choice == 'bacon':
	print(1.10)
else:
	print('bad choice')
print('-' * 80)
choices = {'spam':1.25,
	   'ham':1.99,
	   'eggs':0.99,
	   'bacon':1.10}
if(choice in choices):
	print(choices[choice])
else:
	print('bad choice')
print('-' * 80)
x = 1
if x:
	y = 2
	if y:
		print('block2')
	print('block1')
print('block0')
x = 'SPAM'
if 'rubbery' in 'shrubbery':
	print(x * 8)
	x += 'NI'
	if x.endswith('NI'):
		x *= 2
		print(x)
print('-' * 80)
if 2 and 3:
	print('2 and 3 are all True')
if {} and []:
	print('dictionary and list are all not empty')
else:
	print('dictionary or list is empty')
x = 2
y = 5 if x > 3 else 6
print('y is : ', y)
z = 5 if x > 3 else 6 if y > 9 else 7
print('z is : ', z)
print('-' * 80)