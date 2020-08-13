#create a program that gets factorials
#factoial n! = n 3628800
n = int(input('Enter number ot get factorial: '))
factorial = 1
for numbers in range(1, n + 1):
    factorial = factorial * numbers
print('Factorial of', n, 'is ', factorial)


