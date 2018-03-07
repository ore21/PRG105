"""read file"""


def main():
    input_file = open('names.txt', 'r')
    print(input_file.readline)

    num = input_file.readline()

    while num != "":
        print(num)
        num = input_file.readline()
        
    input_file.close()


main()
