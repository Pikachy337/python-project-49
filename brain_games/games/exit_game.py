import sys


def exit_game():
    print('Are you sure you want to exit?',
          '1.Yes 2.No', sep='\n')
    question = input('Enter the number: ')
    if question == '1':
        print('Exit...')
        sys.exit()
    elif question == '2':
        print('Back to games...')
        print('Select the game you are interested in:')
    else:
        print('Invalid number.')
        print('Back to games...')
