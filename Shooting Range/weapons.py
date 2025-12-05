class Weapon():
    def __init__(self, model, ammo : int, count_magazine : int):
        self.model = model
        self.ammo = ammo
        self.max_ammo = self.ammo
        self.count_magazine = count_magazine

    def shoot(self):
        pass

    def reload(self):
        pass

class Pistols(Weapon):
    def __init__(self, model, ammo : int, count_magazine : int):
        super().__init__(model, ammo, count_magazine)


    def shoot(self, bullets):
        if self.ammo > 0 and 0 < bullets <= self.ammo:
            s = f'{self.model} shooting like {"PIFF-PUFF" + ("-PIFF-PUFF" * (bullets-1))}'
            self.ammo -= bullets
            return s
        elif bullets > self.ammo > 0: return f'The weapon has {self.ammo} bullets. No more.'
        else: return f'{self.model} needs to reload'

    def reload(self):
        if self.count_magazine - 1 == 0:
            print(f'The {self.model} has no magazines')
        else:
            print('Reloading...')
            self.ammo = self.max_ammo
            print('Reload complete')
            self.count_magazine -= 1


class SubmachineGun(Weapon):
    def __init__(self, model, ammo : int, count_magazine : int):
        super().__init__(model, ammo, count_magazine)

    def shoot(self, bullets):
        if self.ammo > 0 and 0 < bullets <= self.ammo:
            s = f'{self.model} shooting like {"RATATA" + ("-TATA" * (bullets - 1))}'
            self.ammo -= bullets
            return s
        elif bullets > self.ammo > 0: return f'The weapon has {self.ammo} bullets. No more.'
        else: return f'{self.model} needs to reload'

    def reload(self):
        if self.count_magazine - 1 == 0:
            return f'The {self.model} has no magazines'
        else:
            print('Reloading...')
            self.ammo = self.max_ammo
            print('Reload complete')
            self.count_magazine -= 1

