"""Игра угадай число"""

import numpy as np

number = np.random.randint(1, 101) # загадываем число

# количество попыток
count = 20 

# диапазон чисел
min_number = 1
max_number = 100

while count>0:  # пока число попыток не равно нулю
    count-=1
    predict_number = int(input(f"Угадай число от {min_number} до {max_number}: "))
    
    if predict_number > number:
        max_number = predict_number
        print(f'Число должно быть меньше! Осталось попыток: {count}')

    elif predict_number < number:
        min_number = predict_number
        print(f'Число должно быть больше! Осталось попыток: {count}')
    
    else:
        print(f"Вы угадали число! Это число = {number}, за {count} попыток")
        break #конец игры выход из цикла

if count==0: print("Ваши попытки закончились. Вы не угадали число!")