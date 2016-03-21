# Data structure is collection of data of similar type. 4 types of list, tuple, dictionary, set
# most common tasks which we do with all data structure is indexing,slicing,adding, multiplying and checking for membersip

#list : ordered collection of data, list of comma seperated values enclosed in a square bracket. Non similar datatypes are allowed in list
# Once the list is created we can add,remove or alter value in list, that is why list is said to be mutable.

j = "orange"
l1 = ['apple','orange', 'kiwi', 'zukkini', 'spinach']
l2 = ['zukkini', 'spinach','okra', 'opo']
t1 = ('ant',123)

print l1[:2] #slicing
print l1[1:4] #slicing
print l2[1:]

print l1[0] #indexing
print l1[-2] # negative index

l1.append('strawberry') # adding
print l1

l1[3]= 'Cabbage' #replacing
print l1

del l1[3] #deleting
print l1

print l1[1]*3 #multiply

print l1+l2 #concat but original l1 not change
print l1

for i in l1: #iteration
    print i

if j in l1:  #membership
    print "Yes"

 # len,cmp,max,min,list are fucntion for list

print max(l1)
print min(l1)

print len(l1) # function len retuns length of string
print cmp(l1,l2) #function cmp compares content of both the list
print cmp(l2,l1)

print list(t1) # converts seq/tuple into list

# append, count, extend, remove,pop,insert,index,reverse,sort  are objects for list
l1.append("kiwi") # adds kiwi to the list
print l1

print l1.count("kiwi") # count the occurence of apple in list

l1.extend(l2) # adds contents of seq to list.
print l1

print l1.index("orange") # returns first index value of the object

print l1.pop() # removes and returs last object in the list.
print l1

l1.remove("strawberry") # remove mentioned object from the list
print l1

l1.insert(0, "mango") # inserts mentioned object at mentioned index
print l1

l1.reverse() # reverse the object of the list
print l1

l1.sort()
print l1




