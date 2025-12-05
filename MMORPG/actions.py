import random
from chars import Mage, Warrior, Priest

def choice_class(new_character_name, user_class):
    if user_class == 'Маг':
        new_character_name = Mage(new_character_name, random.randint(100, 150), random.randint(200, 250), True)
        return new_character_name
    elif user_class == 'Воин':
        new_character_name = Warrior(new_character_name, random.randint(200, 300), random.randint(100, 150), False)
        return new_character_name
    elif user_class == 'Жрец':
        new_character_name = Priest(new_character_name, random.randint(150, 200), random.randint(250, 300), True)
        return new_character_name
    else:
        return f'Неверный выбор класса'

def game(character):
    move = input('Выберите действие (Перемещение/Атака/Конец игры): ')
    while move != 'Конец игры':
        if move == "Перемещение":
            print(character.walk())
        elif move == 'Атака':
            button = input('Выберете способность (Q/W/R): ')
            target = input('Введите цель: ')
            print(character.cast(button, target))
        move = input('Выберите действие (Перемещение/Атака/Конец игры): ')

def characteristics(new_character):
    print(f'Имя персонажа: {new_character.name}')
    print(f'Здоровье: {new_character.health}')
    print(f'Мана: {new_character.mana}')
    print(f'Дальний бой' if new_character.range_attack else 'Ближний бой')

def create_character():
    new_character_name = input('Введите имя персонажа: ')
    user_class = input('Выберите класс персонажа (Маг/Воин/Жрец): ')
    choice_class(new_character_name, user_class)
    return new_character_name