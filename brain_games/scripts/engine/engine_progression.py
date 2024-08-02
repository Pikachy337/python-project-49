from random import randint

print('Welcome to the Brain Games!')  # ceremony
print('May I have your name?: ', end='')
user_name = input()
print(f'Hello, {user_name}!')


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


def progression_front():
    # Create 2 counters
    counter_for_mistakes = 0
    counter_for_correct_answer = 0

    while counter_for_mistakes != 3 and counter_for_correct_answer != 3:
        # Get 2 files from back
        correct_answer, question = progression_back()

        # User contact
        print('What number is missing in the progression?')
        print('Question: ', end='')
        print(*question)

        # User input number
        print('Your answer: ', end='')
        user_answer = input()
        # Check result
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
