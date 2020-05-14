# _*_ coding:utf-8 _*_
from sys import argv
script , filename = argv

print "We are going to erase %r : " % filename
print "If you don't want that, hit CTRL-C(^C)."
print "If you do want that, hit ENTER."

raw_input("?")

print "Opening the file ..."
target = open(filename, 'w')

print "Truncate the file , Goodbye !"
target.truncate()

print "Now I'm going to ask you to input three lines : "

line1 = raw_input("line 1 :")
line2 = raw_input("line 2 :")
line3 = raw_input("line 3 :")

print "I am going to write these to the file ."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "Finally , we close the file."
target.close()