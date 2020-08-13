#this is close 

num = 99

for i in range(num):
    print(num, 'bottles of Beer on the wall', num, 'bottles of beer! Take one down and pass it around')
    num = num - 1
    print(num, 'bottles of beer on the wall')
    
    if num ==2:
        print(num, 'bottles of Beer on the wall', num, 'bottles of beer! Take one down and pass it around')
        print(num, 'bottle of beer on the wall')
    elif num == 1:
        print(num, 'bottle of Beer on the wall', num, 'bottle of beer! Take one down and pass it around')
        print('0 bottles of beer on the wall')


#solution
        #for quant in range(99, 0, -1):
   #if quant > 1:
      #print quant, "bottles of beer on the wall,", quant, "bottles of beer."
      #if quant > 2:
         #suffix = str(quant - 1) + " bottles of beer on the wall."
      #else:
         #suffix = "1 bottle of beer on the wall."
   #elif quant == 1:
      #print "1 bottle of beer on the wall, 1 bottle of beer."
      #suffix = "no more beer on the wall!"
   #print "Take one down, pass it around,", suffix
   #print "--"