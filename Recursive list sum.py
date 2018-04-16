"""Recursive list sum"""


def main():
    num_list = [3, 4, 5, 7, 9, 12]
    num(num_list)


def num(num_list):
    if len(num_list) > 1:
        print(num_list[0])
        num_list[0] += num_list[1]
        num_list.pop(1)
        num(num_list)

    else:
        display = num_list[0]
        print("your total is : " + str(display))


main()
