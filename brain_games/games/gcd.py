from random import randint
from math import gcd

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def run_game():
    """Run the 'greatest common divisor' game by generating
     two random numbers and calculating their GCD.
     """
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)
    correct_answer = gcd(number_1, number_2)
    question = f'{number_1} {number_2}'
    return question, correct_answer
