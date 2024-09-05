#!/usr/bin/env python3
from brain_games.scripts.brain_even import main as bev
from brain_games.scripts.brain_progression import main as bprogr
from brain_games.scripts.brain_calc import main as bcalc
from brain_games.scripts.brain_gcd import main as bgcd
from brain_games.scripts.brain_prime import main as bprime
from brain_games.exit_game import exit_game

lst_game = ['1. Check for evenness.', '2. Calculator.',
            '3. Greatest common divisor.', '4. Arithmetic progression.',
            '5. Is it a prime number.', '6. Exit.']


def main():
    """Offers the player 5 games to choose from
     and launches the selected one.
     """
    # ceremony
    print('Hello, this is my project for Hexlet №1. ',
          'Created Dmitry Yarinsky. Edits made : 18',
          'Select the game you are interested in:', sep='\n')
    # choice the game
    counter = 0
    while counter != 15:
        print(*lst_game, sep='\n')
        game_number = input('Enter the game: ')
        game_actions = {
            '1': bev,
            '2': bcalc,
            '3': bgcd,
            '4': bprogr,
            '5': bprime,
            '6': exit_game
        }
        # check value game_number
        if game_number in game_actions:
            game_actions[game_number]()
            counter += 1
        else:
            print('Invalid number. Please enter number 1-6:')

    # counter for rofls? Yes.
    if counter == 15:
        print('WOOOW! It seems you have been playing too much!',
              'Time to relax.',
              'Exit...', sep='\n')


if __name__ == '__main__':
    main()
