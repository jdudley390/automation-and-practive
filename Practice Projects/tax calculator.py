price = float(input("Enter the price of the item: $"))
while price != 0:
    
    tax = price * .08
    total = tax + price
    print("The full price of the item with tax is: $", format(total, '.2f'),  "\n")
    price = float(input("Enter proce of another item orS press 0 to exit: $"))