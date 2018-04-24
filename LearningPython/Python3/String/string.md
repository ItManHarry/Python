# Common string literals and operations

| Operation | Interpretation |
| --- | --- |	 					
| S = '' | Empty string |
| S = "spam's" | Double quotes, same as single |
| S = 's\np\ta\x00m' | Escape sequences |
| S = """...multiline...""" | Triple-quoted block strings |
| S = r'\temp\spam' |  Raw strings (no escapes) |
| B = b'sp\xc4m' |  Byte strings in 2.6, 2.7, and 3.X (Chapter 4, Chapter 37) |
| U = u'sp\u00c4m' |  Unicode strings in 2.X and 3.3+ (Chapter 4, Chapter 37) |
| S1 + S2 | Concatenate |
| S * 3 | Repeat |
| S[i] | Index |
| S[i:j] | Slice |
| len(S) | Length  |
| "a %s parrot" % kind | String formatting expression |
| "a {0} parrot".format(kind) | String formatting method in 2.6, 2.7, and 3.X |
| S.find('pa') | Search |
| S.rstrip() | Remove whitespace |
| S.replace('pa', 'xx') | Replacement |
| S.split(',') | Split on delimiter |
| S.isdigit() | Content test |
| S.lower() | Case conversion |
| S.endswith('spam') | End test |
| 'spam'.join(strlist) | Delimiter join |
| S.encode('latin-1') | Unicode encoding |
| B.decode('utf8') | Unicode decoding |
| for x in S: print(x) | Iteration |
| 'spam' in S | Membership |
| [c * 2 for c in S] |  |
| map(ord, S) | 
| re.match('sp(.*)am', line) | Pattern matching: library module |
# String backslash characters 
| Escape | Meaning |
| --- | --- |	 				
| \newline | Ignored (continuation line) | 
| \\ | Backslash (stores one \) | 
| \' | Single quote (stores ') | 
| \" | Double quote (stores ") | 
| \a | Bell | 
| \b | Backspace | 
| \f | Formfeed | 
| \n | Newline (linefeed) | 
| \r | Carriage return | 
| \t | Horizontal tab | 
| \v | Vertical tab | 
| \xhh| Character with hex value hh (exactly 2 digits) | 
| \ooo | Character with octal value ooo (up to 3 digits) | 
| \0 | Null: binary 0 character (doesn’t end string) | 
| \N{ id } | Unicode database ID | 
| \uhhhh | Unicode character with 16-bit hex value | 
| \Uhhhhhhhh | Unicode character with 32-bit hex valuea | 
| \other | Not an escape (keeps both \ and other) | 

# String in Action

- String slicing

![String Slice](https://github.com/ItManHarry/Python/blob/master/LearningPython/Python3/String/stringSlice.jpg)

- Indexing (S[i]) fetches components at offsets:
	
	- The first item is at offset 0.
	
	- Negative indexes mean to count backward from the end or right.
	
	- S[0] fetches the first item.
	
	- S[−2] fetches the second item from the end (like S[len(S)−2]).
	
- Slicing (S[i:j]) extracts contiguous sections of sequences:

	- The upper bound is noninclusive.
	
	- Slice boundaries default to 0 and the sequence length, if omitted.
	
	- S[1:3] fetches items at offsets 1 up to but not including 3.
	
	- S[1:] fetches items at offset 1 through the end (the sequence length).
	
	- S[:3] fetches items at offset 0 up to but not including 3.
	
	- S[:−1] fetches items at offset 0 up to but not including the last item.
	
	- S[:] fetches items at offsets 0 through the end—making a top-level copy of S.
	
- Extended slicing (S[i:j:k]) accepts a step (or stride) k, which defaults to +1:
	
	- Allows for skipping items and reversing order—see the next section.
	
- String Conversion Tools

	- int("42"), float("1.5"), str(42), str(3.1515) 	# Convert from/to string
	
	- repr(42) 											# Convert to as-code string

- Character code conversions

	- ord function  # from character to int
	
	- chr function  # from int to character

# String Methods

- Attribute fetches

	An expression of the form object.attribute means “fetch the value of attribute
in object.”

- Call expressions

	An expression of the form function(arguments) means “invoke the code of func
tion, passing zero or more comma-separated argument objects to it, and return
function’s result value.”

| String Methods |
| --- |
| S.capitalize() | 
| S.ljust(width [, fill])| 
| S.casefold() | 
| S.lower()| 
| S.center(width [, fill]) | 
| S.lstrip([chars])| 
| S.count(sub [, start [, end]]) | 
| S.maketrans(x[, y[, z]])| 
| S.encode([encoding [,errors]]) | 
| S.partition(sep)| 
| S.endswith(suffix [, start [, end]]) | 
| S.replace(old, new [, count])| 
| S.expandtabs([tabsize]) | 
| S.rfind(sub [,start [,end]])| 
| S.find(sub [, start [, end]]) | 
| S.rindex(sub [, start [, end]])| 
| S.format(fmtstr, *args, **kwargs)|  
| S.rjust(width [, fill])| 
| S.index(sub [, start [, end]]) | 
| S.rpartition(sep)| 
| S.isalnum() | 
| S.rsplit([sep[, maxsplit]])| 
| S.isalpha() | 
| S.rstrip([chars])| 
| S.isdecimal() | 
| S.split([sep [,maxsplit]])| 
| S.isdigit() | 
| S.splitlines([keepends])| 
| S.isidentifier() | 
| S.startswith(prefix [, start [, end]])| 
| S.islower() | 
| S.strip([chars])| 
| S.isnumeric() | 
| S.swapcase()| 
| S.isprintable() | 
| S.title()| 
| S.isspace() | 
| S.translate(map)| 
| S.istitle() | 
| S.upper()| 
| S.isupper()|  
| S.zfill(width)| 
| S.join(iterable)| 

# String Formatting Expressions

- String formatting expressions: '...%s...' % (values)
	
	The original technique available since Python’s inception, this form is based upon
the C language’s “printf” model, and sees widespread use in much existing code.

- String formatting method calls: '...{}...'.format(values)

	A newer technique added in Python 2.6 and 3.0, this form is derived in part from
a same-named tool in C#/.NET, and overlaps with string formatting expression
functionality.

| Code | Meaning |
| --- | --- |	 					
| s | String (or any object’s str(X) string) |
| r | Same as s, but uses repr, not str |
| c | Character (int or str) |
| d | Decimal (base-10 integer) |
| i | Integer |
| u | Same as d (obsolete: no longer unsigned) |
| o | Octal integer (base 8) |
| x | Hex integer (base 16) |
| X | Same as x, but with uppercase letters |
| e | Floating point with exponent, lowercase |
| E | Same as e, but uses uppercase letters |
| f | Floating-point decimal |
| F | Same as f, but uses uppercase letters |
| g | Floating-point e or f |
| G | Floating-point E or F |
| % | Literal % (coded as %%) |