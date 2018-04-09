print('-' * 80)
s = 'sp\xc4m'
print(s)
print(s[2])
print('Write into the unidata.txt file.')
file = open('unidata.txt', 'w', encoding='utf-8')
file.write(s)
file.close()
print('Read from the unidata.txt file')
text = open('unidata.txt', 'r', encoding='utf-8').read()
print(text)
print(len(text))
print('Read the file in binary mode')
raw = open('unidata.txt', 'rb').read()
print(raw)
print(len(raw))
print(text.encode('utf-8'))
print(raw.decode('utf-8'))
print(text.encode('latin-1'))
print(text.encode('utf-16'))
print(len(text.encode('latin-1')), len(text.encode('utf-16')))
print('-' * 80)