# Задача 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

line = 'Итс абвтайм ту навести суетуабв'
result = ' '.join(filter(lambda x: 'абв' not in x, line.split()))
print(result)

with open('file.txt', 'w', encoding='utf-8') as f:
    f.write(result)

# Задача 2. Создайте программу для игры с конфетами человек против человека. Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

import random

def choose_player():
    p = random.randint(0,1)
    if p == 0:
        print('Первым ходит игрок 1')
    else:
        print('Первым ходит игрок 2')
    return p
 

def player1_turn(candies):
    take = 29
    while take > 28 or take < 1:
        take = int(input('Player 1, Take your candies: '))
        if take > 28 or take < 1:
            print('Please take from 1 to 28 candies: ')
        if take > candies:
            print('We do not have so many candies!')
            take = 29
    return take
        
 
def player2_turn(candies):
    take = 29
    while take > 28 or take < 1:
        take = int(input('Player 2, Take your candies: '))
        if take > 28 or take < 1:
            print('Please take from 1 to 28 candies: ')
        if take > candies:
            print('We do not have so many candies!')
            take = 29
    return take
    
    
def actual_game():
    candies = 2021
    count = 1
    turn = choose_player()
    eternity = True
    while eternity:
        if turn % 2 == 0:
            print ('Player 1!')
            take = player1_turn(candies)
            candies -= take
            print(f'Player 1 took {take} candies')
            print(f'{candies} candies left')
        elif turn % 2 == 1:
            print ('Player 2!')
            take = player2_turn(candies)
            candies -= take
            print(f'Player 2 took {take} candies')
            print(f'{candies} candies left')
        count += 1
        if candies == 0:
            if turn % 2 == 0:
                return f'Player 1 wins after {count} rounds'
            else:
                return f'Player 2 wins after {count} rounds'
            break
        turn += 1

print(actual_game())

# Задача 2 (а, b). Добавьте игру против бота. Достаточно сделать так, чтобы бот не брал конфет больше положенного или больше чем имеется в куче.b) 
# Подумайте как наделить бота ""интеллектом"".

def choose_player():
    p = random.randint(0,1)
    if p == 0:
        print('Первым ходит игрок 1')
    else:
        print('Первым ходит бот')
    return p


def player_turn(candies):
    take = 29
    while take > 28 or take < 1:
        take = int(input('Player, Take your candies: '))
        if take > 28 or take < 1:
            print('Please take from 1 to 28 candies: ')
        if take > candies:
            print('We do not have so many candies!')
            take = 29
    return take

def bot_turn(candies):
    take = candies % 29
    if take == 0:
        take = random.randint(1, 28)
    return take


def actual_game():
    candies = 100
    count = 1
    turn = choose_player()
    eternity = True
    while eternity:
        if turn % 2 == 0:
            print ('Player!')
            take = player_turn(candies)
            candies -= take
            print(f'Player took {take} candies')
            print(f'{candies} candies left')
        elif turn % 2 == 1:
            print ('Bot!')
            take = bot_turn(candies)
            candies -= take
            print(f'Bot took {take} candies')
            print(f'{candies} candies left')
        count += 1
        if candies == 0:
            if turn % 2 == 0:
                return f'Player wins after {count} rounds'
            else:
                return f'Bot wins after {count} rounds'
            break
        turn += 1

print(actual_game())