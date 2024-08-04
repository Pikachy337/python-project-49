#!/usr/bin/env python3
from random import randint
from math import gcd


def welcome_user():
    print('Welcome to the Brain Games!')  # ceremony
    print('May I have your name?: ', end='')
    global user_name
    user_name = input()
    print(f'Hello, {user_name}!')


def gcd_back():
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)
    return number_1, number_2


def gcd_front():
    counter_for_mistakes = 0
    counter_for_correct_answer = 0
    print('Find the greatest common divisor of given numbers.')

    while counter_for_mistakes != 3 and counter_for_correct_answer != 3:
        number_1, number_2 = gcd_back()
        print(f'Question: {number_1} {number_2}')
        print(f'Your answer: ', end='')
        user_answer = int(input())
        correct_answer = gcd(number_1, number_2)

        # Check result
        if user_answer != correct_answer:
            print(f'{user_answer} is wrong answer ;(. '
                  f'Correct answer was {correct_answer}')
            counter_for_mistakes += 1
            print(f"Let's try again, {user_name}!")
        else:
            print('Correct!')
            counter_for_correct_answer += 1
            # Congratulations
        if counter_for_correct_answer == 3:
            print(f'Congratulations, {user_name}')
