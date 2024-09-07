import prompt

MAX_SCORE = 3


def game_run(game):
    """Run the game engine for a given game module."""
    print('Welcome to the Brain Games!')
    user_name = input('May I have your name?: ')
    print(f'Hello, {user_name}!')

    print(game.DESCRIPTION)
    score = 0
    while score < MAX_SCORE:
        question, correct = game.run_game()

        print(f"Question: {question}")
        answer = prompt.string("Your answer: ")

        if answer != str(correct):
            print(
                f"'{answer}' is wrong answer ;(.",
                f"Correct answer was '{correct}'.",
            )
            print(f"Let's try again, {user_name}!")
            return

        print("Correct")
        score += 1

    print(f"Congratulations, {user_name}!")
