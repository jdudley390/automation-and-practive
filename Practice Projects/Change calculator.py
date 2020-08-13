#Wite a program that will give which coins are needed to make change
#i.e. if the change is $.58 have program show 2 quarters, 5 nickels, 3 pennies
#allow the user to put in cost and how much money is given to them
#then have change calulated

def main():
    total_cost = float(input("Item cost: $"))
    make_change(total_cost)

    

def make_change(cost):
    customer_pay = float(input("Total received: $"))
    change = customer_pay - cost
    print('Change: $', format(change, '.2f'))
    

main()