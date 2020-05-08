from heapq import *
print('-' * 80)
lt = list(range(10))
lt.append(0.5)
#list data
print(type(lt))
print(lt)
print('-' * 80)
#将list转换为堆
heapify(lt)
print(type(lt))
print(lt)
print('-' * 80)
heappush(lt, 7.2)
print(lt)
print(heappop(lt))
print(heappop(lt))
print('Now the list is : ', lt)
print('-' * 80)
#heapreplace:弹出最小元素，压入指定元素
print(heapreplace(lt, 8.1))
print('After replace : ', lt)
print('-' * 80)
#输出最大的三个元素
print('Three largest elements : ', nlargest(3, lt))
#输出最小的三个元素
print('Three largest elements : ', nsmallest(3, lt))
print('-' * 80)