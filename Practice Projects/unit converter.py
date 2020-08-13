#convert units in python
#write seperate funtions for each conversion
#convert cups ot fluid ounces

def cups_to_flOZ(number):
    flOZ = number * 8
    print(flOZ, '.2f', "FL OZ")

def miles_to_km(number):
    km = number * 1.609
    print(format(km, '.2f'), "KM")

num = float(input("Enter number to be converted: "))
miles_to_km(num)
#cups_to_flOZ(num)