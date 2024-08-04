#!/usr/bin/env python3
from random import randint


def welcome_user():
    print('Welcome to the Brain Games!')  # ceremony
    print('May I have your name?: ', end='')
    global user_name
    user_name = input()
    print(f'Hello, {user_name}!')


def prime_back():
    number = randint(1, 1000)
    correct_answer = ''
    counter = 0

    for i in range(2, number // 2 + 1):
        if number % i == 0:
            counter += 1
    # if the number of divisors is 0
    # then the number is prime
    if counter <= 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return number, correct_answer


def prime_front():
    counter_for_mistakes = 0
    counter_for_correct_answer = 0
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    while counter_for_mistakes != 3 and counter_for_correct_answer != 3:
        number, correct_answer = prime_back()
        print(f'Question: {number}')
        print(f'Your answer: ', end='')
        user_answer = input()

        # check answer
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
    welcome_user()
    prime_front()
