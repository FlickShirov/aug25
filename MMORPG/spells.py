class Spells:

    def mage_cast_choice(self, button, target):
        match button.upper():
            case 'Q':
                return f'{self.name} is casting Crystal Nova on {target}'
            case 'W':
                return f'{self.name} is casting Frostbite on {target}'
            case 'R':
                return f'{self.name} is casting Freezing Field on {target}'
            case _:
                return f'{self.name} has not this spell'
    
    def warrior_cast_choice(self, button, target):
        match button.upper():
            case 'Q':
                return f'{self.name} is casting Shield Bash on {target}'
            case 'W':
                return f'{self.name} is casting Overpower on {target}'
            case 'R':
                return f'{self.name} is casting Revenge on {target}'
            case _:
                return f'{self.name} has not this spell'
            
    def priest_cast_choice(self, button, target):
        match button.upper():
            case 'Q':
                return f'{self.name} is casting Healing on {target}'
            case 'W':
                return f'{self.name} is casting Battle Ressurection on {target}'
            case 'R':
                return f'{self.name} is casting Global Stun on {target}'
            case _:
                return f'{self.name} has not this spell'