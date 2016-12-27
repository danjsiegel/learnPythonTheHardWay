filename = raw_input("give me the file name: ")

print "We're going to erase %r." % filename
print "If you don't want that, hit Ctrl-C (^-C)."
print "If you do want that, hit Return."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for 3 lines."

line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

print "I'm going to write these to the file"

target.write('%s\n%s\n%s\n' % (line1, line2, line3))

print "And finally, we close it."
target.close()

