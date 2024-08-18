#!/usr/bin/env python3
from random import randint
from math import gcd

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def run_game():
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)
    correct_answer = gcd(number_1, number_2)
    question = f'{number_1} {number_2}'
    return question, str(correct_answer)
