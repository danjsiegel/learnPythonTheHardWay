from sys import argv

script, input_file = argv

def print_all(f):   #passes in a random variable named f. When we call the function later with the parameter input_file, the function runs input_file.read()
	print f.read()

def rewind(f):
	f.seek(0)

def print_a_line(line_count, f):  #linecount by default starts at 1. each time the function runs, it sets the variable to the line. 
	print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Let's rewind, kind of like tape"

rewind(current_file)

print "let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)


