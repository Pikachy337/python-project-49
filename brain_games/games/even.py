#!/usr/bin/env python3
from random import randint

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def run_game():
    """ Run the 'even number' game by generating a
    random number and determining if it's even.
    """
    question = randint(0, 100)
    correct_answer = is_even(question)
    return question, correct_answer


def is_even(question):
    """Determine if a given number is even."""
    correct_answer = 'yes' if question % 2 == 0 else 'no'
    return correct_answer
