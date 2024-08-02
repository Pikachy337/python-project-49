from random import randint


def progression_back():
    result = []
    start_progression = randint(1, 100)
    difference = randint(2, 15)

    # Create a progression
    for i in range(randint(5, 10)):  # create a progression
        result.append(start_progression + i * difference)

    # Adding a hidden element
    del_elem = randint(0, len(result) - 1)
    correct_answer = result.pop(del_elem)
    result.insert(del_elem, '..')

    return correct_answer, result


def progression():
    correct_answer, question = progression_back()
    print('What number is missing in the progression?')
    print('Question: ', end='')
    print(*question)


if __name__ == '__main__':
    progression()
