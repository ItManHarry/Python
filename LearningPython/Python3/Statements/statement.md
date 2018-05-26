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

## Python 3.X reserved words
False class finally is return
None continue for lambda try
True def from nonlocal while
and del global not with
as elif if or yield
assert else import pass
break except in raise

## Variable Name Rules

- Syntax: (underscore or letter) + (any number of letters, digits, or underscores)
Variable names must start with an underscore or letter, which can be followed by
any number of letters, digits, or underscores. _spam, spam, and Spam_1 are legal
names, but 1_Spam, spam$, and @#! are not.

- Case matters: SPAM is not the same as spam
Python always pays attention to case in programs, both in names you create and
in reserved words. For instance, the names X and x refer to two different variables.
For portability, case also matters in the names of imported module files, even on
platforms where the filesystems are case-insensitive. That way, your imports still
work after programs are copied to differing platforms.

- Reserved words are off-limits
Names you define cannot be the same as words that mean special things in the
Python language. For instance, if you try to use a variable name like class, Python
will raise a syntax error, but klass and Class work fine. Table 11-3 lists the words
that are currently reserved (and hence off-limits for names of your own) in Python.

## Naming conventions

- Names that begin with a single underscore (_X) are not imported by a from module
import * statement (described in Chapter 23).

- Names that have two leading and trailing underscores (__X__) are system-defined
names that have special meaning to the interpreter.

- Names that begin with two underscores and do not end with two more (__X) are
localized (“mangled”) to enclosing classes (see the discussion of pseudoprivate
attributes in Chapter 31).

- The name that is just a single underscore (_) retains the result of the last expression
when you are working interactively.

## Common Python expression statements

| Operation | Interpretation |
| --- | --- |
| spam(eggs, ham) | Function calls	 |
| spam.ham(eggs) | Method calls |
| spam | Printing variables in the interactive interpreter |
| print(a, b, c, sep='') | Printing operations in Python 3.X |
| yield x ** 2 | Yielding expression statements |

