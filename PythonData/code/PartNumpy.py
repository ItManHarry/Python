dt = {'A':100,'B':200,'C':400}
for k, v in dt.items():
    print('Key : ', k, ', Value : ', v)
print('-' * 80)    
import numpy as np
v_array = [1,2,3,4,5]
#以下报错TypeError: can only concatenate list (not "int") to list
#v_array + 1   
#此时使用numpy的array即可
#对于ndarray结构来说，里面所有的元素必须是同一类型（否则会自动向下转换），同等个数的列表才能执行相关的操作
v_array = np.array([1,2,3,4,5])
print('Type is : ', type(v_array))
v_array2 = np.array([1,2,3,4,5,6.6])
print('Array 2 : ', v_array2)
v_array3 = np.array([1,2,3,4,5,6.6,'abc'])
print('Array 3 : ', v_array3)
#array中的元素都加1
v_array += 1
print(v_array)
v_array *= 2
print(v_array)
v_array += v_array
print(v_array)
v_array -=v_array
print(v_array)
#数组相加只能是同个数的数组进行相加
array1 = np.array([1,2,3,4,5])
array2 = np.array([2,3,4,5,6])
array3 = array1 + array2
print(' Array1 type is : ', type(array1))
print(' Array2 type is : ', type(array2))
print(' Array3 type is : ', type(array3))
print(array3)
print('-' * 80)   
array4 = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(' Array4 type is : ', type(array4))
print(array4)
print(array4.shape)
print('' * 80)
#dtype-元素数据类型
print('Element type is : ', array4.dtype)
#数组元素的长度，和类型有关，比如：int为4，字符串为：44
print('Array length is : ', array4.itemsize)
#shape属性获取数组/子数组的个数，返回一个元组
print('Array and subarray length is :  ', array4.shape)
#和shape方法一样
print('Array and subarray length is :  ', np.shape(array4))
#size-数组元素总个数，多维数组：数组个数*子数组个数
print('Array 1 is : ', array1)
print('Array 1 size is : ', array1.size)
#和size方法一样
print('Array 1 size is : ', np.size(array1))
print('Array 1 size is : ', array1.size, ', item size is : ', array1.itemsize)
print('Array 4 is : ', array4)
print('Array 4 size is : ', array4.size, ', item size is : ', array4.itemsize)
array6 = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]]])
print('Array 6 size is : ', array6.size, ', item size is : ', array6.itemsize, ', shape is : ' , array6.shape)
#数组维度
print('数组维数 : ', array6.ndim)
#使用新元素替换所有的元素 - 必须是同一类型
array6.fill(10)
print('Array 6 now is : ', array6)
print('' * 80)
#索引与切片和Python的一致，从0开始
array1 = np.array([1,2,3,4,5])
print('Array 1 is : ', array1)
print('Index 2 element : ', array1[2])
print('Index 1:3 elements : ', array1[1:3])
print('Index -2: elements : ', array1[-2:])
print('' * 80)
#矩阵
v_array = np.array([
    [1,2,3,4],
    [10,20,30,40],
    [100,200,300,400],
    [1000,2000,3000,4000]
])
print('矩阵数组 : ', v_array)
print('矩阵数据单个元素 : ', v_array[1,1])
print('矩阵数据多个元素 : ', v_array[2,1:3])
#第一个":"表示取所以样板数据，后面的对应的列
r_array = v_array[:, 1]
print('Type is : ', type(r_array))
print('矩阵数据某一列元素 : ', r_array)
print('-' * 80)
#数组拷贝 - copy
array1 = [1,2,3,4,5,6]
array2 = array1
print('Array 1 is : ', array1)
print('Array 2 is : ', array2)
print('Now I change array2 element : ')
array2[2] = 300
print('Now array 1 is : ', array1)
print('Now array 2 is : ', array2)
array1 = [1,2,3,4,5,6]
array2 = array1.copy()
print('Array 1 is : ', array1)
print('Array 2 is : ', array2)
print('Now I change array2 element (copy): ')
array2[2] = 300
array2.append(700)
print('Now array 1 is : ', array1)
print('Now array 2 is : ', array2)
for e in array2:
    print('Element : ', e)
print('-' * 80)