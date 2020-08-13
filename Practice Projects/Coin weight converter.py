#Create a program where you can enter the weight of coins you have 
#and have it converted to $ and cents and show how many
#wrappers you would need

#Create a variable to control the loop
another = 'y'

while another == 'y':
    #have the user enter the type of coin they will use
    coin = input("What type of coin are you weighing? (Enter p for pennies, n for nickels, d for dimes, and q for quarters) ")
    ###Create a loop that will give the value of each amount of each coin
    if coin == 'p':
        p_weight = 2.5
        total_weight = int(input('Enter pounds(lbs) of pennies: '))
        weight_in_grams = total_weight * 450
        p_total = weight_in_grams / p_weight
        p_value = p_total * .01
        print('$', format(p_value, '.2f'), sep='')
    elif coin == 'n':
        n_weight = 5.0
        total_weight = int(input('Enter pounds(lbs) of nickels: '))
        weight_in_grams = total_weight * 450
        n_total = weight_in_grams / n_weight
        n_value = n_total * .05
        print('$', format(n_value, '.2f'), sep="")
    elif coin == 'd':
        d_weight = 2.26
        total_weight = int(input('Enter pounds(lbs) of dimes: '))
        weight_in_grams = total_weight * 450
        d_total = weight_in_grams / d_weight
        d_value = d_total * .1
        print('$', format(d_value, '.2f'), sep="")
    elif coin == 'q':
        q_weight = 5.6
        total_weight = int(input('Enter pounds(lbs) of quarters: '))
        weight_in_grams = total_weight * 450
        q_total = weight_in_grams / q_weight
        q_value = q_total * .25
        print('$', format(q_value, '.2f'), sep="")
    another = input('Would you like to get the value of another coin? (y/n) ')