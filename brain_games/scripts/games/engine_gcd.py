#!/usr/bin/env python3
from random import randint
from math import gcd
from brain_games.scripts.games.welcome_user import get_user_name
from brain_games.scripts.games.check_answer import check_answer


def gcd_back():
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)
    correct_answer = gcd(number_1, number_2)
    result = f'Question: {number_1} {number_2}'
    return result, correct_answer


def gcd_front():
    user_name = get_user_name()
    # redefine variables for repeated game
    counter_for_mistakes = 0
    counter_for_correct_answer = 0

    print('Find the greatest common divisor of given numbers.')

    while counter_for_mistakes < 3 and counter_for_correct_answer < 3:
        result, correct_answer = gcd_back()
        print(result)  # output question
        user_answer = input('Your answer: ')

        # check answer using module
        (counter_for_correct_answer,
         counter_for_mistakes) = check_answer(user_answer, correct_answer,
                                              counter_for_correct_answer,
                                              counter_for_mistakes)

        if counter_for_correct_answer == 3:
            print(f'Congratulations, {user_name}!')


if __name__ == '__main__':
    gcd_front()
