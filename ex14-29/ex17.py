from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying form %s to %s" % (from_file, to_file)

# we can do these next 2 commands in a single line, will probably be a part of the study drills
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bypes long" % len(indata)

print "does the output file exist? %r" % exists(to_file)
print "Ready, hit return to continue, Ctrl-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done"

out_file.close()
in_file.close()
