#  Задача 2. Создайте программу для игры с конфетами человек против человека.

# Правила: На столе лежит 150 конфет. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
#  За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'

# вариант человек против человека:

from random import randint

def input_dat(name):
    x = int(input(f"{name}, введите кол-во конфет, которое хотите взять от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x

def printStol(name, k, counter, value):
    print(f"Ходил {name}, он взял {k} конфет, теперь у него {counter}. На столе осталось {value} конфет.")
    print("_______________________________________________________________________________________\n")


player1 = input("Имя первого игрока: ")
# player2 = input("Имя второго игрока: ")  # Игра на двоих
player2 = "бот Тихон"  # Игра против бота
value = int(input("Введите количество конфет на столе: "))
flag = randint(0,2)
if flag:
    print(f"Первый ходит {player1}")
   
else:
    print(f"Первый ходит {player2}")
 
counter1 = 0 
counter2 = 0

def bot_calc(value):    # Игра против бота с интелектом
    k = randint(1,29)
    while value-k <= 28 and value > 29:
        k = randint(1,29)
    return k 

while value > 28:
    if flag:
        k = input_dat(player1)
        counter1 += k
        value -= k
        flag = False
        printStol(player1, k, counter1, value)
    else:
        # k = input_dat(player2)  # Игра на двоих
        # k = randint(1,29)   # Игра против бота
        k = bot_calc(value)   # Игра против бота с интелектом
        counter2 += k
        value -= k
        flag = True
        printStol(player2, k, counter2, value)

if flag:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")