""""name and email adress"""

import pickle

person_email_address = 1
name = 2
num = 3


def main():
    try:
        input_file = open("user dictionary", 'rb')
        names = pickle.load(input_file)
        print(names)
    except(FileNotFoundError, IOError):
        print("file not found, please enter a name and an email then quit to create the file :")
        names = {}

    choice = 0

    while choice != num:

        choice = menu()

    if choice == person_email_address:
        (person_email_address(names))
    elif choice == name:
        (name(names))
    elif choice == num:
        (num(names))


def menu():
    print()
    print('name and email address')
    print('-----------------------')
    print('1. Look up an email address')
    print('2. Look up a name')
    print('3. Look up a phone number')

    choice = int(input('Enter a number of your choice: '))
    while choice < 1 or choice > 3:
        choice = int(input('Enter a valid choice: '))
    return choice


def person_email(names):
    person_email_address = input('Enter an email adress: ')
    print(names.get(person_email_address, 'not found'))


def person_name(names):
    person_email_address = input('Enter an email address: ')
    name = input('Enter a name: ')
    if person_email_address not in names:
        names[person_email_address] = name
    else:
        print(' That entry already exists.')


def person_number(names):
    person_email_address = input('Enter an email address: ')
    person_number = input('Enter a phone number: ')
    if person_email_address not in names:
        names[person_email_address] = person_number
    else:
        print(' That entry already exists.')


main()
