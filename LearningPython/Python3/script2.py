import math
import random
n = 123 + 222
print("The number is : ", n)
n = 1.5 * 4
print("Now the number is : ", n)
n = 2 ** 100
print("Finally the number is : ", n)
print("The big number length is : ", len(str(2 ** 10000)))
print(3.1415 * 2)
print(math.pi)
print(math.sqrt(84))
print(random.random())
print(random.choice([1,2,3,4,5,6,7,8]))
s = "Spam"
print("The string length is : ", len(s))
for c in s:
	print("Character is : ", c)
print("The first character is : ", s[0])
print("The second character is : ", s[1])
print("The third character is : ", s[2])
print("The forth character is : ", s[3])
print("*" * 70)
print("The first character is : ", s[-4])
print("The second character is : ", s[-3])
print("The third character is : ", s[-2])
print("The forth character is : ", s[-1])
print("*" * 70)
print(s[1:])
print(s[1:3])
print(s[:3])
print(s[:-1])
print(s + "xyz")
print(s*8)
s = 'x' + s[1:]
print("Now the String is : ", s)
print("*"*70)
s = "shrubby"
l = list(s)
print(len(l))
for e in l :
	print("The element is : ", e)
l[1] = 'c'
print(''.join(l))
print("*"*70)
b = bytearray(b'spam')
b.extend(b'eggs')
print(b.decode())
s = "Spam"
print(s.find("pa"))
print(s.replace("pa","xy"))
print(s)
print("*"*70)
s = "aaa,bbb,ccc,dd"
list = s.split(",")
print("Splited list length is : ", len(list))
for e in list:
	print("Element is : ", e.upper())   
print("*"*70)
s = "Spam"
print("s is alpha : ", s.isalpha())
s = "125"
print("s is number : ", s.isdigit())
s = "aaa,bbb,ccc,dd\n"
print(s.rstrip())
print("*" * 70)
for e in s.rstrip().split(","):
	print("Element is : ", e)
print("Lower case is : %s, upper case is : %s!" %('Spam','SPAM'))
print("Lower case is : {0}, upper case is : {1}!".format("spam","SPAM"))
print("Lower case is : {}, upper case is : {}!".format("spam","SPAM"))
print("{:,.2f}".format(296999.2567))
print("%.2f | %+05d" %(3.14159, -42))
s = "A\nB\tC"
print(s)
print("The length of the s is : ", len(s))
print(ord("\n"))
s = "a\0B\0C"
print("Now the s is : ", s)
s = """
	aaaaaa,
	bbbbbb,
	cccccc,
	dddddd,
	'eeeee',
	'fffff'
	c:\\uses\\20112004\\desktop,
	d:/java/projects
"""
print(s)
print("*" * 70)
#Unicode Strings
s = 'sp\xc4m'
print(s)
s = 'a\x01c'
print(s)
s = b'a\x01c'
print(s)
s = "sp\xc4\u00c4\U000000c4m"
print(s)
print('\u00A3', '\u00A3'.encode('latin1'), b'\xA3'.decode('latin1'))
