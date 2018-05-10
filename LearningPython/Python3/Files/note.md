# Files

| Operation | Interpretation|
| --- | --- |
| output = open(r'C:\spam', 'w') |  Create output file ('w' means write) |
| input = open('data', 'r') |  Create input file ('r' means read) |
| input = open('data')  | Same as prior line ('r' is the default) |
| aString = input.read() |  Read entire file into a single string |
| aString = input.read(N) |  Read up to next N characters (or bytes) into a string |
| aString = input.readline() |  Read next line (including \n newline) into a string |
| aList = input.readlines() |  Read entire file into list of line strings (with \n) |
| output.write(aString)  | Write a string of characters (or bytes) into file |
| output.writelines(aList) |  Write all line strings in a list into file |
| output.close() |  Manual close (done for you when file is collected) |
| output.flush()  | Flush output buffer to disk without closing |
| anyFile.seek(N) |  Change file position to offset N for next operation |
| for line in open('data'): use line  | File iterators read line by line |
| open('f.txt', encoding='latin-1')  | Python 3.X Unicode text files (str strings) |
| open('f.bin', 'rb')  | Python 3.X bytes files (bytes strings) |
| codecs.open('f.txt', encoding='utf8')  | Python 2.X Unicode text files (unicode strings) |
| open('f.bin', 'rb')  | Python 2.X bytes files (str strings) |