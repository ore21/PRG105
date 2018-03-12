"""Alphabetic Telephone Number Translator"""


def main():
    letters = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
               'U', 'V', 'W', 'X', 'Y', 'Z')
    numbers = ('2', '2', '2', '3', '3', '3', '4', '4', '4', '5', '5', '5', '6', '6', '6', '7', '7', '7', '7',
               '8', '8', '8', '9', '9', '9', '9')

    phone_number = input('enter a 10-character telephone number in the format XXX-XXX-XXXX :')

    print(len(phone_number))
    letters_final = ""
    for number in phone_number:
        for item in range(0, len(numbers)):
            if number.upper() == numbers[item]:
                letters_final += (letters[item] + " ")

    print(letters_final)


main()
