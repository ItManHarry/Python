#列表去重
#方式一
oldList = [1,2,3,4,5,2,3,5,6,8,9]
newList = []
for i in oldList:
    if i not in newList:
        newList.append(i)
print('Old list : ', oldList)
print('Result list : ', newList)
print('-' * 80)
#方式二 使用set()集合
st = set(oldList)
newList = list(st)
print('Old list : ', oldList)
print('Result list : ', newList)
#方式三 使用itertools模块下的groupby函数，该函数用于分组，相同的就分为一组
print('-' * 80)
#导入itertools模块，如果没有安装执行"pip install more-itertools"即可安装
import itertools
#首先必须对列表排序
oldList.sort()
#执行分组
it = itertools.groupby(oldList)
newList = []
for k, g in it:
    newList.append(k)
print('Old list : ', oldList)
print('Result list : ', newList)