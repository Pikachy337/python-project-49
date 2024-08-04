#!/usr/bin/env python3
from random import randint


def welcome_user():
    print('Welcome to the Brain Games!')  # ceremony
    print('May I have your name?: ', end='')
    global user_name
    user_name = input()
    print(f'Hello, {user_name}!')


def calc_back():
    choice_operations = randint(1, 3)  # selection the game
    # random the numbers for game + and -
    number_1 = randint(0, 100)
    number_2 = randint(0, 100)
    # random the numbers for game *
    number_mult_1 = randint(1, 15)
    number_mult_2 = randint(1, 15)
    return choice_operations, number_1, number_2, number_mult_1, number_mult_2


def calc_front():
    counter_for_mistakes = 0
    counter_for_correct_answer = 0
    print('What is the result of the expression?')

    while counter_for_mistakes != 3 and counter_for_correct_answer != 3:
        choice_operations, number_1, number_2, number_mult_1, number_mult_2 = calc_back()

        if choice_operations == 1:  # for +
            print(f'Question: {number_1} + {number_2}')
            print('Your answer: ', end='')
            user_answer = int(input())
            correct_answer = number_1 + number_2
            if user_answer == correct_answer:
                counter_for_correct_answer += 1
                print('Correct!')
            else:
                print(f"'{user_answer}' is wrong answer ;(. "
                      f"Correct answer was '{correct_answer}'")
                print(f"Let's try again, {user_name}!")
                counter_for_mistakes += 1

        elif choice_operations == 2:  # for -
            print(f'Question: {max(number_1, number_2)} - '
                  f'{min(number_1, number_2)}')
            print('Your answer: ', end='')
            user_answer = int(input())
            correct_answer = max(number_1, number_2) - min(number_1, number_2)
            if user_answer == correct_answer:
                counter_for_correct_answer += 1
                print('Correct!')
            else:
                print(f"'{user_answer}' is wrong answer ;(. "
                      f"Correct answer was '{correct_answer}'")
                print(f"Let's try again, {user_name}!")
                counter_for_mistakes += 1

        elif choice_operations == 3:  # for *
            print(f'Question: {number_mult_1} * {number_mult_2}')
            print('Your answer: ', end='')
            user_answer = int(input())
            correct_answer = number_mult_1 * number_mult_2
            if user_answer == correct_answer:
                counter_for_correct_answer += 1
                print('Correct!')
            else:
                print(f"'{user_answer}' is wrong answer ;(. "
                      f"Correct answer was '{correct_answer}'")
                print(f"Let's try again, {user_name}!")
                counter_for_mistakes += 1

        if counter_for_correct_answer == 3:
            print(f'Congratulations, {user_name}')


if __name__ == '__main__':
    welcome_user()
    calc_front()
