import prompt
from random import randint


def main():
    print('Welcome to the Brain Games!')  # ceremony
    name = prompt.string('May I have your name?: ')
    print(f'Hello, {name}')
    print('Answer "yes" if the number is even, otherwise answer "no".')  # begin game
    counter_for_mistakes = 0
    counter_for_correct_answer = 0
    while counter_for_mistakes != 3 and counter_for_correct_answer != 3:
        number = randint(0, 100)  # form a number
        print(f'Question: {number}')  # question
        print(f'Your answer: ', end='')  # user input number
        user_answer = input()
        correct_answer = 'yes' if number % 2 == 0 else 'no'
        if user_answer != correct_answer:  # truth check
            print(f'{user_answer} is wrong answer ;(. Correct answer was {correct_answer}')
            counter_for_mistakes += 1
            print(f"Let's try again, {name}!")
        else:
            print('Correct!')
            counter_for_correct_answer += 1
