import re
match = re.match('Hello[ \t]*(.*)world','Hello Python world')
print(match.group(1))
match = re.match('[/:](.*)[/:](.*)[/:](.*)','/usr/home:lumberjack')
print(match.groups())
print(re.split('[/:]','/usr/home/lumberjack'))