from actions import *

#РЕАЛИЗОВАТЬ ФУНКЦИЮ С ЗАПИСЬЮ ИНФЫ О ПЕРСОНАЖЕ В JSON (УЗНАТЬ КАК ДЕЛАЕТСЯ)
#МБ ДОБАВИТЬ ЕЩЁ КЛАССОВ. ПОДУМАТЬ НАД ТЕМ, КАК СНОСИТЬ ХП И ВОЗМОЖНО ПРИКРУТИТЬ PVP
#РЕАЛИЗОВАТЬ СЮЖЕТ ДЛЯ РАЗНЫХ КЛАССОВ

def start_game():
    print('Добро пожаловать в игру "Витя практикует классы"')
    new_character = create_character()
    characteristics(new_character)
    return new_character

game(start_game())