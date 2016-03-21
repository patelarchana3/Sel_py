# os module provides method that

import os

print os.path  # provides path of current directory
print os.name   #provides name of current os
print os.environ  # provides env paths as a dict

#renaming and deleting file
#os.rename("imp.txt","new1.txt")        # rename is use to rename the file
os.remove("new.txt")    # remove will removed file from specifc provided path

#directory commands
#os.mkdir("sample")

#os.chdir("sample")      #change current working directory
print os.getcwd()       # get the information of current working directory

#os.rmdir("sample")      # remove directory
