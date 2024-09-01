#!/usr/bin/env python3
def welcome_user():
    print('Welcome to the Brain Games!')
    user_name = input('May I have your name?: ')
    print(f'Hello, {user_name}!')
    return user_name


def get_user_name():
    return welcome_user()


if __name__ == '__main__':
    welcome_user()
