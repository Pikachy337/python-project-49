#!/usr/bin/env python3
from random import randint

DESCRIPTION = 'What is the result of the expression?'


def run_game():
    choice_operations = randint(1, 3)  # selection the game
    # random the numbers for game + and -
    number_1 = randint(0, 100)
    number_2 = randint(0, 100)
    # random the numbers for game *
    number_mult_1 = randint(1, 15)
    number_mult_2 = randint(1, 15)

    # for +
    if choice_operations == 1:
        correct_answer = number_1 + number_2
        result = f'{number_1} + {number_2}'
    # for -
    elif choice_operations == 2:
        correct_answer = max(number_1, number_2) - min(number_1, number_2)
        result = (f'{max(number_1, number_2)} - '
                  f'{min(number_1, number_2)}')
    # for *
    else:
        correct_answer = number_mult_1 * number_mult_2
        result = f'{number_mult_1} * {number_mult_2}'

    return result, str(correct_answer)
