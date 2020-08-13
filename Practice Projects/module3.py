price = float(input("Enter the price of the item: $"))
while price != 0:
    
    tax = price * .08
    total = tax + price
    print("The full price of the item with tax is: $", total, "\n")
    price = float(input("Enter another item of press 0 to exit: $"))