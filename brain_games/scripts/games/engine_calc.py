#!/usr/bin/env python3
from random import randint
from brain_games.scripts.games.welcome_user import get_user_name
from brain_games.scripts.games.check_answer import check_answer


def calc_back():
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
        result = f'Question: {number_1} + {number_2}'
    # for -
    elif choice_operations == 2:
        correct_answer = max(number_1, number_2) - min(number_1, number_2)
        result = (f'Question: {max(number_1, number_2)} - '
                  f'{min(number_1, number_2)}')
    # for *
    else:
        correct_answer = number_mult_1 * number_mult_2
        result = f'Question: {number_mult_1} * {number_mult_2}'

    return result, correct_answer


def calc_front():
    user_name = get_user_name()
    # redefine variables for repeated game
    counter_for_mistakes = 0
    counter_for_correct_answer = 0

    print('What is the result of the expression?')

    while counter_for_mistakes < 3 and counter_for_correct_answer < 3:
        result, correct_answer = calc_back()
        print(result)
        user_answer = input('Your answer: ')

        # check answer using module
        (counter_for_correct_answer,
         counter_for_mistakes) = check_answer(user_answer, correct_answer,
                                              counter_for_correct_answer,
                                              counter_for_mistakes)

        if counter_for_correct_answer == 3:
            print(f'Congratulations, {user_name}')


if __name__ == '__main__':
    calc_front()
