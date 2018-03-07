"""read file"""


def names():
    input_file = open("names.txt", "r")

    num = input_file.readline()

    while num != "":
        print(num)
        num = input_file.readline()

    input_file.close()


names()
