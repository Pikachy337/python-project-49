#!/usr/bin/env python3
from random import randint


def welcome_user():
    print('Welcome to the Brain Games!')  # ceremony
    print('May I have your name?: ', end='')
    global user_name
    user_name = input()
    print(f'Hello, {user_name}!')


def even_back():
    number = randint(0, 100)
    return number


def even_front():
    # Create 2 counters
    counter_for_mistakes = 0
    counter_for_correct_answer = 0

    print('Answer "yes" if the number is even, otherwise answer "no".')

    while counter_for_mistakes != 3 and counter_for_correct_answer != 3:
        number = even_back()  # form a number
        print(f'Question: {number}')  # question
        print('Your answer: ', end='')  # user input number
        user_answer = input()
        correct_answer = 'yes' if number % 2 == 0 else 'no'

        # check answer
        if user_answer != correct_answer:  # truth check
            print(f'{user_answer} is wrong answer ;(. '
                  f'Correct answer was "{correct_answer}"')
            counter_for_mistakes += 1
            print(f"Let's try again, {user_name}!")
        else:
            print('Correct!')
            counter_for_correct_answer += 1


if __name__ == '__main__':
    welcome_user()
    even_front()
