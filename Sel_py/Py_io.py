

#to read from the keyboard , we use raw_input/input
# it reads one line from std input and returns string.
import imp

#str = raw_input("Enter any number: ")
#print str

#input is same as raw_input but dif is only that python considers enter string as expression
#exp = input("Enter your input: ")
#print exp

#opening Files. before we want to perform any action on files we need to open it
# file object = open(filename [,access_mode][,buffering])
#filename = filename which we want to open
#access = indicates with what access we want to open file, eg read, write
#buffering = if specified 0 then no buffering takes place, if 1 then buffering value is 1 while accessing file.
#access : r - readu only mode. file pointing at the begining
# r+: read and write
# w: open for only writing. If does not exist creates a new file for writing.
# w+ :write and read access, overwrites the file if file exists, if not creates new for read and write
# a : file is open for appending. Pointer is at the end of the file for writing
# a+ : file is open for both reading and writing. append mode.
# rb : files opens in binary format for reading
# similar we have wb, rb+,wb+,ab, ab+

#   file object attributes
# open("filename","access:, buffering) is use to open any file
fopen = open("new.txt","r+",)
if fopen.closed:        # .closed attribute checks if file is closed
    print "File is closed"
else:
    print "File is open"

print fopen.name # name attribute returns open file name
print fopen.mode # mode attr returns in which mode file is open
print fopen.softspace # returns false if space is explicity required with print, otherwise true.

# reading and writing files
#fopen.write("this is third line.\n")
#print fopen.read()      #read() is used to read from file, if nothing is mention then it will read whole file, if mention red(10) will read first 10 lines of file
# a = fopen.readline() # readline(size) will read one line at the time with trailing new line
a = fopen.readlines()   #readlines(size) will read all lines by default or specified size and return list of strings with new line(\n).

print a
for i in a:
    print i.strip()

#File Position
print fopen.tell()   # tells the pointer position in file
fopen.seek(0,0)   #moves cursor to the specified position
print fopen.tell()

# close() method is use to close specified open file and clears all the unsaved information before closing
fopen.close()
if fopen.closed:        # code to check file is closed
    print "File is closed"
else:
    print "File is open"

#