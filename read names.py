"""read file"""


def main():
    input_file = open("names.txt")
    for line in input_file:
        print(line, end="")

    record = input_file.readline()
    record = record.rstrip("\n")

    while record != "":
        print(record)
        record = input_file.readline()
        record = record.rstrip("\n")

    input_file.close()


main()
