def times(x, y):
	return x * y
print('-' * 80)
print(times(2, 4))
print(times(3.14, 4))
print(times('Harry', 5))
print('-' * 80)
def intersect(seq1, seq2):
	res = []
	for x in seq1:
		if x in seq2:
			res.append(x)
	return res
seq1 = [1,2,3,4,5]
seq2 = [2,3,4,6,7]
print("Sequence 1 is : ", seq1)
print("Sequence 2 is : ", seq2)
print("Sequence 1 and 2's intersection is : ", intersect(seq1, seq2))
print(intersect('ABCDEFG','EFABXYZ'))
print('-' * 80)