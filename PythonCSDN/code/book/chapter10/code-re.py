import re
print('=' * 180)
p = re.compile('www')
print(type(p))
m1 = re.match(p,'www.fkit.org')
print(type(m1))
print(m1.span())
print(m1.group())
print(re.match('fkit','www.fkit.org'))
print('-' * 80)
m2 = re.search('www','www.fkit.org')
print(type(m2))
print(m2.span())
print(m2.group())
print('-' * 80)
m3 = re.search('fkit','www.fkit.org')
print(m3.span())
print(m3.group())
print('-' * 80)
r = re.findall('fkit','Fkit is good, I like the fkit and the Fkit.org web',re.I)
print(type(r))
print(r)
r = re.finditer('fkit','Fkit is good, I like the fkit and the Fkit.org web',re.I)
print(type(r))
for e in r:
    print(e.span() ,'-->',e.group())
print('-' * 80)
my_date = '2020-04-24'    
print('Date string : ', my_date)
print(re.sub(r'-','/',my_date))
my_str = 'Java is a good language , and the Python too'
print('String : ', my_str)
print(re.sub(r'o', 'u', my_str))
my_str = 'a,b,c,d,e,f'
my_list = my_str.split(',')
print(my_list)
r = re.split(',', my_str)
print(type(r))
print(r)
print('-' * 80)
print(re.escape(r'www.crazyit.org is good, and I love it'))
print(re.escape(r'A-Zand0_9?'))
print('=' * 180)