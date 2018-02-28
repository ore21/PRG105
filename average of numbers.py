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
        print("the total of numbers is :", total, " .2f ")
        avg = (total / count)
        print("total of numbers is :", avg, " .2f ")

        total = object_file.readline(total + count)

    object_file.close()


main()
