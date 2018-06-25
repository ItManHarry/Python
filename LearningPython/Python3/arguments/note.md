# Arguments

## Arguments passing

- Arguments are passed by automatically assigning objects to local variable
names.

	Function arguments—references to (possibly) shared objects sent by the
caller—are just another instance of Python assignment at work. Because references
are implemented as pointers, all arguments are, in effect, passed by pointer. Objects
passed as arguments are never automatically copied.

- Assigning to argument names inside a function does not affect the caller.

	Argument names in the function header become new, local names when the function
runs, in the scope of the function. There is no aliasing between function argument
names and variable names in the scope of the caller.

- Changing a mutable object argument in a function may impact the caller.

	On the other hand, as arguments are simply assigned to passed-in objects, functions
can change passed-in mutable objects in place, and the results may affect the
caller. Mutable arguments can be input and output for functions.

- Immutable arguments are effectively passed “by value.”

	Objects such as integers
and strings are passed by object reference instead of by copying, but because
you can’t change immutable objects in place anyhow, the effect is much like making
a copy.

- Mutable arguments are effectively passed “by pointer.”

	Objects such as lists
and dictionaries are also passed by object reference, which is similar to the way C
passes arrays as pointers—mutable objects can be changed in place in the function,
much like C arrays.

## Argument Matching Syntax

| Syntax | Location | Interpretation |
|--- | --- | --- |
| func(value) | Caller | Normal argument: matched by position |
| func(name=value) | Caller | Keyword argument: matched by name |
| func(*iterable) | Caller | Pass all objects in iterable as individual positional arguments |
| func(**dict) | Caller | Pass all key/value pairs in dict as individual keyword arguments |
| def func(name) | Function | Normal argument: matches any passed value by position or name |
| def func(name=value) | Function | Default argument value, if not passed in the call |
| def func(*name) | Function | Matches and collects remaining positional arguments in a tuple |
| def func(**name) | Function | Matches and collects remaining keyword arguments in a dictionary |
| def func(*other, name)| Function| Arguments that must be passed by keyword only in calls (3.X) |
| def func(*, name=value) | Function| Arguments that must be passed by keyword only in calls (3.X) |

