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
#分组 - groupby
#单列分组
print('-' * 200)
gbr = df.groupby('代理商代码')
print('Group type is : ', type(gbr))
#查看分组 - groups属性返回数据字典
print(type(gbr.groups))
for code in gbr.groups.keys():
    print('Dealer code is : ', code)
print('-' * 200)    
#   多列分组
gbr = df.groupby(['代理商代码','部门所属'])
#print(gbr.head())
for code in gbr.groups.keys():
    print('Group key is : ', code)
print('-' * 200)   
print(gbr.groups)
print('-' * 200)   
#遍历分组
for name, group in gbr:
    print('Key : ', name)
    #print('Group : ', group)
    print('Group : ', len(group))
print('-' * 200)      
#获取某个分组get_group('key')
gbr = df.groupby('代理商代码')
group = gbr.get_group('42')
print('42 size is : ', group.count())
print('Data : ', group)
print('-' * 200)  
import numpy as np
#分组并求每组的平均
df = pd.read_csv('./data/titanic.csv')
gbr = df.groupby('pclass').aggregate(np.mean)
print('Group by pclass all number column mean : ')
print(gbr)
print('-' * 200)  
#求分组后某一列的平均值
gbr = df.groupby('pclass')['age'].mean()
print('Group by pclass  age mean is : ')
print(gbr)
print('-' * 200)  
#求分组后某一列的总和
sum = df.groupby('pclass')['age'].sum()
print('Group by pclass  age sum is : ')
print(sum)
print('-' * 200)  
#相关系数
corr = df.corr()
print('Corr is : ', corr)
print('-' * 200)  
#列个数据统计
ac = df['age'].value_counts()
print(type(ac))
print('Age count is ； ', ac)
print('-' * 200) 
#指定升序
ac = df['age'].value_counts(ascending=True)
print('Age count is ； ', ac)
print('-' * 200)  
#指定区间
ac = df['age'].value_counts(ascending=True, bins=5)
print('Age count is ； ', ac)
print('-' * 200)  
#Series结构的增删改查 Series对应的是某一列的值
#查 - 1.和list一样,使用范围索引，2.使用dataframe的索引
sd = df['age']
print('Data type is : ', type(sd))
#使用范围索引
print(sd[0])
print(sd[3:10])
#数据修改 ， 修改之前备份一下
data_backup = sd.copy()
print('Backup data : ', data_backup)
#执行修改
sd.replace(to_replace=1,value=0.9167,inplace=True)
print('After replace : ', sd)
#增加
print('Type is : ', type(sd[0]))
d = [100,101]
i = ['k','h']
s = pd.Series(data=d,index=i)
sd.append(s)
print('After added : ', sd)
#删除
del  sd[0]
sd.drop([1,2], inplace=True)
print('After deleted : ',sd)
print('-' * 200) 