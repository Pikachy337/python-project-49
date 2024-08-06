#!/usr/bin/env python3
from brain_games.scripts.brain_even import main as bev
from brain_games.scripts.brain_progression import main as bprogr
from brain_games.scripts.brain_calc import main as bcalc
from brain_games.scripts.brain_gcd import main as bgcd
from brain_games.scripts.brain_prime import main as bprime

lst_game = ['1. Check for evenness.', '2. Calculator.',
            '3. Greatest common divisor.', '4. Arithmetic progression.',
            '5. Is it a prime number.', '6. Exit.']


def start_mini_game():
    # ceremony
    print('Hello, this is my project for Hexlet №1. ',
          'Created Dmitry Yarinsky. Edits made : 0',
          'Select the game you are interested in:', sep='\n')
    # choice the game
    counter = 0
    while counter != 15:
        print(*lst_game, sep='\n')
        game_number = input('Enter the game: ')
        if game_number == '1':
            bev()
            counter += 1
        elif game_number == '2':
            bcalc()
            counter += 1
        elif game_number == '3':
            bgcd()
            counter += 1
        elif game_number == '4':
            bprogr()
            counter += 1
        elif game_number == '5':
            bprime()
            counter += 1
        elif game_number == '6':
            break
        else:
            print('Entered the wrong number',
                  'Input number from 1 to 5.', sep='\n')
    # counter for rofls? Yes.
    if counter == 15:
        print('WOOOW! It seems you have been playing too much!',
              'Time to relax.',
              'Exit...', sep='\n')


if __name__ == '__main__':
    start_mini_game()
