"""read file"""


def names():
    input_file = open("names.txt", "r")
    num = input_file.readline()
    total = 0

    while num != "":
        print(num)
        num = input_file.readline()
        total += 1

    input_file.close()
    print("you had total of :" + num)
    print(total)
    print("names ")


names()
