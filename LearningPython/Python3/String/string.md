# Common string literals and operations

```
	Operation 					Interpretation
	S = '' 						Empty string
	S = "spam's" 				Double quotes, same as single
	S = 's\np\ta\x00m' 			Escape sequences
	S = """...multiline...""" 	Triple-quoted block strings
	S = r'\temp\spam' 			Raw strings (no escapes)
	B = b'sp\xc4m' 				Byte strings in 2.6, 2.7, and 3.X (Chapter 4, Chapter 37)
	U = u'sp\u00c4m' 			Unicode strings in 2.X and 3.3+ (Chapter 4, Chapter 37)
	S1 + S2						Concatenate
	S * 3						Repeat
	S[i]						Index
	S[i:j]						Slice
	len(S)						Length 
	"a %s parrot" % kind 		String formatting expression
	"a {0} parrot".format(kind) String formatting method in 2.6, 2.7, and 3.X
	S.find('pa')				Search
	S.rstrip()					Remove whitespace
	S.replace('pa', 'xx')		Replacement
	S.split(',')				Split on delimiter
	S.isdigit()					Content test
	S.lower()					Case conversion
	S.endswith('spam')			End test
	'spam'.join(strlist)		Delimiter join
	S.encode('latin-1')			Unicode encoding
	B.decode('utf8')			Unicode decoding
	for x in S: print(x)		Iteration
	'spam' in S					Membership
	[c * 2 for c in S]
	map(ord, S)
	re.match('sp(.*)am', line) 	Pattern matching: library module
```
# String backslash characters

```
	Escape 				Meaning
	\newline 			Ignored (continuation line)
	\\ 					Backslash (stores one \)
	\' 					Single quote (stores ')
	\" 					Double quote (stores ")
	\a 					Bell
	\b 					Backspace
	\f 					Formfeed
	\n 					Newline (linefeed)
	\r 					Carriage return
	\t 					Horizontal tab
	\v 					Vertical tab
	\xhh 				Character with hex value hh (exactly 2 digits)
	\ooo 				Character with octal value ooo (up to 3 digits)
	\0 					Null: binary 0 character (doesn’t end string)
	\N{ id } 			Unicode database ID
	\uhhhh 				Unicode character with 16-bit hex value
	\Uhhhhhhhh 			Unicode character with 32-bit hex valuea
	\other 				Not an escape (keeps both \ and other)
```
# String in Action

- String slicing

![String Slice]()