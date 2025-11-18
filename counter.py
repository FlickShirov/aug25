from random import randint
from time import sleep

my_list = [randint(0, 100) for _ in range(100)]
my_dict = {}
max_count = 0


for i in my_list:
    key = i
    my_dict[key] = my_list.count(i)
    if my_dict[key] > max_count:
        max_count = my_dict[key]
        max_key = key
print(my_list)
sleep(2)
print(my_dict)
sleep(2)
print(f'{max_key}: {max_count}')