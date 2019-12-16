#普通除法
div = 5 / 3
print(div)
#整除
div = 5 // 3
print(div)
div = 6.5 // 2.3
print(div)
#求余的结果正负值始终和除数保持一致
mod = 23 % 7
print(mod)
mod = -23 % 7
print(mod)
mod = 23 %  -7
print(mod)
mod = -23 % -7
print(mod)
#乘方
print(3 ** 3)
#开方
print(27 ** (1/3))
import math
print(math.sin(3.14 / 4))
#扩展运算符
a = 24
a += 2
print(a)
a *= 3
print(a)
a /= 4
print(a)
a %= 3
print(a)
a **= 2
print(a)
#索引运算符
s = "www.baidu.com"
print(s[3])
print(s[3:7])
print(s[3:9:2])
x = 38
y = 24
print(" x > y ? ",x > y)
z = 38
print(" x >= z ? ", x >= z)
print(" x < y ? ",x < y)
print(" x <= z ? ", x <= z)
str1 = "123"
str2 = str(123)
#is判断引用对象是否一致
print(" str1 is str2 ? ", str1 is str2)
print(" str1 is not  str2 ? ", str1 is not str2)
#==判断值是否相等
print("str1 is str2 ? ", str1 == str2)
a = 30
b = 27
print(3 ** 3 < a and 5 ** 2 > b)
print(3 ** 3 < a or 5 ** 2 > b)
print(not 3 ** 3 < a)
print(not 5 ** 2 > b)
print(not(3 ** 3 < a or 5 ** 2 > b))
#if实现三目运算符
age = int(input('Your age : '))
print("比25大") if  age > 25 else (print('等于25') if age == 25 else print('比25小'))
s = print("比25大"), "成年人" if  age > 25 else print('小于或者等于25')
print(s)
#in
a = 'a'
b = 'java.com'
print("a in b ? " , a in b)