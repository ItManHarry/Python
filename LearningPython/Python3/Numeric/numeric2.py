import math
#Division:classic,floor,and True
#the '/' operand and '//' operand
print('-' * 80)
print(10 / 4)
print(10 / 4.0)
print(10 // 4)
print(10 // 4.0)
x = 10
y = 4
z = x // y
print(z)
z = x / float(y)
print(z)
print('-' * 80)
print(math.floor(2.5))
print(math.floor(-2.5))
print(math.trunc(2.5))
print(math.trunc(-2.5))
print(5 / 2, 5 / -2)
print(5 // 2, 5 // -2)
print(5 / 2.0, 5 / -2.0)
print(5 // 2.0, 5 // -2.0)
print('-' * 80)
print(999999999999999999999999999999 + 1)
print(2 ** 200)
print('-' * 80)
#Hex , Octal, Binary:Literals and Conversions
print(0o1, 0o20,0o377)
print(0x01, 0x10, 0xFF)
print(0b1, 0b1111, 0b11111111)
print(0xFF, (15 * (16 ** 1)) + (15 * (16 ** 0)))
print(0x2F, (2 * (16 ** 1)) + (15 * (16 ** 0)))
print(0xF, 0b1111, (1 * (2 ** 3)) + (1 * (2 ** 2)) + (1 * (2 ** 1)) + (1 * (2 ** 0)))
print(2 * 4 ** 2)
print('{0:o},{1:x},{2:b}'.format(64,64,64))
print('%o, %x, %x, %X' % (64,64,255,255))
print('-' * 80)
x = 1
print(x << 2)
print(x | 2)
print(x & 1)
print('-' * 80)