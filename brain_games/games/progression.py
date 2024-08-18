#!/usr/bin/env python3
from random import randint

DESCRIPTION = 'What number is missing in the progression?'


def run_game():
    # Form a numbers
    question = []
    start_progression = randint(1, 100)
    difference = randint(2, 15)

    # Create a progression
    for i in range(randint(5, 10)):
        question.append(start_progression + i * difference)

    # Adding a hidden element
    del_elem = randint(0, len(question) - 1)
    correct_answer = question.pop(del_elem)
    question.insert(del_elem, '..')

    return question, str(correct_answer)
