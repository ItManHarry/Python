# 科学计算库 - Numpy

## numpy简介：

	NumPy（Numerical Python）是Python的一种开源的数值计算扩展。这种工具可用来存储和处理大型矩阵，比Python自身的嵌套列表（nested list structure)结构
要高效的多（该结构也可以用来表示矩阵（matrix）），支持大量的维度数组与矩阵运算，此外也针对数组运算提供大量的数学函数库
	
	出处：https://baike.baidu.com/item/numpy/5678437?fr=aladdin

## 安装numpy	

```
	pip install numpy
```

## numpy数据结构之ndarray

```python
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
	#数据过滤器的几种方式
	array1 = np.arange(0,100,10)
	#方式一
	mask = np.array([0,0,0,0,0,0,1,1,1,1], dtype=bool)
	print(array1)
	print(mask)
	#过滤结果
	print(array1[mask])
	#方式二
	random_array = np.random.rand(10)
	print(random_array)
	mask = random_array > 0.5
	print(mask)
	print(random_array[mask])
	array1 = np.array([10,20,30,40,50,60])
	print(array1[np.where(array1 > 30)])
	print('-' * 80)
	#构建指定类型的数组
	array1 = np.array([1,2,3,4,5],dtype = np.float32)
	print(array1)
	array1 = np.array([1,2,3,4,5.6,6,'Jack'],dtype=np.object)
	print(array1)
	#类型转换
	array1 = np.array([1,2,3,4,5],dtype=np.int32)
	print(array1)
	array2 = array1.astype(np.float32)
	print(array2)
	print('-' * 80)
	#数据计算
	data_array = np.array([[1,2,3],[4,5,6]])
	print('Data : ', data_array)
	#求和 - 所有元素的和
	print('All elements sum : ',np.sum(data_array))
	print('All elements sum : ',data_array.sum())
	#求和 - 列级相加
	#调用方式一
	print('Columns sum : ', np.sum(data_array,axis=0))
	#调用方式二
	print('Columns sum : ', data_array.sum(axis=0))
	#求和 - 子数组求和
	print('Rows sum : ', np.sum(data_array,axis=1))
	print('Rows sum : ', data_array.sum(axis=1))
	#求积
	print(data_array.prod())
	print(data_array.prod(axis=0))
	print(data_array.prod(axis=1))
	#最小元素
	print(data_array.min())
	print(data_array.min(axis=0))
	print(data_array.min(axis=1))
	#最大元素
	print(data_array.max())
	print(data_array.max(axis=0))
	print(data_array.max(axis=1))
	#最小索引
	print(data_array.argmin())
	print(data_array.argmin(axis=0))
	print(data_array.argmin(axis=1))
	#最大索引
	print(data_array.argmax())
	print(data_array.argmax(axis=0))
	print(data_array.argmax(axis=1))
	#平均数
	print(data_array.mean())
	print(data_array.mean(axis=0))
	print(data_array.mean(axis=1))
	#标准差
	print(data_array.std())
	print(data_array.std(axis=0))
	print(data_array.std(axis=1))
	#方差
	print(data_array.var())
	print(data_array.var(axis=0))
	print(data_array.var(axis=1))
	#截段
	print(data_array.clip(2,4))
	#四舍五入
	data_array = np.array([1.25,3.42,5.84,7.47,9.72,10.54])
	print('Data : ', data_array)
	print('After round : ', data_array.round())
	for d in data_array.round():
		print('Element : ', d)
	#指定精度
	print('Data : ', data_array)
	print('After round : ', data_array.round(decimals=1))
	for d in data_array.round(decimals=1):
		print('Element : ', d)
	print('-' * 80)
```

