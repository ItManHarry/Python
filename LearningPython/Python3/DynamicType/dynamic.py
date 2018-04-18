import copy
import sys
#Shared References
print('-' * 80)
a = 3
b = a
a = 'Spam'
print('a is : ', a)
print('b is : ', b)
print('-' * 80)
x = 3
y = x
x = x + 2
print('x is : ', x)
print('y is : ', y)
print('-' * 80)
l1 = [2,3,4]
l2 = l1
print('list 1 is : ', l1)
print('list 2 is : ', l2)
l1[0] = 8
print('now list 1 is : ', l1)
print('now list 2 is : ', l2)
print('-' * 80)
#copy the list
list1 = [2,3,4]
list2 = list1[:]
list3 = copy.copy(list1)
list4 = copy.deepcopy(list1)
list1[0] = 9
print('list 1 is : ', list1)
print('list 2 is : ', list2)
print('list 3 is : ', list3)
print('list 4 is : ', list4)
print('-' * 80)
#Shared References and Equality
l = [1,2,3]
m = l
print('l and m have the same values : ', l == m)
print('l and m are same objects : ', l is m)
m = [1,2,3]
print('l and m have the same values : ', l == m)
print('l and m are same objects : ', l is m)
x = 42
y = 42
print("x's value equals y's value :  ", x == y)
print("x and y are same objects : ", x is y)
print(sys.getrefcount(1))
print('-' * 80)