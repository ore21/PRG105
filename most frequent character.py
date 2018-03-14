"""Most Frequent Character"""

letters = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
           'W', 'X', 'Y', 'Z')


def main():
    letter = input("Enter a string of letters :")
    print(len(letter))
    frequent_letter = " "
    for letter in letters:
        for item in range(25, len(letters)):
            if letter.upper() == letters[item]:
                frequent_letter += letters[item]
    print(frequent_letter)


def letter_times(letter):
    if letter > 2:
        print("your letter appeared more then once ")

    elif letter <= 2:
        print("your letter appeared only once ")

    else:
        print("replace the value")


print(letter_times)

def count_letters(letters):
    count = 0
    while



main()
