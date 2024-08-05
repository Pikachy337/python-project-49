#!/usr/bin/env python3
from random import randint
from brain_games.scripts.games.welcome_user import get_user_name

user_answer = ''
correct_answer = ''
counter_for_mistakes = 0
counter_for_correct_answer = 0


def calc_back():
    global correct_answer
    choice_operations = randint(1, 3)  # selection the game
    # random the numbers for game + and -
    number_1 = randint(0, 100)
    number_2 = randint(0, 100)
    # random the numbers for game *
    number_mult_1 = randint(1, 15)
    number_mult_2 = randint(1, 15)

    # for +
    if choice_operations == 1:
        correct_answer = number_1 + number_2
        result = f'Question: {number_1} + {number_2}'
    # for -
    elif choice_operations == 2:
        correct_answer = max(number_1, number_2) - min(number_1, number_2)
        result = (f'Question: {max(number_1, number_2)} - '
                  f'{min(number_1, number_2)}')
    # for *
    else:
        correct_answer = number_mult_1 * number_mult_2
        result = f'Question: {number_mult_1} * {number_mult_2}'

    return result


def calc_front():
    global counter_for_mistakes
    global counter_for_correct_answer
    global user_answer
    print('What is the result of the expression?')

    while counter_for_mistakes != 3 and counter_for_correct_answer != 3:
        result = calc_back()
        print(result)
        print('Your answer: ', end='')
        user_answer = int(input())

        # check answer using module
        check_answer()


def check_answer():
    global counter_for_correct_answer, counter_for_mistakes
    user_name = get_user_name()  # get user_name

    if str(user_answer) == str(correct_answer):
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
    calc_front()
