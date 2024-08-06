user_name = None


def welcome_user():
    global user_name
    if user_name is None:
        print('Welcome to the Brain Games!')
        user_name = input('May I have your name?: ')
        print(f'Hello, {user_name}!')
    return user_name


def get_user_name():
    return user_name


if __name__ == '__main__':
    welcome_user()
