from brain_games.games.welcome_user import welcome_user, get_user_name
from brain_games.cli import get_answer

MAX_SCORE = 3


def game_run(game):
    welcome_user()

    print(game.DESCRIPTION)
    score = 0
    while score < MAX_SCORE:
        question, correct = game.run_game()
        answer = get_answer(question)

        if answer != correct:
            print(
                f"'{answer}' is wrong answer ;(.",
                f"Correct answer was '{correct}'.",
            )
            print(f"Let's try again, {get_user_name()}!")
            return

        print("Correct")
        score += 1

    print(f"Congratulations, {get_user_name()}!")
