import pandas as pd
print('-' * 200)
df = pd.read_csv('./data/employees.csv',encoding='gbk')
print(df.info())
print('-' * 200)
print(df.head(10))
print('-' * 200)
print(df.tail(10))
print('-' * 200)
print(df.index)
print('-' * 200)
print(df.columns)
print('-' * 200)
print(df.values)
#for d in df.values:
    #print(d)
print('-' * 200)
print(df.dtypes)
print('-' * 200)
ids = df[['雇员职号','雇员姓名']]
print(ids.index)
print(ids.values)
print('-' * 200)
es1 = df[df['在职状态'] == 14891]
es2 = df[df['在职状态'] == 123356]
print('总人数 :\t', len(df))
print('在职人数 :\t', len(es1))
print('离职人数 :\t', len(es2))
#多条件组合筛选
es3 = df[(df['在职状态'] == 14891) & (df['代理商代码'] == '42')]
print('湖南直营在职人数:\t', len(es3), type(es3))
employees = es3.values
for employee in employees:
    print(employee)
print('-' * 200)    
print(employees[1])    
print('-' * 200)
print(es1.index)
print(es1.head(10))
print(es1.tail(10))
print('-' * 200)