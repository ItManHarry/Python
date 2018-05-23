# Python’s Statements

## Python statements

| Statement | Role | Example |
| --- | --- | --- |
| Assignment | Creating references | a, b = 'good', 'bad' |	
| Calls and other expressions | Running functions | log.write("spam, ham") |	
| print calls | Printing objects | print('The Killer', joke) |	
| if/elif/else | Selecting actions | if "python" in text: print(text) |	
| for/else | Iteration | for x in mylist:print(x) |	
| while/else | General loops | while X > Y:print('hello') |	
| pass | Empty placeholder | while True:pass |	
| break | Loop exit | while True:if exittest(): break |	
| continue | Loop continue | while True:if skiptest(): continue |	
| def | Functions and methods |def f(a, b, c=1, *d):print(a+b+c+d[0])|	
| return | Functions results | def f(a, b, c=1, *d):return a+b+c+d[0] |	
| yield | Generator functions | def gen(n):for i in n: yield i*2 |	
| global | Namespaces | x = 'old' def function(): global x, y; x = 'new' |	
| nonlocal | Namespaces (3.X) | def outer():x = 'old' def function():nonlocal x; x = 'new'|	
| import | Module access | import sys |	
| from | Attribute access | from sys import stdin |	
| class | Building objects | class Subclass(Superclass):staticData = [] def method(self): pass |	
| try/except/ finally | Catching exceptions | try:action()except:print('action error') |	
| raise | Triggering exceptions | raise EndSearch(location) |	
| assert | Debugging checks | assert X > Y, 'X too small' |	
| with/as | Context managers (3.X, 2.6+) | with open('data') as myfile:process(myfile) |	
| del | Deleting references | del data[k] del data[i:j] del obj.attr del variable |

## Assignment statement forms

| Operation | Interpretation |
| --- | --- |
| spam = 'Spam' | Basic form |
| spam, ham = 'yum', 'YUM' | Tuple assignment (positional) |
| [spam, ham] = ['yum', 'YUM'] | List assignment (positional) |
| a, b, c, d = 'spam' | Sequence assignment, generalized |
| a, *b = 'spam' | Extended sequence unpacking (Python 3.X) |
| spam = ham = 'lunch' | Multiple-target assignment |
| spams += 42 | Augmented assignment (equivalent to spams = spams + 42) |