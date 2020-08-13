#print numbers 1-100 for multipls of 3 have it print fizz
#for multiples of 5 print Buzz
#for both print fizzBuzz

#print 1-100
for i in range(1, 101):
    if i % 3 ==0 and i % 5 ==0:
        print('fizzBuzz')
    elif i % 3 ==0:
        print('fizz')
    elif i % 5 == 0:
        print('Buzz')
    
    print(i)

#notice indenting
#have to have fizzBuzz combor written before each individual
