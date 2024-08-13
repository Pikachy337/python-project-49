#!/usr/bin/env python3
from random import randint
from brain_games.games.welcome_user import get_user_name
from brain_games.games.check_answer import check_answer


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

    return result, correct_answer


def progression_front():
    user_name = get_user_name()
    # redefine variables for repeated game
    counter_for_mistakes = 0
    counter_for_correct_answer = 0

    print('What number is missing in the progression?')

    while counter_for_mistakes != 1 and counter_for_correct_answer < 3:
        # Get 2 files from back
        question, correct_answer = progression_back()

        # User contact
        print('Question: ', end='')
        print(*question)
        user_answer = input('Your answer: ')

        # check answer using module
        (counter_for_correct_answer,
         counter_for_mistakes) = check_answer(user_answer, correct_answer,
                                              counter_for_correct_answer,
                                              counter_for_mistakes)

        if counter_for_correct_answer == 3:
            print(f'Congratulations, {user_name}!')


if __name__ == '__main__':
    progression_front()
