#第一章实操 ： 简单计算器和进制转换
#简单计算器
x = float(input("请输入第一个数："))
y = float(input("请输入第二个数："))
print("x + y : ", x + y)
print("x - y  : ", x - y)
print("x * y  : ", x * y)
#进制转换
x = int(input("请输入一个整数:"))
#十六进制
print("Hex : ", hex(x))
#八进制
print("Oct : ", oct(x))
#二进制
print("Bin : ", bin(x))