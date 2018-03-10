"""list processing"""

my_randoms = 0
number = 0


def main():
    for i in range(20):
        my_randoms = random.ranrange(range(1, 101, 1))
        return my_randoms
        print(my_randoms)

def numbers():
    print("Enter a number between 1 - 100 :")
    print(my_randoms)

    if number == (1, 101, 1):
        print("number is greater then user's number :")

    elif number != (1, 101, 1):
        print(" there are no numbers in the list greater than the entered number :")


main()
