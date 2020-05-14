# _*_ coding:utf-8 _*_
from sys import argv
script , input_file = argv
def print_all(f):
	print f.read()
	
def rewind(f):
	f.seek(0)

def print_a_line(line_count, f):
	print line_count, f.readline()
	
current_file = open(input_file)
print "-" * 60
print "Print all the content : "
print_all(current_file)
print "-" * 60
print "Now let us rewind : "
rewind(current_file)
print "-" * 60
print "Let's print three lines : "
current_line = 1
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)