from random import choice, randint

DESCRIPTION = 'What is the result of the expression?'


def calculate(operation, num1, num2):
    """Calculate the result of a basic arithmetic
    operation between two numbers.
    """
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2


def run_game():
    """Run the arithmetic game by generating a random
    arithmetic expression and its result.
    """
    operations = ['+', '-', '*']
    operation = choice(operations)

    if operation == '*':
        num1, num2 = randint(1, 15), randint(1, 15)
    else:
        num1, num2 = randint(0, 100), randint(0, 100)

    # Ensure the subtraction operation is non-negative
    if operation == '-' and num1 < num2:
        num1, num2 = num2, num1

    correct_answer = calculate(operation, num1, num2)
    result = f'{num1} {operation} {num2}'

    return result, correct_answer
