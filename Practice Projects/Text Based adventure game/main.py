#Creat the beginning of the game
def start_game():
    #bring in game_started variable which has been set to false
    #when the game has started. This is the beginning of the game
    global game_started
    if game_started:
        return
    game_started = True


#Create a player class that will hold each differnt characters attributes
class Person:

    def __init__(self, person_name, level, job, XP, health, mana, weapon1, weapon2, armor1, armor2, support1, support2, support3, ability1, ability2):
        self.person_name = person_name
        self.level = level
        self.job = job
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
        self.ability1 = ability1
        self.ability2 = ability2
 #Create function that will display all info about person/player       
    def display_person_info(self):
        print('Name: %s' %self.person_name)
        print('Level: %s' %self.level)
        print('XP: %s' %self.XP)
        print('HP: %s' %self.health)
        print('MP: %s' %self.mana)
        self.weapon1.display_weapon()
        # Instead, do this (actually, you already do this
        # in ranged_attack())
        # print('Weapon: %s' % self.weapon.weapon_name)
#Create a loop to display nothing if parameter in class is empty
#Do this for all classes except level, XP, Mana and health
#which will all be displayed at 0 when neccesary
        if self.support1 == No:
            return None
        else:
            self.support1.display_support()
        

class Support:
     #The base class for all items
    def __init__(self, support_name, description, value, weight, type, boost):
        self.support_name = support_name
        self.description = description
        self.value = value
        self.weight = weight
        self.type = type
        self.boost = boost
    def display_support(self):
        print('Item Name: %s' %self.support_name)
    def display_support_info(self):
        print('Item Name: %s' %self.support_name)
        print('Item Type: %s' %self.type)
        print('Boost: %s' %self.boost)
        print('Item Weight: %s' %self.weight)
            
            
        
            
        
 
    
class Weapon:
    def __init__(self, weapon_name, weapon_damage, description, weight, value):
        self.weapon_name = weapon_name
        self.weapon_damage = weapon_damage
        self.description = description
        self.weight = weight
        self.value = value

        
    def display_weapon(self):
        print('Weapon Name: %s' %self.weapon_name)
    def display_weapon_info(self):
        print('Weapon Name: %s' %self.weapon_name)
        print('Weapon Weight:%s' %self.weight)
        print('Damage:%s' %self.weapon_damage, '\n')

class Shop:
    def __init__(self, item, price, weight, description):
        self. item_name = item
        self.price = price
        self.weight = weight
        self.description = description
    def display_shop_items(self):
        while item != "":
            print('Item: %s' %self.item_name)
            print('Price: %s' %self.item_name, '\n')
        




#create instances of weapons class here
#methods for weapons in order: self, weapon_name, weapon_damage, description, weight, value
No_weapon = Weapon('None', 0, "None", 0, 0)
dagger = Weapon('Dagger', 6, 'Small knife', 2, 10)
long_sword = Weapon('Long Sword', 12, 'standard sword, light and weak', 4, 25)
pistol = Weapon("Pistol", 20, 'small ranged weapon', 5, 400) #change to new class "Ranged Weapon"
shotgun = Weapon("Shotgun", 85, 'Heavy double barreled weapon. Powerful with long reload time', 9, 1900) #change to new class "Ranged Weapon"
staff = Weapon("Staff", 5, "Item that can focus magical power", 2, 15)
#create instances of support items
No = Support('None', 'None', 0, 0, 'None', 0)
hp = Support('HP Potion', 'Item that restores a small amount of health', 1, 1, 'HP', 25)
mp = Support('Mana Potion', 'Item that restores a small amount of mana', 1, 1, 'MP', 25 )
#Create characters here
#methods in order are: person_name, level, job, XP, health, mana, weapon1, weapon2, armor1, armor2, support1, support2, support3, ability1, ability2
ragnor = Person("Ragnor", 0, 'Mage', 0 ,100, 0, staff, No, No, No, mp, No, No, No, No )
issa = Person("Issa", 0, 'Knight', 0, 100, 0, long_sword, No, No, No, hp, No, No, No, No )
#gregory  =Person('Gregory')


ragnor.display_person_info()
issa.display_person_info()


#def current_attack(self, current_weapon, target):
        #target.health -= self.weapon.weapon_damage
        #print("Weapon: %s" % self.weapon.weapon_name)
        #print(target.person_name + "'s Health: "+str(target.health))



