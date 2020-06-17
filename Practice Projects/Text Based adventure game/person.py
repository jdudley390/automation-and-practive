class Person:

    def __init__(self, person_name, level, XP, health, mana, weapon1, weapon2, armor1, armor2, support1, support2, support3):
        self.person_name = person_name
        self.level - level
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
        self.weapon.display_weapon_name()
        # Instead, do this (actually, you already do this
        # in ranged_attack())
        # print('Weapon: %s' % self.weapon.weapon_name)




