#Multiple list inside of a list
list = [["cat", "bat"], [10,20,30,40]] #this is a list of 2 lists
print(list[0][1]) #this will print the 2nd item in the first list (remember start at 0 not 1 for index)

#assign new value to an item in a list

list1 = [10, 20, 30]
print(list1)
list1 [1] = 'Hello' ## will replace the number 20 with 'Hello'
list1[2:3] = [6, 8] #replaces 30 with 6 and adds 8 to index[3]
print(list1)

#if you use a number higher than the lists length with a slice it will add on to the list

'howdy' in ['hello', 'hi', 'howdy', 'hey'] #will evalute to true since value is in list
#not in operates the same way
'howdy' not in ['hello', 'hi', 'howdy', 'hey'] #will evaluate to false