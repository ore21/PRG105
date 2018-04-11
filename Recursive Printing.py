"""Recursive Printing"""


def main():
    count = int(input("Printing numbers :"))
    int_arg(count)


def int_arg(count):
    n = 0
    while n <= count:
        print(n)
        n += 1


main()
