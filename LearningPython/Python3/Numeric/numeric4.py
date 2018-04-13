from fractions import Fraction
from decimal import Decimal
import decimal
print('-' * 80)
x = Fraction(1, 3)
y = Fraction(4, 6)
print(x)
print(y)
print(x + y)
print(x - y)
print(x * y)
print('-' * 80)
print(Fraction('.25'))
print(Fraction('1.25'))
print(Fraction('0.25') + Fraction('1.25'))
print('-' * 80)
a = 1 / 3.0
b = 4 / 6.0
print(a)
print(b)
print(a + b)
print(a - b)
print(a * b)
print('-' * 80)
print(0.1+0.1+0.1-0.3)
print(Fraction(1,10)+Fraction(1,10)+Fraction(1,10)-Fraction(3,10))
print(Decimal('0.1')+Decimal('0.1')+Decimal('0.1')-Decimal('0.3'))
print('-' * 80)
print(1 / 3)
print(Fraction(1,3))
decimal.getcontext().prec = 2
print(Decimal(1) / Decimal(3))
print('-' * 80)