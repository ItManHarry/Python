#定义矩阵转置的函数
#方式一：循环实现
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
def printMatrix(m):
    #由于m是二维列表
    for array in m:
        for e in array:
            print(e, end=' ')
        print('')
printMatrix(matrix)
print('-' * 50)
def transformMatrix1(m):
    #列变行
    nm = [[] for i in m[0]]
    for array in m:        
        for i in range(len(array)):
            #nm[i]代表新矩阵的第i行
            #array[i]代表原矩阵的第i列
            nm[i].append(array[i])
    return nm
printMatrix(transformMatrix1(matrix))
#使用zip()函数实现
print('-' * 50)
def transformMatrix2(m):
    return list(zip(*m))
printMatrix(transformMatrix2(matrix)) 
#使用numpy模块实现
print('-' * 50)
def transformMatrix3(m):
    import numpy
    return numpy.transpose(m).tolist()
printMatrix(transformMatrix3(matrix))  