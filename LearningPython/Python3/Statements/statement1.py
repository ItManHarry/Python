print('-' * 80)
while True:
	reply = input('Please input the text : ')
	if reply == 'stop':
		break
	elif not reply.isdigit():
		print(reply.upper())
	else:
		print(int(reply) ** 2)
print('Bye!!!')
print('-' * 80)
while True:
	reply = input('Give me a number(or input Q to quit) : ')
	if reply.upper() == 'Q':
		print('Game over.')
		break
	else:
		try:
			num = int(reply)
			print(num ** 2)
		except:
			print('It is not a number, input again:')
print('Bye')			
print('-' * 80)
while True:
	reply = input('Give me a number(or input Q to quit) : ')
	if reply.upper() == 'Q':
		print('Game over.')
		break
	elif not reply.isdigit():
		print('It is not a number, input again:')
	else:
		num = int(reply)
		if num < 20:
			print('low number')
		else:
			print('high number')
print('Bye')
print('-' * 80)