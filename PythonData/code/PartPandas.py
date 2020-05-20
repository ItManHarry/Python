import pandas as pd
print('-' * 200)
#读取数据到dataframe（df）
df = pd.read_csv('./data/titanic.csv')
#读取前几条数据,默认是5条
print(df.head())
print('-' * 200)
print(df.head(10))
print('-' * 200)
#读取后几条数据,默认是5条
print(df.tail())
print('-' * 200)
print(df.tail(10))
print('-' * 200)
#返回当前dataframe信息
print('Data frame info : ')
print(df.info())
print('-' * 200)
#返回dataframe索引信息
print('Data frame index : ')
print(df.index)
print('-' * 200)
#dataframe列
print('Data frame columns : ')
print(df.columns)
print('-' * 200)
#daaframe列数据类型
print('Data frame data type : ')
print(df.dtypes)
print('-' * 200)
#daaframe数据-数据类型为array
print('Data frame data : type is : ', type(df.values), ', values are : ')
print(df.values)
print('-' * 200)
#自定义dataframe，字典作为参数进行创建
data = {
    'name':['Harry','Jack','Tom'],
    'age':[32,24,38]}
cdf = pd.DataFrame(data) 
print(cdf.info())
print(cdf.head())
print('-' * 200)
#读取某一列数据
ages = df['age']
print('Column age : ', type(ages))
print('-' * 200)
print('ages all : ')
print(ages)
print('-' * 200)
print('ages index : ')
print(ages.index)
print('-' * 200)
print('ages values : ')
print(ages.values)
print('-' * 200)
#指定索引
df = df.set_index('name')
print(df.head())
#根据索引获取列的值
ages = df['age']
print("Allen, Miss Elisabeth Walton' s age is : ", ages['Allen, Miss Elisabeth Walton'])
#某一列数据统一操作(加减乘除......),以加为例
print('Before add 10 : ')
print(ages[:5])
ages = ages + 10
print('After add 10 : ')
print(ages[:5])
#取最大
print('Max age : ', ages.max())
#取最小
print('Min age : ', ages.min())
#取平均
print('Mean age : ', ages.mean())
print('-' * 200)
#获取数据基本统计特性（较为实用）,只针对数字类型的数据进行统计，非数字不可用
print(df.describe())
print('-' * 200)
#取某几列
print('Get some columns : ')
print(df[['pclass','age','ticket']][:10])
print('-' * 200)
#Pandas索引 - iloc:位置定位
print(df.iloc[0])
print('-' * 200)
print(df.iloc[:10])
print('-' * 200)
print(df.iloc[0:3, 4:9])
print('-' * 200)
#Pandas索引 - loc:索引定位
print(df.loc['Allison, Master Hudson Trevor','age'])
print(df.loc['Andrews, Mr Thomas, jr','age'])
print('-' * 200)
#bool类型的索引 年龄大于20的索引
print(df['age'] > 20)
print('-' * 200)
#筛选出年龄大于20的人
print(df[df['age'] > 20][:10])
print('-' * 200)
#筛选出所有的男女乘客
fs = df[df['sex'] == 'female']
ms = df[df['sex'] == 'male']
print('Female passengers : ', len(fs), ', use sum method : ', (df['sex'] == 'female').sum())
print('Male passengers : ', len(ms), ' use sum method : ', (df['sex'] == 'male').sum())
print('-' * 200)
#男乘客平均年龄
ma = df.loc[df['sex'] == 'male', 'age'].mean()
print('Male passengers mean age ： ', ma)
#40岁以上乘客总人数
ps = df[df['age'] > 40]
print('Age more than 40 years old passengers size : ', len(ps))
sa = (df['age'] > 40).sum()
print('Total passenger  : ', sa)
print('-' * 200)