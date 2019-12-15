#列表去重
#方式一
oldList = [1,2,3,4,5,2,3,5,6,8,9]
newList = []
for i in oldList:
    if i not in newList:
        newList.append(i)
print('Result list : ', newList)