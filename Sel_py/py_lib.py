import sys # sytsem specific functions and parameters
import os # provides operating system dependent functionality.
import math # for performing math functions like min(),max(),ceil() for Numbers
import random # to perform random fucntions like randrange, random(),shuffle()
import time # when we use time related fucntions methods in code

# COMMANDS FOR OS
print os.name # provides name of the operating system
print os.environ # mapping object representing string env.


for i in sys.argv: #sys.argv provides list of command line arguments
    print i

print sys.path # list of strings, path from where module has been invoked

print os.getcwd() #provides current working directory information

dirname ="."

if __name__ == '__main__':
    print 'This program is being run by itself'
else:
    print "This function is being imported from other module"

a = "100"
b = int(a)

print b