import prompt


def welcome_user():
    name = prompt.string('May I have your name?: ')
    print(f'Hello, {name}')


def get_answer(question):
    print(f"Question: {question}")
    answer = prompt.string("Your answer: ")
    return answer
