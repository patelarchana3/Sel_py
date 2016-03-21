#tuple is immutable data structue. They are enclosed in parantheses

t1 = ('apple', 100, 120.35, 'hello')
t2 = (1458, 'as', 'tuple')
l1 = [100, 200, 300]

t3 = () # empty tuple
t4 = (50,) # even if have only one object in tuple we need to use comma

# accessing tuple
print t1[0]
print t1[:2]
print t1[2:]

#tuple is immutabble so cannot update or change the values of the tuple. we can create new tuple from them
# t1[0] = "100" this is not allowed for tuple

#removing indivdual object is not possible with tuple so we have to delete entire tuple

# len,concat (+), multiple(*), iteration, in

print len(t1) #returns len of the object in tuple

t3 = t1 + t2 # returns  new tuple concat two tuple
print t3

print t2 *3 # multiple

for i in t1:
    print i
    if i in t2:
        print "Yes"
    else:
        print "no"

# cmp, len, min, max, tuple,
print cmp(t1,t2)
print len(t2)
print max(t1)
print min(t1)
print tuple(l1)
