def main():

    dict1 = {"Name": "Archana", "Age": 32 , "Profession":"Software QA Engineer"}
    dict2 = {"Name": "Jigar", "Age": 35 , "Profession":"Devops Engineer"}
    dict3 = {"Name": "Shlok", "Age": 2 , "Profession":"nothing"}

    #dictionary has key value pair
    # We can access values in dictionary using key
    # accessing value in dictionary
    print "Value of Name in dict1 is: ", dict1["Name"]

    #del is used delete entire tuple or particular key:value in dic
    #del dict1["Profession"]
    print dict1
    #del dict3
    print dict3

    #cmp compares two dict basaed on their value and keys
    print "dict1 has same value as dict2: ", cmp(dict1,dict2)

    #len returns the length of dict
    print "len of dict1 is: ", len(dict1)

    #str returns string representation of the dict
    print "String representation of dict1 is: ", str(dict1)

    #type returns the type of passed variable
    print "dict1 is of type: ", type(dict1)

    #clear removes all the items from dict
    #dict.clear(dict1)
    #print dict1

    #copy returns the shallow copy of the dictionary
    dict4 = dict1.copy()
    print dict4

    #fromkeys creates new dictionary from the keys form the seq and value set to value
    dict5 = dict.fromkeys(dict1,("Deepen"))
    print dict5

    #get returns the value at specified key
    print "Value at Name key in dict1 is:", dict1.get("Nam","key not found")

    #has_key returns true if given key is present in dict
    print "Is Age key present in dict1: ", dict1.has_key("Age")

    #items returns the (key,value) pair of the dict
    print "(key,value) pair of dict1 is %s: ", dict1.items()

    #keys retuns the lsit of dict keys
    print "keys in dict1 is: ", dict1.keys()

    #Values returns the list of values in dict
    print "Values in the Dict1 is: ", dict1.values()

    #setdefault is similar to get , but it will set value to default if key is not found
    print "Key not found has default value: ", dict1.setdefault("Nam",None)
    print dict1
    #del dict["Nam"]

    #update value updates the dict1 with provided dict2 value
    dict1.update(dict2)
    print "Updated dict 1 is :" , dict1






main()