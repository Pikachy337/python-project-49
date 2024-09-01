#!/usr/bin/env python3
import prompt


def welcome_user():
    """Welcomes the player."""
    name = prompt.string('May I have your name?: ')
    print(f'Hello, {name}')
