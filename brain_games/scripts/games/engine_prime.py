#!/usr/bin/env python3
from random import randint
from brain_games.scripts.games.welcome_user import get_user_name

user_answer = ''
correct_answer = ''
counter_for_mistakes = 0
counter_for_correct_answer = 0


def prime_back():
    number = randint(1, 1000)
    counter = 0
    global correct_answer

    for i in range(2, number // 2 + 1):
        if number % i == 0:
            counter += 1
    # if the number of divisors is 0
    # then the number is prime
    if counter <= 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return number


def prime_front():
    # Create 2 counters
    global counter_for_mistakes
    global counter_for_correct_answer
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    while counter_for_mistakes != 3 and counter_for_correct_answer != 3:
        number = prime_back()
        print(f'Question: {number}')
        print(f'Your answer: ', end='')
        global user_answer
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
    prime_front()
