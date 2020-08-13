#Right a program so a user can put in the sides of a triangle
#and determine if it is a pythagorean triple

#Create variable to allow loop to repeat
#Make sure the user can enter the sides in any order
again = 'y'

while again.lower() == 'y':
    print('Please enter the length of all three sides of the triangle')
    side1 = int(input('Side 1: '))
    side2 = int(input('Side 2: '))
    side3 = int(input('Side 3: '))
    if side3 > side1 and side3 > side2:
        a = side1**2
        b = side2**2
        c = side3**2
        ab = a + b
    
        if ab == c:
            print("This is a pythagorean triple")
        else:
            print('This is not a pythagorean triple')
    elif side1 > side2 and side1 > side3:
        c = side1**2
        b = side2**2
        a = side3**2
        ab = a + b
        if ab == c:
            print("This is a pythagorean triple")
        else:
            print('This is not a pythagorean triple') 
    elif side2 > side1 and side2 > side3:
        b = side1**2
        a = side2**2
        c = side3**2
        ab = a + b
        if ab == c:
            print("This is a pythagorean triple")
        else:
            print('This is not a pythagorean triple')
        
    again = input('Would you like to check another 2 sides? (y/n) ')
    
#finished correctly!!!!