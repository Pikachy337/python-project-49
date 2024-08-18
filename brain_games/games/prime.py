#!/usr/bin/env python3
from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def run_game():
    question = randint(1, 1000)
    counter = 0

    for i in range(2, question // 2 + 1):
        if question % i == 0:
            counter += 1

    # if the question of divisors is 0, then the question is prime
    if counter <= 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return question, correct_answer
