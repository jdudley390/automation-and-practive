class Person:

    def __init__(self, person_name, level, XP, health, mana, weapon1, weapon2, armor1, armor2, support1, support2, support3):
        self.person_name = person_name
        self.level = level
        self.XP = XP
        self.health = health
        self.mana = mana
        self.weapon1 = weapon1
        self.weapon2 = weapon2
        self.armor1 = armor1
        self.armor2 = armor2
        self.support1 = support1 
        self.support2 = support2  
        self.support3 = support3
        
    def display_person_info(self):
        print('Name: %s' %self.person_name)
        # display_weapon_name already calls print; but
        # you probably don't need this method at all.
        self.weapon1.display_weapon_info()
        # Instead, do this (actually, you already do this
        # in ranged_attack())
        # print('Weapon: %s' % self.weapon.weapon_name)

class Support:
     #The base class for all items
    def __init__(self, name, description, value, weight):
        self.support_name = support_name
        self.description = description
        self.value = value
        self.weight = weight
    
    def display_support_info(self):
        print('Weapon Name: %s' %self.support_name)
 
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)
class Weapon:
    def __init__(self, weapon_name, weapon_damage, description, weight, value):
        self.weapon_name = weapon_name
        self.weapon_damage = weapon_damage
        self.description = description
        self.weight = weight
        self.value = value

        

    def display_weapon_info(self):
        print('Weapon Name: %s' %self.weapon_name)
        print('Weapon Weight:%s' %self.weight)
        print('Damage:%s' %self.weapon_damage)

class Shop:
    def __init__(self, item, price):
        self. item_name = item
        self.price = price
    def display_shop_items(self):
        while item != "":
            print('Item: %s' %self.item_name)
            print('Price: %s' %self.item_name, '\n')
        



    
#create instances of weapons class here
dagger = Weapon('Dagger', 6, 'Small knife', 2, 10)
long_sword = Weapon('Long Sword', 12, 'standard sword, light and weak', 4, 25)
pistol = Weapon("Pistol", 40, 'small ranged weapon', 5, 1000) #change to new class "Ranged Weapon"
shotgun = Weapon("Shotgun", 85, 'Heavy double barreled weapon. Powerful with long reload time', 9, 1900) #change to new class "Ranged Weapon"

#Create characters here
bob = Person("Bob", 0, 0,100, 0, shotgun, None, None, None, None, None, None )
james = Person("James", 0, 0, 100, 0, long_sword, None, None, None, None, None, None  )

bob.display_person_info()
james.display_person_info()


#def current_attack(self, current_weapon, target):
        #target.health -= self.weapon.weapon_damage
        #print("Weapon: %s" % self.weapon.weapon_name)
        #print(target.person_name + "'s Health: "+str(target.health))
