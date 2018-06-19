# Function Basics

## Function-related statements and expressions

	Two ways to make functions (def and lambda), two ways to manage scope visibility (global and nonlocal), and two ways to send results back to callers (return and yield).

| Statement or expression | Examples |
| --- | --- |
| Call expressions | myfunc('spam', 'eggs', meat=ham, *rest) |
| def | def printer(messge):print('Hello ' + message) |
| return | def adder(a, b=1, *c):return a + b + c[0] |
| global | x = 'old' def changer():global x; x = 'new' |
| nonlocal (3.X) | def outer():x = 'old' def changer():nonlocal x; x = 'new' |
| yield | def squares(x):for i in range(x): yield i ** 2 |
| lambda | funcs = [lambda x: x**2, lambda x: x**3] |

## Coding Functions

- def is executable code.
	
	Python functions are written with a new statement, the
def. Unlike functions in compiled languages such as C, def is an executable statement—
your function does not exist until Python reaches and runs the def. In fact,
it’s legal (and even occasionally useful) to nest def statements inside if statements,
while loops, and even other defs. In typical operation, def statements are coded in
module files and are naturally run to generate functions when the module file they
reside in is first imported.

- def creates an object and assigns it to a name.
	
	When Python reaches and runs
a def statement, it generates a new function object and assigns it to the function’s
name. As with all assignments, the function name becomes a reference to the function
object. There’s nothing magic about the name of a function—as you’ll see,
the function object can be assigned to other names, stored in a list, and so on.
Function objects may also have arbitrary user-defined attributes attached to them
to record data.

- lambda creates an object but returns it as a result.

	Functions may also be created
with the lambda expression, a feature that allows us to in-line function definitions
in places where a def statement won’t work syntactically.

- return sends a result object back to the caller.

	When a function is called, the
caller stops until the function finishes its work and returns control to the caller.
Functions that compute a value send it back to the caller with a return statement;
the returned value becomes the result of the function call. A return without a value
simply returns to the caller (and sends back None, the default result).

- yield sends a result object back to the caller, but remembers where it left off.

	Functions known as generators may also use the yield statement to send back a value and suspend
	their state such that they may be resumed later, to produce a series of results over time. This is another advanced topic covered later in this part of the book.
	
- global declares module-level variables that are to be assigned.

	By default, all
names assigned in a function are local to that function and exist only while the
function runs. To assign a name in the enclosing module, functions need to list it
in a global statement. More generally, names are always looked up in scopes—
places where variables are stored—and assignments bind names to scopes.

- nonlocal declares enclosing function variables that are to be assigned.

	Similarly,
the nonlocal statement added in Python 3.X allows a function to assign a
name that exists in the scope of a syntactically enclosing def statement. This allows
enclosing functions to serve as a place to retain state—information remembered
between function calls—without using shared global names.

- Arguments are passed by assignment (object reference).

	In Python, arguments
are passed to functions by assignment (which, as we’ve learned, means by object
reference). As you’ll see, in Python’s model the caller and function share objects
by references, but there is no name aliasing. Changing an argument name within
a function does not also change the corresponding name in the caller, but changing
passed-in mutable objects in place can change objects shared by the caller, and
serve as a function result.

- Arguments are passed by position, unless you say otherwise.

	Values you pass
in a function call match argument names in a function’s definition from left to right
by default. For flexibility, function calls can also pass arguments by name with
name=value keyword syntax, and unpack arbitrarily many arguments to send with
*pargs and **kargs starred-argument notation. Function definitions use the same
two forms to specify argument defaults, and collect arbitrarily many arguments
received.

- Arguments, return values, and variables are not declared.

	As with everything
in Python, there are no type constraints on functions. In fact, nothing about a
function needs to be declared ahead of time: you can pass in arguments of any type,
return any kind of object, and so on. As one consequence, a single function can
often be applied to a variety of object types—any objects that sport a compatible
interface (methods and expressions) will do, regardless of their specific types.