"""initials"""


def main():

    name = input('enter a full name containing first, second, and last : ')
    name = name.split()

    print(name)

    first = name[0][0]
    second = name[1][0]
    last = name[2][0]

    print(first, '.', second, '.', last, '.')


main()
