#!/usr/bin/env python3
import prompt
from random import randint
from math import gcd


def main():
    print('Welcome to the Brain Games!')  # ceremony
    name = prompt.string('May I have your name?: ')
    print(f'Hello, {name}')
    # begin game
    print('Find the greatest common divisor of given numbers.')
    counter_for_mistakes = 0
    counter_for_correct_answer = 0
    while counter_for_mistakes != 3 and counter_for_correct_answer != 3:
        number_1 = randint(1, 100)
        number_2 = randint(1, 100)
        print(f'Question: {number_1} {number_2}')
        print(f'Your answer: ', end='')
        user_answer = int(input())
        correct_answer = gcd(number_1, number_2)
        # Check
        if user_answer != correct_answer:
            print(f'{user_answer} is wrong answer ;(. '
                  f'Correct answer was {correct_answer}')
            counter_for_mistakes += 1
            print(f"Let's try again, {name}!")
        else:
            print('Correct!')
            counter_for_correct_answer += 1
            # Congratulations
        if counter_for_correct_answer == 3:
            print(f'Congratulations, {name}')
