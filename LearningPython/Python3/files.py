print('-' * 80)
#create a new file with 'w' mode
f = open('data.txt', 'w')
f.write('Hello\n')
f.write('World\n')
f.close()
#read a file, and 'r' is the default processing mode
f = open('data.txt')
t = f.read()
print('File content is : ')
print(t)
l = t.split()
print(l)
print('read the file using for iteration:')
for line in open('data.txt'):
	print(line)
print('-' * 80)