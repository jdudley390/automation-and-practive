supplies = ['pens', 'pencil', 'paper', 'notebook']
for i, item in enumerate(supplies):
    print('Index/Item ' + str(i) + ' in supplies is: ' + item)
#these will both print the same thing just different syntax
for i in range(len(supplies)):
    print('Index/Item ' + str(i) + ' in supplies is: ' + supplies[i])


cat = ['fat', 'black', 'loud']
size = size[0]
color = cat[1]
volume = cat[2]
#These two will both assign the different item to the indiviual variables
size, color, volume = cat #assigns those variables to each item in the list cat in order

size, color, volume = 'skinny', 'blue', 'quiet' ##assign multipe variable to multiple items with multiple assignment

