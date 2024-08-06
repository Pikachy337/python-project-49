#!/usr/bin/env python3
from random import randint
from brain_games.scripts.games.welcome_user import get_user_name
from brain_games.scripts.games.check_answer import check_answer


def prime_back():
    number = randint(1, 1000)
    counter = 0

    for i in range(2, number // 2 + 1):
        if number % i == 0:
            counter += 1

    # if the number of divisors is 0, then the number is prime
    if counter <= 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return number, correct_answer


def prime_front():
    user_name = get_user_name()
    # redefine variables for repeated game
    counter_for_mistakes = 0
    counter_for_correct_answer = 0

    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    while counter_for_mistakes < 3 and counter_for_correct_answer < 3:
        number, correct_answer = prime_back()
        print(f'Question: {number}')
        user_answer = input('Your answer: ')

        # check answer using module
        (counter_for_correct_answer,
         counter_for_mistakes) = check_answer(user_answer, correct_answer,
                                              counter_for_correct_answer,
                                              counter_for_mistakes)

        if counter_for_correct_answer == 3:
            print(f'Congratulations, {user_name}!')


if __name__ == '__main__':
    prime_front()
