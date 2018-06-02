#Iterations and Comprehensions
print('-' * 80)
for x in [1,2,3,4]:
	print(x ** 2)
for x in (1,2,3,4):
	print(x ** 3)
for x in 'spam':
	print(x * 2)
print('-' * 80)
#read file
for line in open('statement1.py'):
	print(line.upper())
print('-' * 80)