#!/usr/bin/env python3
from random import randint


def progression_back():
    # Form a numbers
    result = []
    start_progression = randint(1, 100)
    difference = randint(2, 15)

    # Create a progression
    for i in range(randint(5, 10)):
        result.append(start_progression + i * difference)

    # Adding a hidden element
    del_elem = randint(0, len(result) - 1)
    correct_answer = result.pop(del_elem)
    result.insert(del_elem, '..')

    return correct_answer, result
