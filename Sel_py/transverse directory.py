#!/usr/bin/python

import os

# traverse root directory, and list directories as dirs and files as files
for root, dirs, files in os.walk("."):
    path = root.split('/')
    print (len(path) - 1) *'---' , os.path.basename(root) # will display only the tail part of the path eg item in
    for file in files:
        print len(path)*'---', file