"""popular names"""


def main():
    input_file = open('BoyNames.txt', 'r')
    boy_names = input_file.readlines()
    print(input('Please enter a name of a Boy :'))
    input_file.close()

    index = 0
    while index < len(boy_names):
        boy_names[index] = boy_names[index].rstrip('\n')
        index += 1

    print(boy_names)

    if 'Ryan' in boy_names:
        print('yes, is on the popular list. ')
    else:
        print('no, is not on the popular list. ')

    input_file = open('GirlNames.txt', 'r')
    girl_names = input_file.readlines()
    print(input('Please enter a name of a Girl :'))
    input_file.close()

    index = 0
    while index < len(girl_names):
        girl_names[index] = girl_names[index].rstrip('\n')
        index += 1

    print(girl_names)

    if 'Camila' in girl_names:
        print('yes, is on the popular list. ')
    else:
        print('no, is not on the popular list. ')


main()
