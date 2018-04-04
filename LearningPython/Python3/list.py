print("-" * 80)
l = [123, 'spam', 1.23]
for i in l :
	print('The element is : ', i)
print("-" * 80)
print('The list length is : ', len(l))
print("-" * 80)
i = 0
while i < len(l):
	print('Index is : ', i , ', and the value is : ', l[i])
	i += 1
print('-' * 80)
print('The first element is : ', l[0])
print('The first elements are : ', l[:-1])
l2 = l + [4,5,6]
l3 = l * 2
print(l)
print(l2)
print(l3)
print('-' * 80)
l.append('NI')
print(l)
print(l.pop(2))
print(l)
print('-' * 80)
l = ['bb','aa','cc']
l.sort()
print(l)
l.reverse()
print(l)
#l[99] = 100
#print(l[99])
print('-' * 80)
#Nesting 
n = [[1,2,3],[4,5,6],[7,8,9]]
print(n)
l = n[1]
print(l)
e = n[1][2]
print(e)
print('-' * 80)
#Comprehensions
m = [[1,2,3],[4,5,6],[7,8,9]]
col2 = [e[1] for e in m]
print(col2)
for i in range(0, len(col2)):
	print('Index is : ', i , ', element is : ', col2[i])
print(m)
col3 = [row[1] + 1 for row in m]
print(col3)
col4 = [row[1] for row in m if row[1] % 2 == 0]
print(col4)
doubles = [c * 2 for c in 'spam']
print(doubles)
print('-' * 80)
cs = list('I am Harry')
print(cs)
ns = list(range(4))
print(ns)
ns2 = list(range(-6, 7, 2))
print(ns2)
matrix = [[x ** 2, x ** 3] for x in range(4)]
print(matrix)
matrix = [[x, x / 2, x * 2] for x in range(-6, 7, 2) if x > 0]
print(matrix)
print('-' * 80)