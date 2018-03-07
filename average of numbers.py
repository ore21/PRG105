"""average of numbers"""


def numbers():
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
        total_of_numbers = str(total) + str(count)
        print("there were a total of :" + total_of_numbers)
        avg = int(num_line) / count
        print("the average of numbers is :" + avg)

        object_file.close()


numbers()
