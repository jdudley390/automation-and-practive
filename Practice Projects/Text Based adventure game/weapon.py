class Weapon(Item):
    def __init__(self, weapon_damage):
        self.weapon_damage = weapon_damage
        

    def display_weapon_name(self):
        print('Weapon Name: %s' %self.weapon_name)






