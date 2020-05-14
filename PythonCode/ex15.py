# _*_ coding:utf-8 _*_
from sys import argv
script, filename = argv
txt = open(filename)

print "Here is you file %r" % filename, ", and the file content is : "
print txt.read()
txt.close()

print "Type the filename again : "

file_again = raw_input("> ")

txt_again = open(file_again)
print txt_again.readline()
print "-" * 50
print txt_again.read()
txt_again.close()