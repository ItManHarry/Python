print('-' * 80)
squares = [x ** 2 for x in [1,2,3,4,5]]
print(squares)
for i in range(0, len(squares)):
	print('The index is : ', i , ' and the value is : ', squares[i])
squares = []
for i in [1,2,3,4,5] :
	squares.append(i ** 2)
print(squares)
for i in squares:
	print("Value is : ", i)
print('-' * 80)