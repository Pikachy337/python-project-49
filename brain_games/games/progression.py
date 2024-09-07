from random import randint

DESCRIPTION = 'What number is missing in the progression?'


def run_game():
    """Run the 'missing number in progression' game by
    generating a sequence of numbers with one missing.
    """
    progr = generate_sequence()
    # Adding a hidden element
    del_elem = randint(0, len(progr) - 1)
    correct_answer = progr.pop(del_elem)
    progr.insert(del_elem, '..')
    question = ' '.join(map(str, progr))
    return question, correct_answer


def generate_sequence():
    """Generate an arithmetic progression."""
    # Form a numbers
    progr = []
    start_progression = randint(1, 100)
    difference = randint(2, 15)

    # Create a progression
    for i in range(randint(5, 10)):
        progr.append(start_progression + i * difference)

    return progr
