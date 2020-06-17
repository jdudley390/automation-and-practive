import collections
#Create inventory for table top game
#Create Dictionary with items name and weight
print("Welcome to Table top gaming!")
print("First choose the number of players: ")
players = int(input())

weapon_inventory = {'Long Sword' : 12, 'Broad Sword' : 15, 'Dagger' : 5}
armor_inventory = {'Light armor' : 15, 'Dark armor' : 20, 'Heavy armor' : 25}
support_inventory = {'Health potion' : 2, 'Mana potion' : 2, 'Elixir of life' : 2 }

for p in range(players):
    
    print('Choose your characters name')
    name = input()
    print('Your character can only carry 32lbs of equipment right now, Choose wisely!\n')
    #create loop that tells you the name of each item and how much it weighs
    for key, value in weapon_inventory.items():
        print("The", key, 'weighs', value, 'pounds')
    print('')
    

    for key, value in armor_inventory.items():
        print("The", key, 'weighs', value, 'pounds')
    print('')    

    for key, value in support_inventory.items():
        print("The", key, 'weighs', value, 'pounds')
    
    print('Choose 1 item from each category')
    print('First a weapon')
    weapon = input()
    if weapon in weapon_inventory:
        weight = 0
        for key, value in weapon_inventory.items():
            weight = weight + value.get(items, 0)
            print(weight)
        

        
