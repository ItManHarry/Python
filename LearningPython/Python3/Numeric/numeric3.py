from decimal import Decimal
import decimal
print('-' * 80)
print(0.1+0.1+0.1-0.3)
print(Decimal('0.1') + Decimal('0.10') + Decimal('0.10') - Decimal('0.30'))
print(Decimal(0.1) + Decimal(0.1) + Decimal(0.1) - Decimal(0.3))
print(Decimal(1) / Decimal(7))
decimal.getcontext().prec = 4
print(Decimal(0.1) + Decimal(0.1) + Decimal(0.1) - Decimal(0.3))
print(Decimal(1) / Decimal(7))
#monetary applications
print(1999 + 1.33)
decimal.getcontext().prec = 2
pay = decimal.Decimal(str(1999 + 1.33))
print(pay)
print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))
#set precision temporarily
with decimal.localcontext() as ctx:
	ctx.prec = 3
	print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))
print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))
print('-' * 80)