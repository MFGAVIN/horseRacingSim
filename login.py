# Retrives user info from \userDB, sends it to main.py

import json


def main():
    choice = int(input(
        '\nHello, Person of Unknowns, Would you like to either\n [1] Log In \n[2] Sign Up\n [ELSE] QUIT'))

    while choice not in [1, 2]:
        choice = int(input('ERROR: ENTERED INCORRECTLY [1 or 2]'))
    else:
        if choice == 1:
            logIn()
        else:
            signUp()


def logIn():
    username = input('\nEnter your Username: ')

    f = open('./horseDB' + '/spock.json',)

    d = json.load(f)

    for i in d['spock']:
        print(i)


def signUp():
    username = input('\nEnter your Username: ')


main()
