#!/usr/bin/env python3
from random import randint
from math import gcd
from brain_games.scripts.games.welcome_user import get_user_name

user_answer = ''
correct_answer = ''
counter_for_mistakes = 0
counter_for_correct_answer = 0


def gcd_back():
    global correct_answer
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)
    correct_answer = gcd(number_1, number_2)
    result = f'Question: {number_1} {number_2}'
    return result


def gcd_front():
    global counter_for_mistakes
    global counter_for_correct_answer
    global user_answer
    print('Find the greatest common divisor of given numbers.')

    while counter_for_mistakes != 3 and counter_for_correct_answer != 3:
        result = gcd_back()
        print(result)  # output question
        print(f'Your answer: ', end='')
        user_answer = input()

        # check answer using module
        check_answer()


def check_answer():
    global counter_for_correct_answer, counter_for_mistakes
    user_name = get_user_name()  # get user_name

    if user_answer == str(correct_answer):
        counter_for_correct_answer += 1
        print('Correct')
    else:
        counter_for_mistakes += 1
        print(f'{user_answer} is wrong answer ;(.'
              f'Correct answer was {correct_answer}.',
              f"Let's try again, {user_name}", sep='\n')

    if counter_for_correct_answer == 3:
        print(f'Congratulations, {user_name}')


if __name__ == '__main__':
    gcd_front()
