#!/usr/bin/env python3
from random import randint

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def run_game():
    """ Run the 'even number' game by generating a
    random number and determining if it's even.
    """
    question = randint(0, 100)
    if is_even(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer


def is_even(question):
    """Determine if a given number is even."""
    correct_answer = question % 2 == 0
    return correct_answer
