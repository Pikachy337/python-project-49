#!/usr/bin/env python3
from random import randint
from brain_games.scripts.games.welcome_user import get_user_name

user_answer = ''
correct_answer = ''
counter_for_mistakes = 0
counter_for_correct_answer = 0


def progression_back():
    global correct_answer
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

    return result


def progression_front():
    # Create 2 counters
    global counter_for_mistakes
    global counter_for_correct_answer
    global user_answer
    print('What number is missing in the progression?')

    while counter_for_mistakes != 3 and counter_for_correct_answer != 3:
        # Get 2 files from back
        question = progression_back()

        # User contact
        print('Question: ', end='')
        print(*question)
        print('Your answer: ', end='')
        user_answer = input()

        # check answer using module
        check_answer()


def check_answer():
    global counter_for_correct_answer, counter_for_mistakes
    user_name = get_user_name()  # get user_name

    if user_answer == str(correct_answer):
        counter_for_correct_answer += 1
        print('Correct')
    else:
        counter_for_mistakes += 1
        print(f'{user_answer} is wrong answer ;(.'
              f'Correct answer was {correct_answer}.',
              f"Let's try again, {user_name}", sep='\n')

    if counter_for_correct_answer == 3:
        print(f'Congratulations, {user_name}')


if __name__ == '__main__':
    progression_front()
