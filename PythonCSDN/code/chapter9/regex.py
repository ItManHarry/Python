import re
line = 'Cats are smaller than dogs'
mo = re.match(r'(.*)are(.*?)', line)
print(type(mo))
if mo:
    group = mo.group()
    print(type(group))
    print(group)