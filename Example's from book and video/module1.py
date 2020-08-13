while True:
    print('Enter you age')
    age = int(input()) #have to input as int. typo in book says just input()

    try:
       int(age)
    except:
        print('Please use numeric digits')
    if age < 1:
        print("Please Enter a positive number.")
        continue
    break
print(f'Your age is {age}.') #f is a string format tool