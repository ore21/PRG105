""""personal information class"""


class PersonalInfo:
    def __init__(self, names, addresses, ages, numbers):
        self.__names = names
        self.__addresses = addresses
        self.__ages = ages
        self.__numbers = numbers

    def set_names(self, name):
        self.__names = name

    def set_addresses(self, address):
        self.__addresses = address

    def set_ages(self, age):
        self.__ages = age

    def set_numbers(self, number):
        self.__numbers = number

    def get_names(self):
        return self.__names

    def get_addresses(self):
        return self.__addresses

    def get_ages(self):
        return self.__ages

    def get_numbers(self):
        return self.__numbers


def main(self):
    info = PersonalInfo(self)

    info.set_names("Ben")
    info.set_addresses("123 6th St. Melbourne, FL 32904")
    info.set_ages("18")
    info.set_numbers("800-576-5677")

    print("Name:"), info.get_names()
    print("Address:"), info.get_addresses()
    print("Age:"), info.get_ages()
    print("Phone Number:"), info.get_numbers()
    print()

    info.set_names("Bill")
    info.set_addresses("71 Pilgrim Avenue Chevy Chase, MD 20815")
    info.set_ages("20")
    info.set_numbers("745-600-3454")

    print("Name:"), info.get_names()
    print("Address:"), info.get_addresses()
    print("Age:"), info.get_ages()
    print("Phone Number:"), info.get_numbers()
    print()

    info.set_names("Jack")
    info.set_addresses("70 Bowman St. South Windsor, CT 06074")
    info.set_ages("25")
    info.set_numbers("800-678-4492")

    print("Name:"), info.get_names()
    print("Address:"), info.get_addresses()
    print("Age:"), info.get_ages()
    print("Phone Number:"), info.get_numbers()
    print()


main()
