from actions import *

def start():
    print('Welcome to the Shooting Range!!!\n')
    new_gun = create_weapon()
    try_gun(new_gun)
    create_new_gun()
    print('Good Game! Well played!')

start()

