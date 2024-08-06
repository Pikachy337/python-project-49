#!/usr/bin/env python3
from random import randint
from brain_games.scripts.games.welcome_user import get_user_name
from brain_games.scripts.games.check_answer import check_answer


def even_back():
    number = randint(0, 100)
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    result = f'Question: {number}'
    return result, correct_answer


def even_front():
    user_name = get_user_name()
    # redefine variables for repeated game
    counter_for_mistakes = 0
    counter_for_correct_answer = 0

    print('Answer "yes" if the number is even, otherwise answer "no".')

    while counter_for_mistakes < 3 and counter_for_correct_answer < 3:
        result, correct_answer = even_back()  # take question
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
    even_front()
