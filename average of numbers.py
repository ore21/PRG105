"""average of numbers"""


def main():

    object_file = open('numbers.txt', 'r')

    num_line = object_file.readline()

    while num_line != "":
        print(num_line)
        num_line = object_file.readline()

    count = 0

    total = 0

    for num_line in object_file:

        total += int(num_line)

        count += 1

    print(total / count)

    object_file.close()


main()