"""most frequent character"""


def main():
    letters = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'W', 'X', 'Y', 'Z')

    letter = input("Enter a string of letters :")

    print(len(letter))

    frequent_letter = " "

    for letter in letters:

        for item in range(0, 25, len(letter)):

            if letter.upper() == letters[item]:
                frequent_letter += letters[item]

    print(len(frequent_letter))


def count_letters(letter):
    count = 0

    while count <= len(letter):
        for letter in letter:
            if letter == letter[count]:
                count += 1
    return count


main()
