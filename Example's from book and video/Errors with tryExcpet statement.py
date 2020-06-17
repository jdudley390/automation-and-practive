#def div42by(divideBy):
#    try:
#        return 42 / divideBy
#    except ZeroDivisionError: ##without specific exception it will catch all Errors
#        print("Error cannot divide by zero") # will print message and then return None statement still
    #except:
        #ZeroDivisionError # or wirte divideBy = 0
                           #will return None statement

#print(div42by(2))
#print(div42by(12))
#print(div42by(0)) #Divide by 0 causes error
#print(div42by(1))

print('How many cats do you own?')
cats = input()
try:
    if int(cats) >= 4:
        print("That's a lot of cats")
    elif int(cats) < 0:
        print("You can't have negative cats silly")
    else:
        print("That is not that many cats")
except:
    print("Must enter numeric value")