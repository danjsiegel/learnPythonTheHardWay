from sys import argv #tells it to pass arguments into the file

script, filename = argv #defines the arguments in the file

txt = open(filename) #function which is called variable txt, tells it to open a file, and the file to open is the variable passed into the script

print "Here's your file %r: " % filename   #just printsout the line
print txt.read()  #tells it to execute the function and .read() tells it to perform the action read, with no arguments passed into it


print "Type the filename again:"  #just a line of text
file_again = raw_input(">")  #prompts the user to pass in a new file name

txt_again = open(file_again)  #same as before 

print txt_again.read() #same as before
