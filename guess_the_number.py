"""
4. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
числа используйте код:
from random import randint
num = randint(LOWER_LIMIT, UPPER_LIMIT)
"""
rom random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
MAX_ATTEMPTS = 10

# Генерируем случайное число, которое нужно угадать
num = randint(LOWER_LIMIT, UPPER_LIMIT)

print("Программа загадала число от 0 до 1000.")
print("У вас есть 10 попыток.")

for attempt in range(1, MAX_ATTEMPTS + 1):
    guess = int(input(f"Попытка {attempt}. Введите вашу догадку: "))
    
    if guess < num:
        print("Загаданное число больше.")
    elif guess > num:
        print("Загаданное число меньше.")
    else:
        print(f"Поздравляю! Вы угадали число {num} за {attempt} попыток.")
        break
else:
    print(f"К сожалению, вы исчерпали все попытки. Загаданное число было {num}.")
