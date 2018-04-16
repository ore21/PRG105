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
    local_base = int(input(" Enter an integer for base :"))
    local_power = int(input(" Enter an integer for Exponent :"))
    local_result = 0
    print("Your answer is :")
    exponent(local_base, local_power, local_result)


main()
