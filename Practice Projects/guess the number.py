import random

number = random.randint(1, 10)
guesses = 0
print('enter a number between 1 and 10')
while guesses < 5:

    myNumber = int(input())
    if myNumber > number:
        print("That's too high!")
        print("Pick another number")
        
    elif myNumber < number:
        print("That's too low!")
        print("Pick another number")
        
    elif myNumber == number:
        print("You got it right!")

    guesses += 1