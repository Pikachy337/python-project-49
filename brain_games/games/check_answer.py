from brain_games.games.welcome_user import get_user_name


def check_answer(user_answer, correct_answer,
                 counter_for_correct_answer, counter_for_mistakes):
    user_name = get_user_name()  # get user_name

    if user_answer == str(correct_answer):
        counter_for_correct_answer += 1
        print('Correct!')
    else:
        counter_for_mistakes += 1
        print(f"'{user_answer}' is wrong answer ;(. "
              f"Correct answer was '{correct_answer}'.",
              f"Let's try again, {user_name}!", sep='\n')
    return counter_for_correct_answer, counter_for_mistakes
