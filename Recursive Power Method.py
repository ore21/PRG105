"""Recursive Power Method"""


def exponent(base, power, result):
    if result == 0:
        temp = base
    else:
        temp = result

    power -= 1
    result = temp * base

    if power > 1:
        exponent(base, power, result)
    else:
        print(result)


def main():
    local_base = input(" Enter an integer for base :")
    local_power = input(" Enter an integer for Exponent :")
    local_result = int(local_base * int(local_power))
    print(local_base, local_power)
    print("your answer is :", local_result)


main()
