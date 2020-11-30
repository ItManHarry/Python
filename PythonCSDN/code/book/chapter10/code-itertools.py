import itertools as it
#使用三个个序列进行排列组合
iter_array1 = it.product('AB', 'CD', 'EF')
for e in iter_array1:
    #ACE/ACF/ADE/ADF/BCE/BCF/BDE/BDF
    print('Element is : ', e, '\n')
    print(''.join(e), end=', ')
    print('\n')
print('-' * 80)    
arr1 = [1,2,3] 
arr2 = [4,5,6]
new_arr = it.product(arr1, arr2)   
print('New array is : ', new_arr)
for e in new_arr:
    print('Element is ：', e, '\n')
print('-' * 80)       
iter_array1 = it.product('ABC', repeat=3)   
for e in iter_array1:
    print('Element is : ', e)
print('-' * 80)       
iter_array2 = it.permutations('ABCD', 3)
for e in iter_array2:
    print('Eelement is : ', e)