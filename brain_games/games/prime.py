from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def run_game():
    """Run the 'prime number' game by generating a
    random number and checking if it is prime.
    """
    question = randint(2, 997)

    correct_answer = is_prime(question)
    if correct_answer:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer


def is_prime(question):
    """Determine whether a number is prime based on
     the number of divisors found.
     """
    counter = 0
    for i in range(2, question // 2 + 1):
        if question % i == 0:
            counter += 1

    # if the question of divisors is 0, then the question is prime
    if counter <= 0:
        correct_answer = True
    else:
        correct_answer = False
    return correct_answer
