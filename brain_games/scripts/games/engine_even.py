#!/usr/bin/env python3
from random import randint
from brain_games.scripts.games.welcome_user import get_user_name

counter_for_mistakes = 0
counter_for_correct_answer = 0
user_answer = ''
correct_answer = ''


def even_back():
    global correct_answer
    number = randint(0, 100)
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    result = f'Question: {number}'
    return result


def even_front():
    # Create 2 counters
    global counter_for_mistakes
    global counter_for_correct_answer
    global user_answer

    print('Answer "yes" if the number is even, otherwise answer "no".')

    while counter_for_mistakes != 3 and counter_for_correct_answer != 3:
        result = even_back()  # take question
        print(result)  # output question
        print('Your answer: ', end='')  # user input number
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
    even_front()
