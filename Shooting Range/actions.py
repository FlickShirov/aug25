from weapons import Pistols, SubmachineGun

def try_gun(new_gun):
    question = input('Do you wanna try your gun: ')
    while True:
        match question.lower():
            case 'yes':
                shooting(new_gun)
                question = input('Do you wanna try your gun one more time: ')
            case 'no':
                break
            case _:
                print('You chose the wrong action')
                question = input('Do you wanna try your gun: ')

def create_new_gun():
    question = input('Do you wanna create a new gun: ')
    while True:
        match question.lower():
            case 'yes':
                new_gun = create_weapon()
                shooting(new_gun)
                question = input('Do you wanna try your gun one more time: ')
            case 'no': break
            case _:
                print('You chose the wrong action')
                question = input('Do you wanna create a new gun: ')

def create_weapon():
    weapon_type = input('Enter the type of weapon (Pistol/Submachine): ')
    model = input('Enter the name of weapon: ').title()
    ammo = int(input('Enter the count of bullets: '))
    count_magazines = int(input('Enter the count of magazines: '))
    match weapon_type.lower():
        case 'pistol':
            new_gun = Pistols(model, ammo, count_magazines)
        case 'submachine':
            new_gun = SubmachineGun(model, ammo, count_magazines)
    return new_gun

def shooting(new_gun):
    text = input('Select an action (shoot/reload/bullets/end): ')
    while True:
        match text.lower():
            case 'shoot':
                print(new_gun.shoot(int(input('How many times to shoot: '))))
                text = input('Select an action (shoot/reload/bullets/end): ')
            case 'reload':
                new_gun.reload()
                text = input('Select an action (shoot/reload/bullets/end): ')
            case 'bullets':
                print(f'The {new_gun.model} has {new_gun.ammo} bullets left')
                text = input('Select an action (shoot/reload/bullets/end): ')
            case 'end':
                break
            case _:
                print('You chose the wrong action')
                text = input('Select an action (shoot/reload/bullets/end): ')