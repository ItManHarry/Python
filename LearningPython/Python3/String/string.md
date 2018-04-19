Operation 					Interpretation
---
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
---