#程序流程 - if
age = int(input('Please input your age : '))
if age > 18:
    print('您已超过18岁')
    print('您已是成年人，要独立了！')
else:
    print('您还没有超过18岁')
    print('您还是未成年！')
score = int(input('请输入你的分数：'))
if score > 90:
    print('非常好，发奖金！')
elif score > 80:
    print('优秀，也有奖金！')
elif score > 70:
    print('还可以，奖金不多！')
elif score > 60:
    print('刚及格,没有奖金！')
else:
    print('你出局了！')
#深入if
s = ""
if s:
    print('字符串不为空')
else:
    print('字符串为空')
i = 0
if i:
    print('数值不为零')
else:
    print('数值为零')
#三目运算符
age = 25
print('成年人要自立') if age > 18 else print('未成年人！')
#pass
score = 100
if score > 90:
    pass
else:
    print('低于120')