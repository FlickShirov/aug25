from spells import Spells


class Character:

    def __init__(self, name, health, mana, range_attack : bool):
        self.name = name
        self.health = health
        self.mana = mana
        self.range_attack = range_attack
        
    def walk(self):
        pass

    def cast(self, button, target):
        pass


class Mage(Character):

    def __init__(self, name, health, mana, range_attack : bool):
        super().__init__(name, health, mana, range_attack)
        self.range_attack = True
    
    def walk(self):
        return f'{self.name} is flying'
    
    def cast(self, button, target):
        return Spells.mage_cast_choice(self, button, target)
    

class Warrior(Character):

    def __init__(self, name, health, mana, range_attack : bool):
        super().__init__(name, health, mana, range_attack)
        self.range_attack = False
    
    def walk(self):
        return f'{self.name} is running'
    
    def cast(self, button, target):
        return Spells.warrior_cast_choice(self, button, target)
    

class Priest(Character):
    
    def __init__(self, name, health, mana, range_attack : bool):
        super().__init__(name, health, mana, range_attack)
        self.range_attack = True

    def walk(self):
        return f'{self.name} is walking'
    
    def cast(self, button, target):
        return Spells.priest_cast_choice(self, button, target)