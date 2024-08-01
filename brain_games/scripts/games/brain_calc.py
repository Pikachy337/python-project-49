#!/usr/bin/env python3
import prompt
from random import randint


def main():
    print('Welcome to the Brain Games!')  # ceremony
    name = prompt.string('May I have your name?: ')
    print(f'Hello, {name}')
    # begin game
    print('What is the result of the expression?')
    counter_for_mistakes = 0
    counter_for_correct_answer = 0

    while counter_for_mistakes != 3 and counter_for_correct_answer != 3:
        choice_operations = randint(1, 3)

        if choice_operations == 1:  # for +
            number_1 = randint(0, 100)
            number_2 = randint(0, 100)
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
                print("Let's try again, {name}!")
                counter_for_mistakes += 1

        elif choice_operations == 2:  # for -
            number_1 = randint(0, 100)
            number_2 = randint(0, 100)
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
                print("Let's try again, {name}!")
                counter_for_mistakes += 1

        elif choice_operations == 3:  # for *
            number_1 = randint(0, 25)
            number_2 = randint(0, 10)
            print(f'Question: {number_1} * {number_2}')
            print('Your answer: ', end='')
            user_answer = int(input())
            correct_answer = number_1 * number_2
            if user_answer == correct_answer:
                counter_for_correct_answer += 1
                print('Correct!')
            else:
                print(f"'{user_answer}' is wrong answer ;(. "
                      f"Correct answer was '{correct_answer}'")
                print("Let's try again, {name}!")
                counter_for_mistakes += 1

        if counter_for_correct_answer == 3:
            print('Congratulations, {name}')
