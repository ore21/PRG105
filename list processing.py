"""list processing"""
import random


def main():
    my_random = []
    for i in range(20):
        my_random.append(random.randrange(1, 101, 1))

    random_number = numbers()
    my_random.append(random_number)
    print(my_random)


def numbers():
    user_num = input("Enter a number between 1 - 100 :")
    print(user_num)
    return user_num


main()
