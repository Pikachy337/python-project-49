#!/usr/bin/env python3
from random import randint

DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def run_game():
    question = randint(0, 100)
    correct_answer = 'yes' if question % 2 == 0 else 'no'
    return question, correct_answer
